import numpy as np
from typing import List


class Solution:
    def rms_norm(self, x: List[float], gamma: List[float], eps: float) -> List[float]:
        # Implement RMS Normalization (similar to LayerNorm but without mean centering or beta)
        # Normalize x, then scale by gamma
        # Return result rounded to 4 decimal places as a list
        x_sq = np.square(x)
        rms = np.sqrt(np.mean(x_sq)+eps)
        x_norm = x/rms
        output = gamma*x_norm
        return np.round(output, 4)
