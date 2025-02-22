from OpenSimula.Parameters import Parameter_float, Parameter_float_list, Parameter_math_exp, Parameter_options, Parameter_boolean
from OpenSimula.Component import Component
from scipy.optimize import fsolve

class HVAC_DX_equipment(Component):
    def __init__(self, name, project):
        Component.__init__(self, name, project)
        self.parameter("type").value = "HVAC_DX_equipment"
        self.parameter("description").value = "HVAC Direct Expansion equipment manufacturer information"
        self.add_parameter(Parameter_float("nominal_air_flow", 1, "m³/s", min=0))
        self.add_parameter(Parameter_float("nominal_total_cooling_capacity", 0, "W", min=0))
        self.add_parameter(Parameter_float("nominal_sensible_cooling_capacity", 0, "W", min=0))
        self.add_parameter(Parameter_float("nominal_cooling_power", 0, "W", min=0))
        self.add_parameter(Parameter_float("no_load_power", 0, "W", min=0))
        self.add_parameter(Parameter_float("no_load_heat", 0, "W", min=0))
        self.add_parameter(Parameter_float_list("nominal_cooling_conditions", [27, 19, 35], "ºC"))
        self.add_parameter(Parameter_math_exp("total_cooling_capacity_expression", "1", "frac"))
        self.add_parameter(Parameter_math_exp("sensible_cooling_capacity_expression", "1", "frac"))
        self.add_parameter(Parameter_math_exp("cooling_power_expression", "1", "frac"))
        self.add_parameter(Parameter_math_exp("EER_expression", "1", "frac"))
        self.add_parameter(Parameter_float("nominal_heating_capacity", 0, "W", min=0))
        self.add_parameter(Parameter_float("nominal_heating_power", 0, "W", min=0))
        self.add_parameter(Parameter_float_list("nominal_heating_conditions", [20, 7, 6], "ºC"))
        self.add_parameter(Parameter_math_exp("heating_capacity_expression", "1", "frac"))
        self.add_parameter(Parameter_math_exp("heating_power_expression", "1", "frac"))
        self.add_parameter(Parameter_math_exp("COP_expression", "1", "frac"))
        self.add_parameter(Parameter_options("dry_coil_model", "SENSIBLE", ["TOTAL", "SENSIBLE"]))
        self.add_parameter(Parameter_boolean("power_dry_coil_correction", True))
        self.add_parameter(Parameter_float_list("expression_max_values", [60,30,60,30,1.5,1], "-"))
        self.add_parameter(Parameter_float_list("expression_min_values", [0,0,-30,-30,0,0], "-"))

    def check(self):
        errors = super().check()
        # Test Cooling and Heating conditions 3 values
        if len(self.parameter("nominal_cooling_conditions").value)!= 3:
            errors.append(f"Error: {self.parameter('name').value}, nominal_cooling_conditions size must be 3")
        if len(self.parameter("nominal_heating_conditions").value)!= 3:
            errors.append(f"Error: {self.parameter('name').value}, nominal_heating_conditions size must be 3")
        return errors
    
    def get_cooling_capacity(self,T_idb,T_iwb,T_odb,T_owb,F_air):
        total_capacity = self.parameter("nominal_total_cooling_capacity").value
        if total_capacity > 0:
            # variables dictonary
            var_dic = self._var_state_dic([T_idb, T_iwb,T_odb,T_owb,F_air,0])
            # Total
            f = self.parameter("total_cooling_capacity_expression").evaluate(var_dic)
            total_capacity = total_capacity * f
            # Sensible
            sensible_capacity = self.parameter("nominal_sensible_cooling_capacity").value
            f = self.parameter("sensible_cooling_capacity_expression").evaluate(var_dic)
            sensible_capacity = sensible_capacity * f
            if (sensible_capacity > total_capacity):
                if self.parameter("dry_coil_model").value == "SENSIBLE":
                    total_capacity = sensible_capacity
                elif self.parameter("dry_coil_model").value == "TOTAL":
                    sensible_capacity = total_capacity
            return (total_capacity, sensible_capacity)
        else:
            return (0,0)
    
    def get_heating_capacity(self,T_idb,T_iwb,T_odb,T_owb,F_air):
        capacity = self.parameter("nominal_heating_capacity").value
        if capacity > 0:
            # variables dictonary
            var_dic = self._var_state_dic([T_idb, T_iwb,T_odb,T_owb,F_air,0])
            # Capacity
            capacity = capacity * self.parameter("heating_capacity_expression").evaluate(var_dic)
            return capacity
        else:
            return 0
    
    def get_cooling_state(self,T_idb,T_iwb,T_odb,T_owb,F_air,F_load):
        total_capacity, sensible_capacity = self.get_cooling_capacity(T_idb,T_iwb,T_odb,T_owb,F_air)
        if total_capacity > 0:
            if (F_load > 0):
                # variables dictonary
                var_dic = self._var_state_dic([T_idb, T_iwb,T_odb,T_owb,F_air,F_load])
                # con
                power_full = self._get_correct_cooling_power(total_capacity,sensible_capacity,var_dic)

                EER_full = total_capacity/power_full
                F_EER = self.parameter("EER_expression").evaluate(var_dic) 
                EER = EER_full * F_EER 
                power = total_capacity*F_load/EER + self.parameter("no_load_power").value
                return (total_capacity*F_load, sensible_capacity*F_load, power, F_EER)
            else:
                return ( 0 , 0 , self.parameter("no_load_power").value, 0 )
        else:
            return (0,0,0,0)
        
    def _get_correct_cooling_power(self,total_capacity, sensible_capacity, var_dic):
        power = self.parameter("nominal_cooling_power").value
        if (sensible_capacity == total_capacity and self.parameter("power_dry_coil_correction").value):
            T_iwb_min = self._get_min_T_iwb(var_dic)
            var_dic["T_iwb"] = T_iwb_min
        f = self.parameter("cooling_power_expression").evaluate(var_dic)
        return (power * f)
                  
    def _get_min_T_iwb(self,var_dic):
        total_capacity = self.parameter("nominal_total_cooling_capacity").value
        sensible_capacity = self.parameter("nominal_sensible_cooling_capacity").value
        def func(T_iwb):
            var_dic["T_iwb"] = T_iwb
            return (sensible_capacity*self.parameter("sensible_cooling_capacity_expression").evaluate(var_dic)-
                    total_capacity*self.parameter("total_cooling_capacity_expression").evaluate(var_dic))
        root = fsolve(func, var_dic["T_iwb"],xtol=1e-3)
        return root[0]
    
    def get_heating_state(self,T_idb, T_iwb,T_odb,T_owb,F_air,F_load):
        capacity = self.get_heating_capacity(T_idb, T_iwb, T_odb,T_owb,F_air)
        if capacity > 0:
            if (F_load > 0):
                # variables dictonary
                var_dic = self._var_state_dic([T_idb, T_iwb,T_odb,T_owb,F_air,F_load])
                # Compressor
                power_full = self.parameter("nominal_heating_power").value
                power_full = power_full * self.parameter("heating_power_expression").evaluate(var_dic)
                COP_full = capacity/power_full
                F_COP = self.parameter("COP_expression").evaluate(var_dic) 
                COP = COP_full * F_COP
                power = capacity*F_load/COP + + self.parameter("no_load_power").value
                return (capacity*F_load, power, F_COP)
            else:
                return (0,self.parameter("no_load_power").value, 0)
        else:
            return (0,0,0)
    
    def _var_state_dic(self, values):
        max = self.parameter("expression_max_values").value
        min = self.parameter("expression_min_values").value
        for i in range(len(values)):
            if (values[i] > max[i]):
                values[i] = max[i]
            elif (values[i] < min[i]):
                values[i] = min[i]
        return {"T_idb":values[0],
                "T_iwb":values[1],
                "T_odb":values[2],
                "T_owb":values[3],
                "F_air":values[4],
                "F_load":values[5]}




        