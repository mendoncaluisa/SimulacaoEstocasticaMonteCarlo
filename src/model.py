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
def fase_de_alvenaria(dados):

    min, moda,max = dados['pert']
    media_ln, desvio_ln, = dados['log_normal']
    media, desvio, = dados['normal']

    duracao = pert(min,moda,max)
    custo_material = lognormal(media_ln, desvio_ln)
    custo_mao_obra = normal(media, desvio)
    necessidade_retrabalho = bernoulli(dados['p_retrabalho'])

    if necessidade_retrabalho:
        tempo_total_alvenaria = duracao + dados['tempo_retrabalho']
        custo_total_alvenaria = custo_material + custo_mao_obra + dados['custo_retrabalho']
    else:
        tempo_total_alvenaria = duracao
        custo_total_alvenaria = custo_mao_obra + custo_material

    return  tempo_total_alvenaria,custo_total_alvenaria
#endregion



def pintura_externa(taxa_empresa_tercerizada, taxa_condicao_climatica,
                    empresa_a_log_normal, empresa_a_normal, empresa_a_pert_tempo_bom, empresa_a_pert_tempo_ruim,
                    empresa_b_log_normal, empresa_b_normal, empresa_b_pert_tempo_bom, empresa_b_pert_tempo_ruim):

    escolha_tercerizada = bernoulli(taxa_empresa_tercerizada)
    condicao_climatica = bernoulli(taxa_condicao_climatica)

    if escolha_tercerizada == 1:
        custo_material = lognormal(empresa_a_log_normal[0], empresa_a_log_normal[1])
        mao_obra = normal(empresa_a_normal[0], empresa_a_normal[1])
        if condicao_climatica == 1:
            duracao = pert(empresa_a_pert_tempo_ruim[0], empresa_a_pert_tempo_ruim[1], empresa_a_pert_tempo_ruim[2])
        else:
            duracao = pert(empresa_a_pert_tempo_bom[0], empresa_a_pert_tempo_bom[1], empresa_a_pert_tempo_bom[2])

    else:
        custo_material = normal(empresa_b_log_normal[0], empresa_b_log_normal[1])
        mao_obra = normal(empresa_b_normal[0], empresa_b_normal[1])
        if condicao_climatica == 1:
            duracao = pert(empresa_b_pert_tempo_ruim[0], empresa_b_pert_tempo_ruim[1], empresa_b_pert_tempo_ruim[2])
        else:
            duracao = pert(empresa_b_pert_tempo_bom[0], empresa_b_pert_tempo_bom[1], empresa_b_pert_tempo_bom[2])

    duracao_total = duracao
    custo_total = custo_material + mao_obra
    return duracao_total, custo_total