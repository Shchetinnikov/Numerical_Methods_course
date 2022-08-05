import numpy as np

xx = np.linspace(0, 1, 110)
Van_matrix = np.vander(xx)
cond = np.linalg.cond(Van_matrix)
print("Число обусловленности для определителя Вандермонда = %1f" %cond)