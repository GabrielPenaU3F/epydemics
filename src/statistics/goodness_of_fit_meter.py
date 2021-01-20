import numpy as np

class GoodnessOfFitMeter():

    def calculate_coefficient_of_determination(self, explained, real):
        explained_variance = np.var(explained)
        real_variance = np.var(real)
        return explained_variance/real_variance