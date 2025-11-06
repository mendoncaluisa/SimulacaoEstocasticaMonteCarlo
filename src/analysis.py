import numpy as np
import matplotlib.pyplot as plt
import sys
import os

# adiciona o diretorio pai ao path pra conseguir importar o main
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import cenario_1, cenario_2, cenario_3

#region Simulação Monte Carlo
def monte_carlo(cenario_func, prazo_contratual, multa_diaria, preco_contrato, n_simulacoes=10000):
    # listas pra armazenar os resultados
    tempos = []
    custos_base = []  # custo SEM multa
    custos_totais = []  # custo COM multa
    
    # roda n simulacoes
    for i in range(n_simulacoes):
        tempo, custo_base = cenario_func()
        
        # calcula multa se houver atraso
        if tempo > prazo_contratual:
            dias_atraso = tempo - prazo_contratual
            multa = dias_atraso * multa_diaria
            custo_total = custo_base + multa
        else:
            custo_total = custo_base
        
        tempos.append(tempo)
        custos_base.append(custo_base)
        custos_totais.append(custo_total)
        
        # mostra progresso a cada 1000 simulacoes
        if (i + 1) % 1000 == 0:
            print(f"Progresso: {i + 1}/{n_simulacoes} simulações completas")
    
    # converte pra numpy array
    tempos = np.array(tempos)
    custos_base = np.array(custos_base)
    custos_totais = np.array(custos_totais)

    # 1a Métrica: Probabilidade de Prejuízo
    prob_prejuizo = calcular_probabilidade_prejuizo(custos_totais, preco_contrato)
    
    # 2a Métrica: Valor médio de multa por atraso
    multa_media = calcular_multa_media_quando_atrasa(tempos, prazo_contratual, multa_diaria)
    
    # 3a Métrica: já calculado acima como custos_totais
    
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
        'custo_base': {
            'media': np.mean(custos_base),
            'desvio_padrao': np.std(custos_base),
            'minimo': np.min(custos_base),
            'maximo': np.max(custos_base),
            'percentil_5': np.percentile(custos_base, 5),
            'percentil_25': np.percentile(custos_base, 25),
            'percentil_50': np.percentile(custos_base, 50),
            'percentil_75': np.percentile(custos_base, 75),
            'percentil_95': np.percentile(custos_base, 95),
            'dados': custos_base
        },
        'custo_total': {
            'media': np.mean(custos_totais),
            'desvio_padrao': np.std(custos_totais),
            'minimo': np.min(custos_totais),
            'maximo': np.max(custos_totais),
            'percentil_5': np.percentile(custos_totais, 5),
            'percentil_25': np.percentile(custos_totais, 25),
            'percentil_50': np.percentile(custos_totais, 50),
            'percentil_75': np.percentile(custos_totais, 75),
            'percentil_95': np.percentile(custos_totais, 95),
            'dados': custos_totais
        },
        # 3 métricas principais
        'probabilidade_prejuizo': prob_prejuizo,
        'multa_media_quando_atrasa': multa_media,
        'preco_contrato': preco_contrato,
        'prazo_contratual': prazo_contratual,
        'multa_diaria': multa_diaria,
        'n_simulacoes': n_simulacoes,
        'n_atrasos': np.sum(tempos > prazo_contratual),
        'taxa_atraso': np.sum(tempos > prazo_contratual) / n_simulacoes * 100,
        'n_prejuizos': np.sum(custos_totais > preco_contrato)
    }
    
    return resultados
#endregion


#region Métricas Principais
def calcular_probabilidade_prejuizo(custos_totais, preco_contrato):
    prejuizos = custos_totais > preco_contrato
    prob = np.sum(prejuizos) / len(custos_totais)
    return prob * 100  

def calcular_multa_media_quando_atrasa(tempos, prazo_contratual, multa_diaria):
    # Filtra apenas os casos onde houve atraso
    atrasos = tempos > prazo_contratual
    
    if np.sum(atrasos) == 0:
        # Não houve nenhum atraso em nenhuma simulação
        return 0.0
    
    # Calcula os dias de atraso apenas para os casos com atraso
    dias_atraso = tempos[atrasos] - prazo_contratual
    
    # Calcula as multas correspondentes
    multas = dias_atraso * multa_diaria
    return np.mean(multas)

def calcular_custo_total_medio(custos_base, tempos, prazo_contratual, multa_diaria):
    custos_totais = []
    
    # Calcula o custo total médio considerando multas
    for custo, tempo in zip(custos_base, tempos):
        if tempo > prazo_contratual:
            dias_atraso = tempo - prazo_contratual
            multa = dias_atraso * multa_diaria
            custo_total = custo + multa
        else:
            custo_total = custo
        
        custos_totais.append(custo_total)
    
    return np.mean(custos_totais)
#endregion


