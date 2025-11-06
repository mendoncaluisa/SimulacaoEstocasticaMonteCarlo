from src.model import terreno_laje_acabamento_interno, fundacao, alvenaria

cenarios = {
    'cenario_1': {

        'fase_1': {
            'pert': [10, 14, 20],
            'log_normal': [120000, 30000],
            'normal':[150000, 35000]
        },

        'fase_2': {
            # probablidade da empresa A ser escolhida
            'p_empresa_A': 0.6,
            # probablidade de ocorrer um evento geologico
            'p_evento_geologico': 0.18,
            # gastos extras caso ocorra um evento geologico
            'tempo_extra': 25,
            'custo_extra': 700000,

            # tempo da empresa A
            'empresa_A': {
                'pert': [30, 40, 55],
                'log_normal': [2700000, 300000],
                'normal':[2300000, 250000]
            },
            
            # tempo da empresa B
            'empresa_B': {
                'pert': [25, 34, 48],
                'log_normal': [3000000, 350000],
                'normal':[2100000, 260000]
            }
        },

        'fase_3': {
            'pert': [0, 100, 130],
            'log_normal': [ 2400000, 300000],
            'normal':[1800000, 200000]
        },
        
        'fase_4': {
            # chance de retrabalho
            'p_retrabalho': 0.12,
            # gastos extras caso ocorra retrabalho
            'tempo_retrabalho': 12,
            'custo_retrabalho': 300000,

            'pert': [0, 75, 95],
            'log_normal': [900000, 120000],
            'normal':[1600000, 200000]
        },
        
        'fase_5': {
            'pert': [0, 110, 150],
            'log_normal': [2500000, 350000],
            'normal':[2500000, 400000]
        },

        'fase_6': {
            # probablidade da empresa A ser escolhida
            'p_empresa_A': 0.6,
            # probablidade do clima estar ruim
            'p_clima_ruim': 0.2,

            # tempo da empresa A
            'empresa_A': {
                'pert_clima_bom': [12, 16, 22],
                'pert_clima_ruim': [16, 20, 28],
                'log_normal': [300000, 50000],
                'normal':[280000, 40000]
            },
            
            # tempo da empresa B
            'empresa_B': {
                'pert_clima_bom': [10, 14, 18],
                'pert_clima_ruim': [14, 18, 24],
                'log_normal': [320000, 60000],
                'normal':[260000, 45000]
            }

        }

    },
    'cenario_2': {

        'fase_1': {
            'pert': [5,7,12],
            'log_normal': [50000,12000],
            'normal': [80000,18000]
        },

        'fase_2': {
            # probablidade da empresa A ser escolhida
            'p_empresa_A': 0.7,
            # probablidade de ocorrer um evento geologico
            'p_evento_geologico': 0.08,
            # gastos extras caso ocorra um evento geologico
            'tempo_extra': 10,
            'custo_extra': 200000,

            # tempo da empresa A
            'empresa_A': {
                'pert': [18,22,30],
                'log_normal': [1200000,180000],
                'normal': [700000,120000]
            },

            # tempo da empresa B
            'empresa_B': {
                'pert': [15,19,25],
                'log_normal': [1300000,200000],
                'normal': [650000,110000]
            }
        },

        'fase_3': {
            'pert': [18,24,32],
            'log_normal': [1000000,150000],
            'normal': [600000,100000]
        },

        'fase_4': {
            # chance de retrabalho
            'p_retrabalho': 0.05,
            # gastos extras caso ocorra retrabalho
            'tempo_retrabalho': 4,
            'custo_retrabalho': 60000,

            'pert': [8,10,14],
            'log_normal': [125000,25000],
            'normal': [160000,30000]
        },

        'fase_5': {
            'pert': [14,18,26],
            'log_normal': [200000,35000],
            'normal': [300000,50000]
        },

        'fase_6': {
            # probablidade da empresa A ser escolhida
            'p_empresa_A': 0.5,
            # probablidade do clima estar ruim
            'p_clima_ruim': 0.3,
            # tempo da empresa A
            'empresa_A': {
                'pert_clima_bom': [6,7,9],
                'pert_clima_ruim': [8,9,12],
                'log_normal': [40000,7000],
                'normal': [50000,8000]
            },
            # tempo da empresa B
            'empresa_B': {
                'pert_clima_bom': [5,7,8],
                'pert_clima_ruim': [7,8,11],
                'log_normal': [45000,8000],
                'normal': [45000,7000]
            }
        }
    },
    'cenario_3': {

        'fase_1': {
            'pert': [8, 12, 18],
            'log_normal': [90000, 20000],
            'normal':[120000, 25000]
        },

        'fase_2': {
            # probablidade da empresa A ser escolhida
            'p_empresa_A': 0.5,
            # probablidade de ocorrer um evento geologico
            'p_evento_geologico': 0.25,
            # gastos extras caso ocorra um evento geologico
            'tempo_extra': 30,
            'custo_extra': 800000,

            # tempo da empresa A
            'empresa_A': {
                'pert': [28, 36, 48],
                'log_normal': [1800000, 220000],
                'normal':[1400000, 180000]
            },
            
            # tempo da empresa B
            'empresa_B': {
                'pert': [25, 32, 44],
                'log_normal': [1900000, 260000],
                'normal':[1350000, 170000]
            }
        },

        'fase_3': {
            'pert': [30, 40, 55],
            'log_normal': [1200000, 170000],
            'normal':[900000, 120000]
        },
        
        'fase_4': {
            # chance de retrabalho
            'p_retrabalho': 0.15,
            # gastos extras caso ocorra retrabalho
            'tempo_retrabalho': 15,
            'custo_retrabalho': 400000,

            'pert': [50, 65, 85],
            'log_normal': [600000, 90000],
            'normal':[1300000, 160000]
        },
        
        'fase_5': {
            'pert': [70, 95, 130],
            'log_normal': [2000000, 300000],
            'normal':[2200000, 300000]
        },

        'fase_6': {
            # probablidade da empresa A ser escolhida
            'p_empresa_A': 0.4,
            # probablidade do clima estar ruim
            'p_clima_ruim': 0.25,

            # tempo da empresa A
            'empresa_A': {
                'pert_clima_bom': [10, 13, 16],
                'pert_clima_ruim': [14, 18, 22],
                'log_normal': [120000, 20000],
                'normal':[100000, 18000]
            },
            
            # tempo da empresa B
            'empresa_B': {
                'pert_clima_bom': [9, 12, 15],
                'pert_clima_ruim': [12, 16, 20],
                'log_normal': [130000, 22000],
                'normal':[95000, 16000]
            }

        }

    }

}

