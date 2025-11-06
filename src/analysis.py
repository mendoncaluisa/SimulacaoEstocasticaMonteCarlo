import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# adiciona o diretorio pai ao path pra conseguir importar o main
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import cenario_1, cenario_2, cenario_3

#region Simulação Monte Carlo
def monte_carlo(cenario_func, n_simulacoes=10000):
    # listas pra armazenar os resultados
    tempos = []
    custos = []
    
    # roda n simulacoes
    for i in range(n_simulacoes):
        tempo, custo = cenario_func()
        tempos.append(tempo)
        custos.append(custo)
        
        # mostra progresso a cada 1000 simulacoes
        if (i + 1) % 1000 == 0:
            print(f"Progresso: {i + 1}/{n_simulacoes} simulações completas")
    
    # converte pra numpy array pra facilitar os calculos
    tempos = np.array(tempos)
    custos = np.array(custos)
    
    # calcula estatisticas
    resultados = {
        'tempo': {
            'media': np.mean(tempos),
            'desvio_padrao': np.std(tempos),
            'minimo': np.min(tempos),
            'maximo': np.max(tempos),
            'percentil_5': np.percentile(tempos, 5),
            'percentil_25': np.percentile(tempos, 25),
            'percentil_50': np.percentile(tempos, 50),  
            'percentil_75': np.percentile(tempos, 75),
            'percentil_95': np.percentile(tempos, 95),
            'dados': tempos
        },
        'custo': {
            'media': np.mean(custos),
            'desvio_padrao': np.std(custos),
            'minimo': np.min(custos),
            'maximo': np.max(custos),
            'percentil_5': np.percentile(custos, 5),
            'percentil_25': np.percentile(custos, 25),
            'percentil_50': np.percentile(custos, 50),  
            'percentil_75': np.percentile(custos, 75),
            'percentil_95': np.percentile(custos, 95),
            'dados': custos
        }
    }
    
    return resultados
#endregion


#region Visualização dos Resultados
def plotar_resultados(resultados, nome_cenario):    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # histograma de tempo
    ax1.hist(resultados['tempo']['dados'], bins=50, density=True, 
             color='skyblue', edgecolor='black', alpha=0.7)
    ax1.axvline(resultados['tempo']['media'], color='red', 
                linestyle='--', linewidth=2, label=f"Média: {resultados['tempo']['media']:.2f}")
    ax1.axvline(resultados['tempo']['percentil_50'], color='green', 
                linestyle='--', linewidth=2, label=f"Mediana: {resultados['tempo']['percentil_50']:.2f}")
    ax1.set_title(f'Distribuição de Tempo - {nome_cenario}')
    ax1.set_xlabel('Tempo (dias)')
    ax1.set_ylabel('Densidade de probabilidade')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # histograma de custo
    ax2.hist(resultados['custo']['dados'], bins=50, density=True, 
             color='lightcoral', edgecolor='black', alpha=0.7)
    ax2.axvline(resultados['custo']['media'], color='red', 
                linestyle='--', linewidth=2, label=f"Média: R$ {resultados['custo']['media']:,.2f}")
    ax2.axvline(resultados['custo']['percentil_50'], color='green', 
                linestyle='--', linewidth=2, label=f"Mediana: R$ {resultados['custo']['percentil_50']:,.2f}")
    ax2.set_title(f'Distribuição de Custo - {nome_cenario}')
    ax2.set_xlabel('Custo (R$)')
    ax2.set_ylabel('Densidade de probabilidade')
    ax2.legend()
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
#endregion