#region Visualização dos Resultados
def plotar_resultados(resultados, nome_cenario):    
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
    
    # Histograma de tempo
    ax1.hist(resultados['tempo']['dados'], bins=50, density=True, 
             color='skyblue', edgecolor='black', alpha=0.7)
    ax1.axvline(resultados['tempo']['media'], color='red', 
                linestyle='--', linewidth=2, label=f"Média: {resultados['tempo']['media']:.2f}")
    ax1.axvline(resultados['tempo']['percentil_50'], color='green', 
                linestyle='--', linewidth=2, label=f"Mediana: {resultados['tempo']['percentil_50']:.2f}")
    ax1.axvline(resultados['prazo_contratual'], color='orange',
                linestyle='--', linewidth=2, label=f"Prazo: {resultados['prazo_contratual']}")
    ax1.set_title(f'Distribuição de Tempo - {nome_cenario}')
    ax1.set_xlabel('Tempo (dias)')
    ax1.set_ylabel('Densidade de probabilidade')
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    
    # Histograma de custo total
    ax2.hist(resultados['custo_total']['dados'], bins=50, density=True, 
             color='lightcoral', edgecolor='black', alpha=0.7)
    ax2.axvline(resultados['custo_total']['media'], color='red', 
                linestyle='--', linewidth=2, label=f"Média: R$ {resultados['custo_total']['media']:,.0f}")
    ax2.axvline(resultados['custo_total']['percentil_50'], color='green', 
                linestyle='--', linewidth=2, label=f"Mediana: R$ {resultados['custo_total']['percentil_50']:,.0f}")
    ax2.axvline(resultados['preco_contrato'], color='orange',
                linestyle='--', linewidth=2, label=f"Contrato: R$ {resultados['preco_contrato']:,.0f}")
    ax2.set_title(f'Distribuição de Custo Total - {nome_cenario}')
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

    print(f"Número de simulações: {resultados['n_simulacoes']:,}")
    print(f"Preço do Contrato: R$ {resultados['preco_contrato']:,.2f}")
    print(f"Prazo Contratual: {resultados['prazo_contratual']} dias")
    print(f"Multa Diária: R$ {resultados['multa_diaria']:,.2f}")
    
    print(f"\n{'='*60}")
    print("MÉTRICAS PRINCIPAIS")
    print(f"{'='*60}\n")
    
    # 1a Métrica: Probabilidade de Prejuízo
    print(f"1. PROBABILIDADE DE PREJUÍZO: {resultados['probabilidade_prejuizo']:.2f}%")
    print(f"   - Número de cenários com prejuízo: {resultados['n_prejuizos']:,} de {resultados['n_simulacoes']:,}")
    
    # 2a Métrica: Multa Média 
    print(f"\n2. MULTA MÉDIA (quando há atraso): R$ {resultados['multa_media_quando_atrasa']:,.2f}")
    print(f"   - Taxa de atraso: {resultados['taxa_atraso']:.2f}%")
    print(f"   - Número de cenários com atraso: {resultados['n_atrasos']:,} de {resultados['n_simulacoes']:,}")
    
    # 3a Métrica: Custo Total
    print(f"\n3. CUSTO TOTAL DO PROJETO:")
    print(f"   - Custo médio: R$ {resultados['custo_total']['media']:,.2f}")
    print(f"   - Desvio padrão: R$ {resultados['custo_total']['desvio_padrao']:,.2f}")
    
    print(f"\n{'='*60}")
    print("ESTATÍSTICAS DE TEMPO")
    print(f"{'='*60}\n")

    print(f"  Média:           {resultados['tempo']['media']:.2f} dias")
    print(f"  Desvio Padrão:   {resultados['tempo']['desvio_padrao']:.2f} dias")
    print(f"  Mínimo:          {resultados['tempo']['minimo']:.2f} dias")
    print(f"  Máximo:          {resultados['tempo']['maximo']:.2f} dias")
    print(f"  Percentil 5%:    {resultados['tempo']['percentil_5']:.2f} dias")
    print(f"  Percentil 25%:   {resultados['tempo']['percentil_25']:.2f} dias")
    print(f"  Mediana (50%):   {resultados['tempo']['percentil_50']:.2f} dias")
    print(f"  Percentil 75%:   {resultados['tempo']['percentil_75']:.2f} dias")
    print(f"  Percentil 95%:   {resultados['tempo']['percentil_95']:.2f} dias")
    
    print(f"\n{'='*60}")
    print("ESTATÍSTICAS DE CUSTO BASE (sem multa)")
    print(f"{'='*60}\n")
    
    print(f"  Média:           R$ {resultados['custo_base']['media']:,.2f}")
    print(f"  Desvio Padrão:   R$ {resultados['custo_base']['desvio_padrao']:,.2f}")
    print(f"  Mínimo:          R$ {resultados['custo_base']['minimo']:,.2f}")
    print(f"  Máximo:          R$ {resultados['custo_base']['maximo']:,.2f}")
    print(f"  Percentil 5%:    R$ {resultados['custo_base']['percentil_5']:,.2f}")
    print(f"  Percentil 25%:   R$ {resultados['custo_base']['percentil_25']:,.2f}")
    print(f"  Mediana (50%):   R$ {resultados['custo_base']['percentil_50']:,.2f}")
    print(f"  Percentil 75%:   R$ {resultados['custo_base']['percentil_75']:,.2f}")
    print(f"  Percentil 95%:   R$ {resultados['custo_base']['percentil_95']:,.2f}")
    
    print(f"\n{'='*60}")
    print("ESTATÍSTICAS DE CUSTO TOTAL (com multa)")
    print(f"{'='*60}\n")

    print(f"  Média:           R$ {resultados['custo_total']['media']:,.2f}")
    print(f"  Desvio Padrão:   R$ {resultados['custo_total']['desvio_padrao']:,.2f}")
    print(f"  Mínimo:          R$ {resultados['custo_total']['minimo']:,.2f}")
    print(f"  Máximo:          R$ {resultados['custo_total']['maximo']:,.2f}")
    print(f"  Percentil 5%:    R$ {resultados['custo_total']['percentil_5']:,.2f}")
    print(f"  Percentil 25%:   R$ {resultados['custo_total']['percentil_25']:,.2f}")
    print(f"  Mediana (50%):   R$ {resultados['custo_total']['percentil_50']:,.2f}")
    print(f"  Percentil 75%:   R$ {resultados['custo_total']['percentil_75']:,.2f}")
    print(f"  Percentil 95%:   R$ {resultados['custo_total']['percentil_95']:,.2f}")
    
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
    
    # boxplot de custos totais
    custos_data = [resultados['custo_total']['dados'] for resultados in resultados_dict.values()]
    ax2.boxplot(custos_data, labels=resultados_dict.keys())
    ax2.set_title('Comparação de Custo Total entre Cenários')
    ax2.set_ylabel('Custo (R$)')
    ax2.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
    
    # Tabela comparativa
    print(f"\n{'='*100}")
    print("TABELA COMPARATIVA DOS CENÁRIOS")
    print(f"{'='*100}")
    print(f"{'Cenário':<15} {'Tempo Médio':<15} {'Custo Total Médio':<25} {'Prob. Prejuízo':<18} {'Multa Média':<20}")
    print(f"{'-'*100}")
    for nome, resultados in resultados_dict.items():
        print(f"{nome:<15} {resultados['tempo']['media']:>10.2f} dias  "
              f"R$ {resultados['custo_total']['media']:>18,.2f}  "
              f"{resultados['probabilidade_prejuizo']:>12.2f}%  "
              f"R$ {resultados['multa_media_quando_atrasa']:>15,.2f}")
    print(f"{'='*100}\n")
