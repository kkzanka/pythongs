# PYTHON-GS
Claro, aqui está o README.md formatado para o GitHub:


# Projeto de Coleta de Plástico nos Oceanos

Este projeto implementa um sistema de coleta de dados e cálculo de impacto ambiental relacionado à poluição por plástico nos oceanos. Ele permite que os usuários insiram dados sobre a quantidade de plástico em diferentes áreas de um oceano específico, calcule a quantidade de plástico coletada, e estime os impactos positivos da coleta, como redução da poluição e vidas marinhas salvas.

## Funcionalidades

### Entrada de Dados:

- O usuário escolhe um oceano e insere a quantidade total de plástico presente.
- Coleta de dados de poluição em diferentes áreas do oceano, com verificação de que a soma dos percentuais não ultrapasse 100%.

### Cálculos:

- Quantidade de plástico coletada por área.
- Total de plástico coletado.
- Redução percentual da poluição.
- Prejuízo econômico evitado pela coleta do plástico.
- Estimativa de vidas marinhas salvas com a coleta.

### Relatório:

- Exibição de um relatório detalhado com todos os dados inseridos e cálculos realizados.

## Estrutura do Código

### Funções

- `input_numero(mensagem)`: Solicita uma entrada do usuário e verifica se é um número válido.
- `coletar_dados_poluição()`: Coleta dados de diferentes áreas do oceano.
- `calcular_coleta(total_plastico, areas)`: Calcula a quantidade de plástico coletada por área.
- `calcular_total_coletado(coleta_por_area)`: Calcula o total de plástico coletado.
- `calcular_reducao(total_plastico, total_coletado)`: Calcula a redução percentual da poluição.
- `calcular_vidas_marinhas_salvas(total_coletado)`: Estima o número de vidas marinhas salvas.
- `exibir_relatorio(total_plastico, coleta_por_area, reducao, prejuizo_economico_evitar, vidas_salvas, percentual_restante)`: Exibe um relatório detalhado dos resultados.

### Fluxo do Programa

- O usuário escolhe um oceano e insere a quantidade total de plástico presente.
- O usuário insere dados de poluição para diferentes áreas.
- O programa verifica se a soma dos percentuais de poluição não ultrapassa 100%.
- O programa calcula a quantidade de plástico coletada, a redução da poluição, o prejuízo econômico evitado e as vidas marinhas salvas.
- Um relatório detalhado é exibido ao usuário.

## Como Executar

- Clone o repositório para sua máquina local:
  ```
  git clone https://github.com/seu-usuario/seu-repositorio.git
  ```
- Navegue até o diretório do projeto:
  ```
  cd seu-repositorio
  ```
- Execute o script:
  ```
  python3 nome_do_script.py
  ```

