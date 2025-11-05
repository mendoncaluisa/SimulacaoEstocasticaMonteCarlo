from src.generators import pert, normal, bernoulli


def terreno_laje_acabamento_interno (pert_min, per_moda, pert_max, log_normal_media, log_normal_desvio, normal_media, normal_desvio):
    duracao = pert(pert_min, per_moda, pert_max)
    custo_material = log_normal()
    custo_mao_obra = normal(normal_media, normal_desvio)

    duracao_total = duracao
    custo_total = custo_mao_obra + custo_material

    return duracao_total, custo_total

def pintura_externa(taxa_empresa_tercerizada, taxa_condicao_climatica,
                    empresa_a_log_normal, empresa_a_normal, empresa_a_pert_tempo_bom, empresa_a_pert_tempo_ruim,
                    empresa_b_log_normal, empresa_b_normal, empresa_b_pert_tempo_bom, empresa_b_pert_tempo_ruim):
    escolha_tercerizada = bernoulli(taxa_empresa_tercerizada)
    condicao_climatica = bernoulli(taxa_condicao_climatica)

    if escolha_tercerizada == 1:
        custo_material = log_normal(empresa_a_log_normal)
        mao_obra = normal(empresa_a_normal)
        if condicao_climatica == 1:
            duracao = pert(empresa_a_pert_tempo_ruim)
        else:
            duracao = pert(empresa_a_pert_tempo_bom)

    else:
        custo_material = normal(empresa_b_log_normal)
        mao_obra = normal(empresa_b_normal)
        if condicao_climatica == 1:
            duracao = pert(empresa_b_pert_tempo_ruim)
        else:
            duracao = pert(empresa_b_pert_tempo_bom)

    duracao_total = duracao
    custo_total = custo_material + mao_obra
    return duracao_total, custo_total