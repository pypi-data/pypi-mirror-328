from .utils import dHf, Sf, Gf


class CO:
    def __init__(self, T_C):
        # https://webbook.nist.gov/cgi/cbook.cgi?ID=C630080&Units=SI&Mask=1#Thermo-Gas
        self.T_C = T_C
        self.T_K = self.T_C + 273
        if self.T_K < 298 or self.T_K > 1300:
            raise ValueError("Invalid temperature.")
        self.Hf_298 = -110.53  # kJ/mol
        self.thermo_params = {
            "A": 25.56759,
            "B": 6.096130,
            "C": 4.054656,
            "D": -2.671301,
            "E": 0.131021,
            "F": -118.0089,
            "G": 227.3665,
            "H": -110.5271,
        }

    def Hf(self):
        return self.Hf_298 + dHf(self)  # kJ/mol

    def Sf(self):
        return Sf(self)  # kJ/mol

    def Gf(self):
        return Gf(self)  # kJ/mol
