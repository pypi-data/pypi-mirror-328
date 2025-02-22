from .utils import dHf, Sf, Gf


class H2:
    def __init__(self, T_C):

        self.T_C = T_C
        self.T_K = self.T_C + 273
        if self.T_K < 298 or self.T_K > 1000:
            raise ValueError("Invalid temperature.")
        self.Hf_298 =  0 # kJ/mol
        self.thermo_params = {
            "A": 33.066178,
            "B": -11.363417,
            "C": 11.432816,
            "D": -2.772874,
            "E": -0.158558,
            "F": -9.980797,
            "G": 172.707974,
            "H": 0,
        }

    def Hf(self):
        return self.Hf_298 + dHf(self)  # kJ/mol

    def Sf(self):
        return Sf(self)  # kJ/mol

    def Gf(self):
        return Gf(self)  # kJ/mol
