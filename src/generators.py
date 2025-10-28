#region Distribuição Normal
from scipy.stats import uniform
import random
import numpy as np
import matplotlib.pyplot as plt

def normal(media: float, desvio_padrao: float) -> float:
    if (desvio_padrao > 0):
        while True:
            p1 = random.uniform(-1,1)
            p2 = random.uniform(-1,1)
            p = p1 * p1 + p2 * p2

            if p < 1:
                break

        return media + desvio_padrao * p1 * np.sqrt(-2. * np.log(p) / p)

#gerando 10 mil números aleatórios (o metodo da normal gera um número por vez  usando o metodo de box muller)
amostras = [normal(0,1) for _ in range(100000)] #amostras é uma lista

#plotando o histograma
plt.figure(figsize=(8, 5))
plt.hist(amostras, bins=80, density=True, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribuição Normal gerada pelo método de Box-Muller')
plt.xlabel('Valores')
plt.ylabel('Densidade de probabilidade')
plt.grid(True, alpha=0.3)
plt.show()

#endregion