#region Cenário 1
def cenario_1():
    #fase 1
    min, moda, max = cenarios['cenario_1']['fase_1']['pert']
    media_ln, desvio_ln = cenarios['cenario_1']['fase_1']['log_normal']
    media_normal, desvio_normal = cenarios['cenario_1']['fase_1']['normal']
    duracao_terreno, custo_terreno = terreno_laje_acabamento_interno(min, moda, max, media_ln, desvio_ln, media_normal, desvio_normal)

    #fase 2
    tempo_fundacao, custo_fundacao = fundacao(cenarios['cenario_1']['fase_2'])

    #fase 3
    min, moda, max = cenarios['cenario_1']['fase_3']['pert']
    media_ln, desvio_ln = cenarios['cenario_1']['fase_3']['log_normal']
    media_normal, desvio_normal = cenarios['cenario_1']['fase_3']['normal']
    duracao_laje, custo_laje = terreno_laje_acabamento_interno(min, moda, max, media_ln, desvio_ln, media_normal, desvio_normal)

    #fase 4
    tempo_alvenaria, custo_alvenaria = alvenaria(cenarios['cenario_1']['fase_4'])

    #fase 5
    min, moda, max = cenarios['cenario_1']['fase_5']['pert']
    media_ln, desvio_ln = cenarios['cenario_1']['fase_5']['log_normal']
    media_normal, desvio_normal = cenarios['cenario_1']['fase_5']['normal']
    duracao_acabamento_interno, custo_acabamento_interno = terreno_laje_acabamento_interno(min, moda, max, media_ln, desvio_ln, media_normal, desvio_normal)

    #fase 6

