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
def bernoulli(p):
    # p é a taxa de sucesso
    random_number = random.random() # gerando um número aleatório entre 0 e 1
    if random_number < p:
        return 1
    else:
        return 0
#endregion

#region Distribuição PERT
import math
#from pert import PERT

#region Distribuição LogNormal
import math

def lognormal(mu_ln: float, sigma_ln: float) -> float:
    # gerar um número normal a partir de μ e σ do log
    z = normal(mu_ln, sigma_ln)
    
    # converter para lognormal
    return math.exp(z)

#endregion

# ==================================================

#region Distribuição Gamma
def gamma(a, b, c):
    # So traduzi do documento pra python

    assert b > 0 and c > 0

    A = 1. / math.sqrt(2. * c - 1.)
    B = c  - math.log(4.)
    Q = c  + 1. / A
    T = 4.5
    D = 1. + math.log(T)
    C = 1. + c / math.e

    if c < 1.0:
        # caso c < 1 
        while True:
            p = C * random.uniform(0., 1.)
            if p > 1.:
                y = -math.log((C - p) / c)
                if random.uniform(0., 1.) <= y**(c-1):
                    return a + b * y
            else:
                y = p**(1. / c)
                if random.uniform(0., 1.) <= math.exp(-y):
                    return a + b * y

    elif c == 1.0:
        # caso c = 1 - vira uma exponential
        return a + b * (-math.log(random.uniform(0., 1.)))

    else:
        # caso c > 1
        while True:
            pi = random.uniform(0., 1.)
            p2 = random.uniform(0., 1.)
            v = A * math.log(pi / (1. - pi))
            y = c * math.exp(v)
            z = pi * pi * p2
            w = B + Q * v - y
            if w + D - T * z >= 0. or w >= math.log(z):
                return a + b * y
#endregion

#region Distribuição Beta
# Gerador Dist. Beta
def beta(alpha, beta):
    # Gera um X e Y seguindo dist Gamma
    x = gamma(0, 1, alpha )
    y = gamma(0, 1, beta  )
    # Calcula a variavel Beta
    varBeta = x / (x + y)

    # Retorna a variavel Beta
    return varBeta

#endregion

#region Deistribuição PERT
def pert(min, moda, max, *, lamb=4):
    # - lambda controla quao concentrado a dist vai ser em torno da moda

    # calcula o range
    r = max - min

    # calcula os parametros pra funcao beta
    beta_a = 1 + lamb * (moda - min) / r
    beta_b = 1 + lamb * (max - moda) / r

    # pega a variavel beta e ajusta ela pra escalar com o intervalo correto
    varBeta = beta(beta_a, beta_b)
    varPERT = min + (varBeta * r)

    # Retorna a variavel PERT
    return varPERT

#endregion
# Formula pra gerar randPERT baseado em:
# https://stackoverflow.com/questions/68476485/random-values-from-a-pert-distribution-in-python

#endregion

#region Plots
#gerando 10 mil números aleatórios (o metodo da normal gera um número por vez  usando o metodo de box muller)
plot_normal = [normal(0,1) for _ in range(100000)] #amostras é uma lista
plot_bernoulli = [bernoulli(0.4) for _ in range(1000000)]
plot_pert = [pert(0, 5, 10) for _ in range(1000000)]

plot_lognormal = [lognormal(0, 0.25) for _ in range(200000)]  # μ=0, σ=0.25

#plotando o histograma normal
plt.figure(figsize=(8, 5))
plt.hist(plot_normal, bins=80, density=True, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribuição Normal gerada pelo método de Box-Muller')
plt.xlabel('Valores')
plt.ylabel('Densidade de probabilidade')
plt.grid(True, alpha=0.3)
plt.show()

#plotando o histograma bernoulli
plt.hist(plot_bernoulli, bins=2, density=True, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribuição Bernoulli')
plt.xlabel('Valores')
plt.ylabel('Densidade de probabilidade')
plt.grid(True, alpha=0.3)
plt.show()

#plotando o histograma pert
plt.figure(figsize=(8, 5))
plt.hist(plot_pert, bins=80, density=True, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribuição PERT')
plt.xlabel('Valores')
plt.ylabel('Densidade de probabilidade')
plt.grid(True, alpha=0.3)
plt.show()

# Distribuição LogNormal
plt.figure(figsize=(8, 5))
plt.hist(plot_lognormal, bins=80, density=True, color='skyblue', edgecolor='black', alpha=0.7)
plt.title('Distribuição LogNormal gerada a partir da Normal')
plt.xlabel('Valores')
plt.ylabel('Densidade de probabilidade')
plt.grid(True, alpha=0.3)
plt.show()

#endregion