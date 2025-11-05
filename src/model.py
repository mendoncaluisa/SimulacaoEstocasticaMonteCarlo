from generators import pert, normal, lognormal, bernoulli


def terreno_laje_acabamento_interno (pert_min, pert_moda, pert_max, log_normal_media, log_normal_desvio, normal_media, normal_desvio):
    duracao = pert(pert_min, pert_moda, pert_max)
    custo_material = lognormal()
    custo_mao_obra = normal(normal_media, normal_desvio)

    duracao_total = duracao
    custo_total = custo_mao_obra + custo_material

    return duracao_total, custo_total


def fundacao(fase):
    # Decide qual empresa vai fzr o trabalho
    empresa_A_escolhida = bernoulli(fase['p_empresa_A'])
    
    # Processo normal
    if empresa_A_escolhida:
        tempo_fundacao = pert(
            fase['empresa_A']['pert'][0], 
            fase['empresa_A']['pert'][1], 
            fase['empresa_A']['pert'][2])
        
        custo_material = lognormal(
            fase['empresa_A']['log_normal'][0], 
            fase['empresa_A']['log_normal'][1])
        
        custo_mao_obra = normal(
            fase['empresa_A']['normal'][0], 
            fase['empresa_A']['normal'][1])
        
    else:
        tempo_fundacao = pert(
            fase['empresa_B']['pert'][0], 
            fase['empresa_B']['pert'][1], 
            fase['empresa_B']['pert'][2])
        
        custo_material = lognormal(
            fase['empresa_B']['log_normal'][0], 
            fase['empresa_B']['log_normal'][1])
        
        custo_mao_obra = normal(
            fase['empresa_B']['normal'][0], 
            fase['empresa_B']['normal'][1])

    # Decide se ocorreu algum evento geologico
    evento_geologico_ocorreu = bernoulli(fase['p_evento_geologico'])

    if evento_geologico_ocorreu:
        tempo_fundacao += fase['tempo_extra']
        custo_fundacao = custo_mao_obra + custo_material + fase['custo_extra']
    else:
        custo_fundacao = custo_mao_obra + custo_material

    return tempo_fundacao, custo_fundacao

    
#region Fase de Alvenaria
def fase_de_alvenaria(dados_alvenaria):

    min, moda,max = dados_alvenaria['pert']
    media_ln, desvio_ln, = dados_alvenaria['log_normal']
    media, desvio, = dados_alvenaria['normal']

    duracao = pert(min,moda,max)
    custo_material = lognormal(media_ln, desvio_ln)
    custo_mao_obra = normal(media, desvio)
    necessidade_retrabalho = bernoulli(dados_alvenaria['p_retrabalho'])

    if necessidade_retrabalho:
        tempo_total_alvenaria = duracao + dados_alvenaria['tempo_retrabalho']
        custo_total_alvenaria = custo_material + custo_mao_obra + dados_alvenaria['custo_retrabalho']
    else:
        tempo_total_alvenaria = duracao
        custo_total_alvenaria = custo_mao_obra + custo_material

    return  tempo_total_alvenaria,custo_total_alvenaria
#endregion


