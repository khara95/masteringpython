
# coding: utf-8

# In[ ]:

"""
Price a down-and-out option by the Crank-Nicolson
method of finite differences.
"""
import numpy as np
from FDCnEu import FDCnEu

class FDCnDo(FDCnEu):
    def __init__(self, S0, K, r, T, sigma, Sbarrier, Smax, M, N,
                 is_call=True):
        super(FDCnDo, self).__init__(S0, K, r, T, sigma, Smax, M, N, is_call)
        self.dS = (Smax-Sbarrier)/float(self.M)
        self.boundary_conds = np.linspace(Sbarrier,
                                          Smax,
                                          self.M+1)
        self.i_values = self.boundary_conds/self.dS