#region Relatório de Estatísticas
def gerar_relatorio(resultados, nome_cenario):
    print(f"\n{'='*60}")
    print(f"RELATÓRIO DE ESTATÍSTICAS - {nome_cenario}")
    print(f"{'='*60}\n")
    
    print("TEMPO (dias):")
    print(f"  Média:           {resultados['tempo']['media']:.2f}")
    print(f"  Desvio Padrão:   {resultados['tempo']['desvio_padrao']:.2f}")
    print(f"  Mínimo:          {resultados['tempo']['minimo']:.2f}")
    print(f"  Máximo:          {resultados['tempo']['maximo']:.2f}")
    print(f"  Percentil 5%:    {resultados['tempo']['percentil_5']:.2f}")
    print(f"  Percentil 25%:   {resultados['tempo']['percentil_25']:.2f}")
    print(f"  Mediana (50%):   {resultados['tempo']['percentil_50']:.2f}")
    print(f"  Percentil 75%:   {resultados['tempo']['percentil_75']:.2f}")
    print(f"  Percentil 95%:   {resultados['tempo']['percentil_95']:.2f}")
    
    print("\nCUSTO (R$):")
    print(f"  Média:           R$ {resultados['custo']['media']:,.2f}")
    print(f"  Desvio Padrão:   R$ {resultados['custo']['desvio_padrao']:,.2f}")
    print(f"  Mínimo:          R$ {resultados['custo']['minimo']:,.2f}")
    print(f"  Máximo:          R$ {resultados['custo']['maximo']:,.2f}")
    print(f"  Percentil 5%:    R$ {resultados['custo']['percentil_5']:,.2f}")
    print(f"  Percentil 25%:   R$ {resultados['custo']['percentil_25']:,.2f}")
    print(f"  Mediana (50%):   R$ {resultados['custo']['percentil_50']:,.2f}")
    print(f"  Percentil 75%:   R$ {resultados['custo']['percentil_75']:,.2f}")
    print(f"  Percentil 95%:   R$ {resultados['custo']['percentil_95']:,.2f}")
    
    print(f"\n{'='*60}\n")
#endregion


#region Comparação entre Cenários
def comparar_cenarios(resultados_dict):
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # boxplot de tempos
    tempos_data = [resultados['tempo']['dados'] for resultados in resultados_dict.values()]
    ax1.boxplot(tempos_data, labels=resultados_dict.keys())
    ax1.set_title('Comparação de Tempo entre Cenários')
    ax1.set_ylabel('Tempo (dias)')
    ax1.grid(True, alpha=0.3)
    
    # boxplot de custos
    custos_data = [resultados['custo']['dados'] for resultados in resultados_dict.values()]
    ax2.boxplot(custos_data, labels=resultados_dict.keys())
    ax2.set_title('Comparação de Custo entre Cenários')
    ax2.set_ylabel('Custo (R$)')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # tabela comparativa
    print(f"\n{'='*80}")
    print("TABELA COMPARATIVA DOS CENÁRIOS")
    print(f"{'='*80}")
    print(f"{'Cenário':<15} {'Tempo Médio':<15} {'Custo Médio':<20}")
    print(f"{'-'*80}")
    for nome, resultados in resultados_dict.items():
        print(f"{nome:<15} {resultados['tempo']['media']:>10.2f} dias  R$ {resultados['custo']['media']:>15,.2f}")
    print(f"{'='*80}\n")
#endregion


#region Execução Principal
if __name__ == "__main__":
    # define o numero de simulacoes
    N_SIMULACOES = 10000
    
    print("Iniciando simulações Monte Carlo...")
    print(f"Número de simulações por cenário: {N_SIMULACOES}\n")
    
    # executa simulacao para cada cenario
    print("Executando Cenário 1...")
    resultados_c1 = monte_carlo(cenario_1, N_SIMULACOES)
    gerar_relatorio(resultados_c1, "Cenário 1")
    plotar_resultados(resultados_c1, "Cenário 1")
    
    print("\nExecutando Cenário 2...")
    resultados_c2 = monte_carlo(cenario_2, N_SIMULACOES)
    gerar_relatorio(resultados_c2, "Cenário 2")
    plotar_resultados(resultados_c2, "Cenário 2")
    
    print("\nExecutando Cenário 3...")
    resultados_c3 = monte_carlo(cenario_3, N_SIMULACOES)
    gerar_relatorio(resultados_c3, "Cenário 3")
    plotar_resultados(resultados_c3, "Cenário 3")
    
    # compara todos os cenarios
    print("\nGerando comparação entre cenários...")
    comparar_cenarios({
        'Cenário 1': resultados_c1,
        'Cenário 2': resultados_c2,
        'Cenário 3': resultados_c3
    })
    
    print("Simulações concluídas!")
#endregion