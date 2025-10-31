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
#endregion

#region Distribuição Bernoulli
import random
import matplotlib.pyplot as plt

## Gerador de Números Aleatórios Segundo Distribuição de Bernoulli
def bernoulli_generator(p):
    # p é a taxa de sucesso
    random_number = random.random() # gerando um número aleatório entre 0 e 1
    if random_number < p:
        return 1
    else:
        return 0
#endregion

#region Plots
#gerando 10 mil números aleatórios (o metodo da normal gera um número por vez  usando o metodo de box muller)
plot_normal = [normal(0,1) for _ in range(100000)] #amostras é uma lista
plot_bernoulli = [bernoulli_generator(0.4) for _ in range(1000000)]

#plotando o histograma
plt.figure(figsize=(8, 5))
plt.hist(plot_normal, bins=80, density=True, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribuição Normal gerada pelo método de Box-Muller')
plt.xlabel('Valores')
plt.ylabel('Densidade de probabilidade')
plt.grid(True, alpha=0.3)
plt.show()

plt.hist(plot_bernoulli, bins=80, density=True, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribuição Bernoulli')
plt.xlabel('Valores')
plt.ylabel('Densidade de probabilidade')
plt.grid(True, alpha=0.3)
plt.show()
#endregion


