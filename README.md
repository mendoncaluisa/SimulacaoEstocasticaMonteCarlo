# SimulacaoEstocasticaMonteCarlo
Este trabalho prático envolve a implementação de um modelo de Simulação de Monte Carlo para a Análise Quantitativa de Risco em Projetos de Construção Civil. O objetivo é apoiar a decisão estratégica da construtora de aceitar ou recusar um contrato de construção com preço e prazo fixos.

## O que deve ser feito:
### Desenvolvimento do Modelo de Simulação:
- Implementar Geradores de Números Aleatórios: O grupo deve implementar os geradores de números aleatórios para as distribuições de probabilidade utilizadas no modelo (PERT, LogNormal, Normal e Bernoulli), sem usar bibliotecas prontas.


- Simulação de uma Rodada Completa: Criar um modelo que simule uma rodada completa do projeto, sequencialmente pelas fases (Preparação do Terreno, Fundação, Laje, Alvenaria, Acabamento Interno e Pintura Externa). Esta simulação deve calcular o prazo final e o custo final do projeto.



- Incorporar Incertezas e Riscos: O modelo deve incluir a lógica de cálculo de duração e custos para cada fase, considerando as variáveis aleatórias e os riscos discretos (como risco geológico, risco de retrabalho por inspeção e condição climática).

### Replicação e Análise de Métricas:
- Replicação de Monte Carlo: Replicar o modelo de simulação um número grande (N) de vezes para gerar as distribuições de probabilidade do Custo Total da Obra e da Duração Total da Obra.


- Cálculo de Métricas de Viabilidade: A partir das distribuições geradas, calcular as métricas essenciais para a tomada de decisão:


- Custo Total do Projeto: Soma dos custos de materiais, mão de obra, custos adicionais por riscos e multas por atraso.


- Valor Médio de Multa por Atraso: O valor médio da multa, calculado apenas nos cenários em que o projeto atrasa.


- Probabilidade de Prejuízo (%): A chance do Custo Total ser maior que o Preço Fixo do Contrato.


### Apoio à Tomada de Decisão:
- Análise de Cenários: Utilizar o modelo para avaliar a viabilidade dos três cenários hipotéticos propostos (Edifício Residencial, Galpão Logístico, Centro de Saúde), confrontando os resultados obtidos com os limites de viabilidade definidos pela diretoria para cada cenário.


- Apresentação de Resultados: Gerar gráficos e tabelas para visualizar os resultados das distribuições e métricas.


- Recomendação Final: Fornecer suporte à decisão, recomendando à diretoria financeira se o contrato deve ser aceito ou não, com base na viabilidade (baixa chance de prejuízo e custos de multa aceitáveis). O projeto só deve ser aceito se for viável.


## Estrutura do Repositório GitHub

A organização a seguir visa separar o código-fonte principal, os dados de entrada/saída e a documentação do projeto, facilitando a execução e a manutenção do modelo de Simulação de Monte Carlo.

├── .gitignore 
├── README.md 
├── LICENSE 
├── Relatorio_Viabilidade_Projetos.pdf 
├── src/ 
│ ├── main.py 
│ ├── model.py 
│ ├── generators.py 
│ ├── analysis.py 
│ └── utils.py 
└── data/
  ├── parametros_cenario1.csv 
  ├── parametros_cenario2.csv 
  ├── parametros_cenario3.csv 
  ├── resultados_cenario1.csv (Gerado) 
  └── resultados_... 
└── docs/ 
  └── pratico-simulacao-monte-carlo.pdf

### Descrição dos Componentes

| Arquivo/Pasta | Descrição |
| :--- | :--- |
| **`README.md`** | Apresentação do projeto, instruções de instalação (dependências) e de execução da simulação, e resumo dos resultados. |
| **`Relatorio_Viabilidade_Projetos.pdf`** | Documento final com metodologia, gráficos, tabelas e a recomendação de decisão para a diretoria financeira em cada cenário. |
| **`src/`** | Diretório para o código-fonte principal. |
| **`src/generators.py`** | Implementação manual dos geradores de números aleatórios para as distribuições **Bernoulli, Normal, LogNormal e PERT**. |
| **`src/model.py`** | Contém a lógica de simulação de uma **rodada completa** do processo de construção, implementando os Pseudocódigos e calculando os custos e durações das fases e as multas contratuais. |
| **`src/analysis.py`** | Contém as funções para a **replicação** de Monte Carlo, o cálculo das métricas de viabilidade (Probabilidade de Prejuízo, Multa Média por Atraso) e a geração de visualizações (gráficos/tabelas). |
| **`src/main.py`** | Script principal que carrega os dados, orquestra a execução das simulações para os 3 cenários e salva os resultados. |
| **`data/`** | Diretório para os dados de entrada e saída da simulação. |
| **`parametros_cenario*.csv`** | Arquivos de entrada que armazenam os parâmetros das distribuições para cada cenário (Tabelas 2, 3 e 4). |
| **`resultados_cenario*.csv`** | Arquivos de saída, gerados pelo `main.py`, contendo os resultados de Custo Total e Duração Total para cada replicação. |
| **`docs/`** | Documentação e referência. |
| **`pratico-simulacao-monte-carlo.pdf`** | O enunciado do trabalho. |


## Como Executar
- Clonar o repositório.
- Instalar dependências.

## Informações do Projeto
- Instituição: Instituto Federal Minas Gerais (IFMG) - Campus Formiga.


- Disciplina: Introdução à Simulação.


- Professor: Diego Mello da Silva.


- Grupo/Autores: Luísa Caetano, Maria Luísa Mendonça, Poliana Sousa e Victor Araújo.