#endregion


#region Cenário 2
def cenario_2():
    # fase 1
    min, moda, max = cenarios['cenario_2']['fase_1']['pert']
    media_ln, desvio_ln = cenarios['cenario_2']['fase_1']['log_normal']
    media_normal, desvio_normal = cenarios['cenario_2']['fase_1']['normal']
    duracao_terreno, custo_terreno = terreno_laje_acabamento_interno(min, moda, max, media_ln, desvio_ln, media_normal,desvio_normal)

    # fase 2
    tempo_fundacao, custo_fundacao = fundacao(cenarios['cenario_2']['fase_2'])

    # fase 3
    min, moda, max = cenarios['cenario_2']['fase_3']['pert']
    media_ln, desvio_ln = cenarios['cenario_2']['fase_3']['log_normal']
    media_normal, desvio_normal = cenarios['cenario_2']['fase_3']['normal']
    duracao_laje, custo_laje = terreno_laje_acabamento_interno(min, moda, max, media_ln, desvio_ln, media_normal,desvio_normal)

    # fase 4
    tempo_alvenaria, custo_alvenaria = alvenaria(cenarios['cenario_2']['fase_4'])

    # fase 5
    min, moda, max = cenarios['cenario_2']['fase_5']['pert']
    media_ln, desvio_ln = cenarios['cenario_2']['fase_5']['log_normal']
    media_normal, desvio_normal = cenarios['cenario_2']['fase_5']['normal']
    duracao_acabamento_interno, custo_acabamento_interno = terreno_laje_acabamento_interno(min, moda, max, media_ln,desvio_ln, media_normal,desvio_normal)

    # fase 6
#endregion


#region Cenário 3
def cenario_3():
    # fase 1
    min, moda, max = cenarios['cenario_3']['fase_1']['pert']
    media_ln, desvio_ln = cenarios['cenario_3']['fase_1']['log_normal']
    media_normal, desvio_normal = cenarios['cenario_3']['fase_1']['normal']
    duracao_terreno, custo_terreno = terreno_laje_acabamento_interno(min, moda, max, media_ln, desvio_ln, media_normal,desvio_normal)

    # fase 2
    tempo_fundacao, custo_fundacao = fundacao(cenarios['cenario_3']['fase_2'])

    # fase 3
    min, moda, max = cenarios['cenario_3']['fase_3']['pert']
    media_ln, desvio_ln = cenarios['cenario_3']['fase_3']['log_normal']
    media_normal, desvio_normal = cenarios['cenario_3']['fase_3']['normal']
    duracao_laje, custo_laje = terreno_laje_acabamento_interno(min, moda, max, media_ln, desvio_ln, media_normal,desvio_normal)

    # fase 4
    tempo_alvenaria, custo_alvenaria = alvenaria(cenarios['cenario_3']['fase_4'])

    # fase 5
    min, moda, max = cenarios['cenario_3']['fase_5']['pert']
    media_ln, desvio_ln = cenarios['cenario_3']['fase_5']['log_normal']
    media_normal, desvio_normal = cenarios['cenario_3']['fase_5']['normal']
    duracao_acabamento_interno, custo_acabamento_interno = terreno_laje_acabamento_interno(min, moda, max, media_ln,desvio_ln, media_normal,desvio_normal)

    # fase 6
#endregion
