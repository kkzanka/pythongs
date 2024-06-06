def input_numero(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isnumeric():
            return int(entrada)
        else:
            print("Por favor, insira um número válido.")


def coletar_dados_poluição():

    areas = []
    while True:
        nome = input("Digite o nome da área (ou 'sair' para finalizar): ")
        if nome == 'sair':
            break
        percentual_str = input(f"Digite o percentual de poluição na área {nome}: ")
        percentual = input_numero(f"Digite o percentual de poluição na área {nome}: ")
        areas.append({'nome': nome, 'percentual': percentual})
    return areas


def calcular_coleta(total_plastico, areas):

    coleta_por_area = []
    for area in areas:
        coletado = total_plastico * area['percentual'] / 100
        coleta_por_area.append({'nome': area['nome'], 'coletado': coletado})
    return coleta_por_area

def calcular_total_coletado(coleta_por_area):
 
    total_coletado = 0
    for area in coleta_por_area:
        total_coletado += area['coletado']
    return total_coletado

def calcular_reducao(total_plastico, total_coletado):

    reducao = (total_coletado / total_plastico) * 100
    return reducao

def calcular_vidas_marinhas_salvas(total_coletado):

    vidas_salvas_por_tonelada = 10  # Estimativa fictícia de vidas marinhas salvas por tonelada de plástico coletado
    vidas_salvas = int(total_coletado * vidas_salvas_por_tonelada)
    return vidas_salvas

def exibir_relatorio(total_plastico, coleta_por_area, reducao, prejuizo_economico_evitar, vidas_salvas):


    print("\n--- Relatório da Coleta de Plástico ---")
    print(f"Total de plástico no oceano: {total_plastico} toneladas")
    for area in coleta_por_area:
        print(f"Na área {area['nome']}, coletamos {area['coletado']:.2f} toneladas de plástico.")
    total_coletado = calcular_total_coletado(coleta_por_area)
    print(f"Total de plástico coletado: {total_coletado:.2f} toneladas")
    print(f"Redução da poluição: {reducao:.2f}%")
    print(f"Prejuízo econômico evitado: {prejuizo_economico_evitar:.2f}")
    print(f"Vidas marinhas salvas: {vidas_salvas}")

# Entrada de dados pelo usuário
oceanos = ["Atlântico", "Pacífico", "Índico", "Ártico", "Antártico", "Sul", "Norte"]
print("Escolha um dos oceanos:")
for i, oceano in enumerate(oceanos):
    print(f"{i + 1}. {oceano}")

oceano_escolhido = input_numero("Digite o número correspondente ao oceano: ")
while oceano_escolhido not in range(1, len(oceanos) + 1):
    print("Por favor, insira um número válido.")
    oceano_escolhido = input_numero("Digite o número correspondente ao oceano: ")

total_plastico = input_numero("Digite a quantidade total de plástico no oceano (em toneladas): ")


# Coletar dados de poluição em diferentes áreas
areas = coletar_dados_poluição()

# Adição de uma nova área
areas.append({'nome': 'Nova Área', 'percentual': 20})

# Remoção da primeira área
areas.pop(0)

# Concatenação de duas listas de áreas
outras_areas = [{'nome': 'Área X', 'percentual': 30}, {'nome': 'Área Y', 'percentual': 40}]
areas.extend(outras_areas)

# Iteração sobre os elementos das áreas
print("\n--- Lista de Áreas ---")
for area in areas:
    print(f"{area['nome']}: {area['percentual']}%")

# Calcular a quantidade de plástico coletado e a redução da poluição
coleta_por_area = calcular_coleta(total_plastico, areas)
total_coletado = calcular_total_coletado(coleta_por_area)
reducao = calcular_reducao(total_plastico, total_coletado)

# Estimativa de impacto econômico
custo_limpeza_por_tonelada = 100  # valor fictício de custo de limpeza por tonelada
prejuizo_economico_evitar = total_coletado * custo_limpeza_por_tonelada

# Calcular vidas marinhas salvas
vidas_salvas = calcular_vidas_marinhas_salvas(total_coletado)

# Exibir relatório
exibir_relatorio(total_plastico, coleta_por_area, reducao, prejuizo_economico_evitar, vidas_salvas)
