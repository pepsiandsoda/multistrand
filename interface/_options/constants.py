################################################################################
#                                                                              #
# Important Constants for Multistrand.                                         #
# Copyright 2010 Caltech                                                       #
# Written by:  Joseph Schaeffer.                                               #
#                                                                              #
#                                                                              #
#                                                                              #
################################################################################


class _OptionsConstants( object ):
    def __init__(self):
        self.ZERO_C_IN_K = 273.15
        pass
    
    @property
    def RATEMETHOD(self):
        return {"Invalid" :0, "Metropolis"    :1, \
                "Kawasaki":2, "EntropyEnthalpy":3}

    @property
    def DANGLES(self):
        return {"None":  0, "Some" : 1, \
                "All" :  2, "NupackDefault": 1}

    @property
    def ENERGYMODEL_TYPE(self):
        return {"Vienna":0, "Nupack":1, \
                "Others?":2}

    @property
    def SUBSTRATE_TYPE(self):
        return {"Invalid":0, "RNA":1, \
                "DNA":2}

    @property
    def SIMULATION_MODE(self):
        return {"Normal":                   0x0010,
                "First Step":               0x0030,
                "Python Module":            0x0040,
                "Python Module:First Step": 0x0060,
                "Energy Only":              0x0200}

    @property
    def SIMULATION_MODE_FLAG(self):
        return {"Normal":                   0x0010,
                "First Bimolecular":        0x0020,
                "Python Module":            0x0040}

    @property
    def STOPRESULT(self):
        return {"Normal":                   0x0011,
                "Time":                     0x0012,
                "Forward":                  0x0021,
                "Time (First Step)":        0x0022,
                "Reverse":                  0x0024,
                "Error":                    0x0081,
                "NaN":                      0x0082,
                "No Moves":                 0x0084}

    @property
    def STOPRESULT_inv(self):
        return {0x0011:                   "Normal",
                0x0012:                     "Time",
                0x0021:                  "Forward",
                0x0022:        "Time (First Step)",
                0x0024:                  "Reverse",
                0x0081:                    "Error",
                0x0082:                      "NaN",
                0x0084:                 "No Moves"}

    def __setattr__(self, name, value):
        if hasattr(self, name):
            pass
        else:
            object.__setattr__(self, name, value)
    
    def __delattr__(self, *args, **kargs):
        pass

Constants = _OptionsConstants()