#endregion


#region Execução Principal
if __name__ == "__main__":
    # define o numero de simulacoes
    N_SIMULACOES = 10000
    
    print("Iniciando simulações Monte Carlo...")
    print(f"Número de simulações por cenário: {N_SIMULACOES}\n")
    
    # Executa o Cenário 1
    print("\n" + "="*60)
    print("EXECUTANDO CENÁRIO 1: EDIFÍCIO RESIDENCIAL")
    print("="*60)
    
    resultados_c1 = monte_carlo(
        cenario_func=cenario_1,
        prazo_contratual=360,
        multa_diaria=3000,
        preco_contrato=19000000,
        n_simulacoes=N_SIMULACOES
    )
    
    gerar_relatorio(resultados_c1, "Cenário 1: Edifício Residencial")
    plotar_resultados(resultados_c1, "Cenário 1: Edifício Residencial")
    
    # Executa o Cenário 2
    print("\n" + "="*60)
    print("EXECUTANDO CENÁRIO 2: GALPÃO LOGÍSTICO")
    print("="*60)
    
    resultados_c2 = monte_carlo(
        cenario_func=cenario_2,
        prazo_contratual=150,
        multa_diaria=5000,
        preco_contrato=4300000,
        n_simulacoes=N_SIMULACOES
    )
    
    gerar_relatorio(resultados_c2, "Cenário 2: Galpão Logístico")
    plotar_resultados(resultados_c2, "Cenário 2: Galpão Logístico")
    
    # Executa o Cenário 3
    print("\n" + "="*60)
    print("EXECUTANDO CENÁRIO 3: CENTRO DE SAÚDE")
    print("="*60)
    
    resultados_c3 = monte_carlo(
        cenario_func=cenario_3,
        prazo_contratual=300,
        multa_diaria=4000,
        preco_contrato=12500000,
        n_simulacoes=N_SIMULACOES
    )
    
    gerar_relatorio(resultados_c3, "Cenário 3: Centro de Saúde")
    plotar_resultados(resultados_c3, "Cenário 3: Centro de Saúde")
    
    # Comparação entre cenários
    print("\n" + "="*60)
    print("GERANDO COMPARAÇÃO ENTRE CENÁRIOS")
    print("="*60)
    
    comparar_cenarios({
        'Cenário 1': resultados_c1,
        'Cenário 2': resultados_c2,
        'Cenário 3': resultados_c3
    })
    
    print("="*100)
    print("SIMULAÇÕES CONCLUÍDAS COM SUCESSO!")
    print("="*100)
#endregion