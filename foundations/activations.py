import numpy as np
from numpy.typing import NDArray


class Solution:
    
    def sigmoid(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        z_sig = 1 / (1 + np.exp(-z))
        return np.round(z_sig, 5)
        

    def relu(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array
        z_new = []
        for value in z:
            if value <= 0.0:
                value = 0.0
            z_new.append(value)

        return z_new
        
