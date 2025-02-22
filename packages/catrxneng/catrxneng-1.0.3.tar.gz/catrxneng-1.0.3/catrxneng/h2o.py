from .utils import dHf, Sf, Gf


class H2O():
    def __init__(self, T_C):

        self.T_C = T_C
        self.T_K = self.T_C + 273
        if self.T_K < 500 or self.T_K > 1700:
            raise ValueError("Invalid temperature.")
        self.Hf_298 = -241.83  # kJ/mol
        self.thermo_params = {
            "A": 30.09200,
            "B": 6.832514,
            "C": 6.793435,
            "D": -2.534480,
            "E": 0.082139,
            "F": -250.8810,
            "G": 223.3967,
            "H": -241.8264
        }

    def Hf(self):
        return self.Hf_298 + dHf(self)  # kJ/mol

    def Sf(self):
        return Sf(self)  # kJ/mol

    def Gf(self):
        return Gf(self)  # kJ/mol
