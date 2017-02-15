
# coding: utf-8

# In[ ]:

""" Crank-Nicolson method of Finite Differences """
import numpy as np
import scipy.linalg as linalg
from FDExplicitEu import FDExplicitEu
class FDCnEu(FDExplicitEu):
    def _setup_coefficients_(self):
        self.alpha = 0.25*self.dt*(
            (self.sigma**2)*(self.i_values**2) -
            self.r*self.i_values)
        self.beta = -self.dt*0.5*(
            (self.sigma**2)*(self.i_values**2) +
            self.r)
        self.gamma = 0.25*self.dt*(
            (self.sigma**2)*(self.i_values**2) +
            self.r*self.i_values)
        self.M1 = -np.diag(self.alpha[2:self.M], -1) +             np.diag(1-self.beta[1:self.M]) -             np.diag(self.gamma[1:self.M-1], 1)
        self.M2 = np.diag(self.alpha[2:self.M], -1) +             np.diag(1+self.beta[1:self.M]) +             np.diag(self.gamma[1:self.M-1], 1)
    def _traverse_grid_(self):
        """ Solve using linear systems of equations """
        P, L, U = linalg.lu(self.M1)
        for j in reversed(range(self.N)):
            x1 = linalg.solve(L,np.dot(self.M2,self.grid[1:self.M, j+1]))
            x2 = linalg.solve(U, x1)
            self.grid[1:self.M, j] = x2

