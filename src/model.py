from src.generators import pert, normal


def terreno_laje_acabamento_interno (pert_min, per_moda, pert_max, log_normal_media, log_normal_desvio, normal_media, normal_desvio):
    duracao = pert(pert_min, per_moda, pert_max)
    custo_material = log_normal()
    custo_mao_obra = normal(normal_media, normal_desvio)

    duracao_total = duracao
    custo_total = custo_mao_obra + custo_material

    return duracao_total, custo_total
