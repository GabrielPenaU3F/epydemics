import numpy as np
from matplotlib import pyplot as plt

from src.domain.models.model import PenaSigmoidModel

x = np.linspace(0, 10000, 100000)
model = PenaSigmoidModel()
rho_x_1 = model.rho(x, 0, 250, 0.2, -0.1)
rho_x_2 = model.rho(x, 0, 250, 0.2, -0.5)
rho_x_3 = model.rho(x, 0, 250, 0.2, -2)
# plt.plot(x, rho_x_1, label='M = -0.1')
plt.plot(x, rho_x_2, label='M = -0.5')
plt.plot(x, rho_x_3, label='M = -2')

plt.legend()
plt.show()
