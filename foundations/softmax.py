import numpy as np
from numpy.typing import NDArray


class Solution:

    def softmax(self, z: NDArray[np.float64]) -> NDArray[np.float64]:
        # z is a 1D NumPy array of logits
        # Hint: subtract max(z) for numerical stability before computing exp
        z_stable = z - np.max(z)
        z_new = np.exp(z_stable)/np.sum(np.exp(z_stable))
        return np.round(z_new, 4)
        
