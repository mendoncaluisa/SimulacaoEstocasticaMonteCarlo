import random

## Gerador de Números Aleatórios Segundo Distribuição de Bernoulli
def bernoulli_generator(p):
    # p é a taxa de sucesso
    random_number = random.random() # gerando um número aleatório entre 0 e 1
    if random_number <= p:
        return 1
    else:
        return 0
