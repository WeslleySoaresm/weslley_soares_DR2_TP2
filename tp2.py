# --------------------------------------------------------------------------
#                          PONTO DE PARTIDA DO PROGRAMA
# ---------------------------------------------------------------------------
#        PROJETO: Módulo Preliminar de Classificação de Fraude Bancária
#        AUTOR: Weslley Soares
#        DATA: 31/08/2025
#        DESCRIÇÃO: Este script analisa transações bancárias com base no
#                   valor e no tipo, classificando-as como normais ou
#                   suspeitas de acordo com regras pré-definidas.
# ---------------------------------------------------------------------------


 #%%
 # ---- CONFIGURAÇÃO E PARÂMETROS INICIAIS ---

ANO_2_DIGITOS = 94

limete_da_tranferencia = 1000 * ANO_2_DIGITOS


# Solicita o valor da transação e converte para um número inteiro.
# O `try-except` garante que o programa não quebre se o utilizador digitar um texto.
try:
   VALOR_TRANSACAO = int(input("Digite o valor da transação:\n"))
except ValueError:
    print("Erro: Valor inválido. Por favor, insira apenas números.")
    exit() # Encerra o programa se o valor for inválido

#Solicita o tipo de transação
#Converte a entrada para minúsculas para evitar erros de
# sensibilidade a maiúsculas/minúsculas. Agora "Saque", "saque" e "SAQUE"
TIPO_TRANSACAO = input("\nTipo de Transação (Pix, Tranferencia, Saque)").lower()


# ---  LÓGICA DE CLASSIFICAÇÃO E ANÁLISE ---

# Exibe um feedback inicial para o utilizador, confirmando os dados analisados.
print(f"A analisar transação do valor:  {VALOR_TRANSACAO} do tipo '{TIPO_TRANSACAO}', aguarde...")

# Estrutura condicional para aplicar as regras de negócio.
if(VALOR_TRANSACAO > limete_da_tranferencia and TIPO_TRANSACAO == "transferencia"):
    #  Transferências de valor muito alto.
    print("\nALERTA !!! Vericar origem da transferêcia")

elif( TIPO_TRANSACAO == "Saque"):
    #  Qualquer saque requer uma confirmação.
    print("\nAlerta !! Precisa ser APROVADO pelo cliente")

elif (TIPO_TRANSACAO == "Pix"):
    #  Um Pix de valor alto
    print("Alerta !! Pix muito alto verifique com cliente.")

else: 
    # Caso padrão: Se nenhuma das regras de alerta for acionada.
    print("\nTransação normal")

    # --- FIM DO SCRIPT ---

 #%%















# ---------------------------------------------------------------------------
#        PROJETO: Módulo de Avaliação de Elegibilidade para Promoção
#        AUTOR: Weslley Soares
#        DATA: 31/08/2025
#        DESCRIÇÃO: Este script avalia se um funcionário é elegível para
#                   promoção com base em critérios pré-definidos como
#                   tempo de empresa e nota de avaliação de performance.
# ---------------------------------------------------------------------------


# --- 1. DADOS DE ENTRADA DO FUNCIONÁRIO ---

# Critérios de avaliação para um funcionário específico.
# Estes valores seriam normalmente obtidos de uma base de dados ou de um input.
tempo_empresa_anos = 4
nota_avaliacao = 7.5

# Variável definida mas não utilizada na lógica atual. Poderia ser um critério futuro.
carga_horaria = 40


# --- 2. LÓGICA DE AVALIAÇÃO E DECISÃO ---

# Exibe um feedback inicial para o utilizador.
print("------ AVALIAÇÃO DE ELEGIBILIDADE PARA PROMOÇÃO -------")
print(f"A analisar funcionário com {tempo_empresa_anos} anos de empresa e nota {nota_avaliacao}.")

# Estrutura condicional para aplicar as regras de negócio da promoção.
# A regra de negócio: o funcionário precisa de mais de 2 anos E uma nota igual ou superior a 8.0.
if (tempo_empresa_anos > 2 and nota_avaliacao >= 8.0):
    # Este bloco só é executado se AMBAS as condições forem verdadeiras.
    print("\nResultado: Elegível para promoção")
else: 
    # Se uma ou ambas as condições forem falsas, este bloco é executado.
    print("\nResultado: Aguardando próxima avaliação")


# --- FIM DO SCRIPT ---
# %%
















# ---------------------------------------------------------------------------
#        PROJETO: Módulo de Análise de Risco de Entregas
#        AUTOR: Weslley Soares
#        DATA: 31/08/2025
#        DESCRIÇÃO: Este script avalia o risco de atraso de uma entrega
#                   com base na distância, clima e zona.
# ---------------------------------------------------------------------------


# --- 1. DADOS DE ENTRADA DA ENTREGA ---

# Fatores utilizados para a análise de risco.
# Estes valores seriam normalmente obtidos de um sistema ou API.


distancia_km = 350
clima = "chuva"
zona_entrega = "rural"


# --- LÓGICA DE AVALIAÇÃO DE RISCO ---

# Exibe um feedback inicial, confirmando os dados que estão a ser processados.
print(f"A analisar entrega para {distancia_km}km, com clima '{clima}' em zona '{zona_entrega}'")

# Estrutura condicional para aplicar as regras de negócio.
# 'and' é avaliado ANTES de 'or'.
# A condição é verdadeira se (distância > 300 E clima == "chuva") OU (zona_entrega == "rural").
if(distancia_km > 300 and clima == "chuva" or zona_entrega == "rural"):
   # Este bloco é executado se pelo menos uma das condições acima for satisfeita.
    print("Risco alto de atraso")
else:
    # Se nenhuma das condições de risco for satisfeita, a entrega é normal.
    print("Entrega dentro do previsto")


# --- FIM DO SCRIPT ---





#%%



# ---------------------------------------------------------------------------
#        PROJETO: Módulo de Diagnóstico de Alarmes de Máquina Industrial
#        AUTOR: Weslley Soares
#        DATA: 31/08/2025
#        DESCRIÇÃO: Este script simula um sistema de alarme que analisa
#                   um código de falha e uma leitura de temperatura para
#                   determinar a ação corretiva necessária.
# ---------------------------------------------------------------------------


# --- DADOS DE ENTRADA (LEITURA DOS SENSORES) ---

# Leituras atuais dos sensores da máquina.
# Numa aplicação real, estes dados viriam de uma fonte externa.


codigo = "F5"
temperatura = 50
# --- 2. LÓGICA DE DIAGNÓSTICO E DECISÃO ---

# Exibe um feedback inicial para o operador.
print(f"A analisar alarme... Código: {codigo}, Temperatura: {temperatura}°C")


# Inicia a árvore de decisão para diagnosticar a falha com base no código e/ou temperatura.
if(codigo == "F1" and temperatura < 40):
    print("Reiniciar máquina.")
elif(codigo == "F2" and temperatura > 60):
    print("Verificar conexão elétrica e sistema de refrigeração.")
elif(codigo == "F3" and temperatura >= 45 and temperatura < 55):
    print("Ajustar temperatura da esteira")
elif(codigo == "F4"):
    print("Realizar diagnóstico dos sensores ópticos")
else:
    print("Falha não reconhecida pelo sistema de alarme. Acionar engenheiro responsável")



# --- FIM DO SCRIPT ---









# %%
# ---------------------------------------------------------------------------
#        PROJETO: Filtro de Avaliações de Alta Performance
#        AUTOR: Weslley Soares
#        DATA: 31/08/2025
#        DESCRIÇÃO: Este script analisa uma lista de notas de avaliação,
#                   filtra as que estão acima de um determinado limiar (7)
#                   e exibe uma lista numerada dessas notas.
# ---------------------------------------------------------------------------


# ---  DADOS DE ENTRADA ---

# Lista com as notas de avaliação a serem analisadas.
notas_avaliacao = [5, 8, 10, 6, 9, 4]

# Variável inicializada em zero que servirá para contar quantas notas
# cumprem o nosso critério.
contador_notas_altas = 0


# --- PROCESSAMENTO E LÓGICA DE FILTRAGEM ---

print("--- Análise de Avaliações Acima de 7 ---")

# Inicia um laço 'for' para percorrer cada 'nota' na lista 'notas_avaliacao'.
for nota in notas_avaliacao:
    
    # Condição para filtrar apenas as notas que nos interessam.
    # O código dentro deste 'if' só será executado se a nota for maior que 7.
    if nota > 7:
        
       
        # Isto garante que a nossa lista numerada comece em 1, não em 0.
        contador_notas_altas += 1
        
        # Exibe a nota encontrada, precedida pelo número da contagem.
        print(f"{contador_notas_altas}º - Avaliação de alta performance: {nota}")

# ---  RESULTADO FINAL ---

# Após o loop terminar, exibimos a contagem total de notas encontradas.
print(f"\nTotal de avaliações acima de 7: {contador_notas_altas}")

# --- FIM DO SCRIPT ---




# %%


# ---------------------------------------------------------------------------
#        EXERCÍCIO: Gerador de Lista de Comissões
#        AUTOR: Weslley Soares
#        DATA: 31/08/2025
#        DESCRIÇÃO: Este script cria uma lista de valores de comissão
#                   de 0 a 50, com um incremento de 5.
# ---------------------------------------------------------------------------


# ---  GERAÇÃO DA LISTA DE COMISSÕES ---

# Usamos a função range() para gerar a sequência de números:
# - Começa em 0.
# - Para em 51 (para que o 50 seja incluído).
# - Pula de 5 em 5.
sequencia_de_comissoes = range(0, 51, 5)

# Usamos list() para converter o objeto 'range' numa lista real.
lista_de_comissoes = list(sequencia_de_comissoes)


# ---  EXIBIÇÃO DO RESULTADO ---

# Imprime a lista final na tela para verificação.
print("Tabela de comissões gerada:")
print(lista_de_comissoes)

# --- FIM DO SCRIPT ---












# %%



# ---------------------------------------------------------------------------
#        PROJETO: Simulador de Tentativas de Conexão
#        AUTOR: Weslley Soares
#        DATA: 31/08/2025
#        DESCRIÇÃO: Este script simula um processo de conexão que tenta
#                   um número limitado de vezes, parando em caso de
#                   sucesso ou ao atingir o limite.
# ---------------------------------------------------------------------------


# ---  CONFIGURAÇÃO INICIAL ---

# Lista de resultados de conexão simulados (False=falha, True=sucesso).
tentativas_conexao = [False, False, False, True, True]

# Variável para contar o número de tentativas realizadas (começa em 0).
tentativas_realizadas = 0

# O número máximo de tentativas permitidas.
limite_tentativas = 4


# ---  LÓGICA DE TENTATIVA DE CONEXÃO ---

print(f"A iniciar processo de conexão. Limite de {limite_tentativas} tentativas.")

# O loop continua enquanto o número de tentativas for menor que o limite.
while tentativas_realizadas < limite_tentativas:
    
    print(f"\nTentativa nº {tentativas_realizadas + 1}...")

    # Obtém o resultado da conexão para a tentativa atual.
    sucesso_conexao = tentativas_conexao[tentativas_realizadas]

    # Verifica se a conexão foi bem-sucedida.
    if sucesso_conexao == True:
        print("Conexão bem-sucedida!")
        break  # Interrompe o loop imediatamente, pois já conseguimos conectar.
    else:
        print("Falha na conexão.")

    # Incrementa o contador para passar para a próxima tentativa.
    tentativas_realizadas += 1

#  O bloco 'else' de um loop 'while' ou 'for' só é executado
# se o loop terminar NORMALMENTE (ou seja, sem ser interrompido por um 'break').
# É perfeito para saber se esgotámos as tentativas!
else:
    print(f"\nLimite de {limite_tentativas} tentativas atingido. Conexão falhou.")

# --- FIM DO SCRIPT ---










# %%
# ---------------------------------------------------------------------------
#        EXERCÍCIO: Reorganização de Fila de Pedidos
#        AUTOR: Weslley Soares
#        DATA: 31/08/2025
#        DESCRIÇÃO: Este script simula a reorganização de uma fila de
#                   pedidos com base em regras de negócio. Ele demonstra
#                   a manipulação de listas (inserção e substituição)
#                   usando estruturas condicionais.
# ---------------------------------------------------------------------------

print("--- CENÁRIO A: Pedido Urgente ---")

# ---  Definição das Variáveis Iniciais ---
pedidos = ["P123", "P456", "P789"]
pedido_a_substituir = "P456"
prioridade_urgente = True  # A condição principal para este cenário
pedido_urgente = "P999"

print(f"Fila inicial: {pedidos}")

# ---  Lógica de Decisão ---

# Como 'prioridade_urgente' é True, este bloco 'if' será executado.
if prioridade_urgente:
    # O método .insert(0, ...) adiciona um item na primeira posição (índice 0).
    pedidos.insert(0, pedido_urgente)
    print("Ação: Pedido urgente inserido no início da fila.")
else:
    # Este bloco não será executado neste cenário.
    if pedido_a_substituir in pedidos:
        indice = pedidos.index(pedido_a_substituir)
        pedidos[indice] = pedido_urgente
    else:
        print(f"Ação: Pedido {pedido_a_substituir} não encontrado para substituição.")

# --- Resultado Final ---
print(f"Fila final (Cenário A): {pedidos}\n")

#---------------------------------------------------------

print("--- CENÁRIO B: Não Urgente, Pedido Existe ---")

# ---  Definição das Variáveis Iniciais ---
pedidos = ["P123", "P456", "P789"]
pedido_a_substituir = "P456" # Este pedido EXISTE na lista
prioridade_urgente = False # A condição principal para este cenário
pedido_urgente = "P999"

print(f"Fila inicial: {pedidos}")

# ---  Lógica de Decisão ---

# Como 'prioridade_urgente' é False, o bloco 'else' será executado.
if prioridade_urgente:
    pedidos.insert(0, pedido_urgente)
else:
    # Verificamos se o pedido a ser substituído realmente está na lista.
    if pedido_a_substituir in pedidos:
        # Encontramos o índice (posição) do pedido a ser substituído.
        indice = pedidos.index(pedido_a_substituir)
        # Atribuímos o novo valor ('pedido_urgente') a essa posição.
        pedidos[indice] = pedido_urgente
        print(f"Ação: Pedido {pedido_a_substituir} substituído por {pedido_urgente}.")
    else:
        print(f"Ação: Pedido {pedido_a_substituir} não encontrado para substituição.")

# ---  Resultado Final ---
print(f"Fila final (Cenário B): {pedidos}\n")

#-----------------------------------------------------------------

print("--- CENÁRIO C: Não Urgente, Pedido Não Existe ---")

# ---  Definição das Variáveis Iniciais ---
pedidos = ["P123", "P456", "P789"]
pedido_a_substituir = "P000" # Este pedido NÃO EXISTE na lista
prioridade_urgente = False # A condição principal para este cenário
pedido_urgente = "P999"

print(f"Fila inicial: {pedidos}")

# ---  Lógica de Decisão ---

# O bloco 'else' será executado.
if prioridade_urgente:
    pedidos.insert(0, pedido_urgente)
else:
    # A verificação 'pedido_a_substituir in pedidos' dará False.
    if pedido_a_substituir in pedidos:
        indice = pedidos.index(pedido_a_substituir)
        pedidos[indice] = pedido_urgente
    else:
        # O programa entra neste bloco e exibe a mensagem pedida.
        print(f"Ação: Pedido {pedido_a_substituir} não encontrado para substituição. A fila não foi alterada.")

# --- Resultado Final ---
    print(f"Fila final (Cenário C): {pedidos}\n")

# --- FIM DO SCRIPT ---
# %%




# ---------------------------------------------------------------------------
#        PROJETO: Demonstração de Concatenação de Listas de Produtos
#        AUTOR: Weslley Soares
#        DATA: 31/08/2025
#        DESCRIÇÃO: Este script demonstra como combinar (concatenar)
#                   múltiplas listas em Python para formar uma única lista
#                   agregada, representando um estoque total.
# ---------------------------------------------------------------------------


# ---  DEFINIÇÃO DAS LISTAS DE PRODUTOS ---

# Listas representando o estoque de diferentes secções, fornecedores ou caixas.
produtos_a = ["banana", "maçã"]
produtos_b = ["laranja", "pera"]
produtos_c = ["laranja", "banana", "maçã", "romã"]


# ---  ANÁLISE INICIAL DOS ESTOQUES ---

# Usamos a função len() para verificar o número de itens em cada lista individual.
# A f-string (f"...") permite formatar a saída de forma legível.
print("--- Análise dos Estoques Individuais ---")
print(f"Lista (A) tem : {len(produtos_a)} itens" )
print(f"Lista (B) tem : {len(produtos_b)} itens" )
print(f"Lista (C) tem : {len(produtos_c)} itens" )


# ---  COMBINAÇÃO DOS ESTOQUES ---

# O operador '+' quando usado com listas, serve para concatená-las (juntá-las).
# Ele cria uma NOVA lista contendo todos os elementos das listas originais,
# na ordem em que aparecem na operação.
estoque_total = produtos_a + produtos_b + produtos_c


# ---  RESULTADO FINAL ---

print("\n--- Análise do Estoque Consolidado ---")
# Exibe o tamanho total do novo estoque combinado.
print(f"O Estoque Total (combinado) tem: {len(estoque_total)} itens" )

# Exibe a lista completa do estoque, incluindo itens duplicados que
# aparecem nas listas originais (ex: "banana", "maçã", "laranja").
print("Itens no Estoque Total:")
print(estoque_total)

# --- FIM DO SCRIPT ---

# %%


# ---------------------------------------------------------------------------
#        PROJETO: Módulo de Verificação de Boletos Vencidos
#        AUTOR: Weslley Soares
#        DATA: 31/08/2025
#        DESCRIÇÃO: Este script analisa uma lista de datas de vencimento
#                   de boletos e classifica cada um como "vencido",
#                   "vence hoje" ou "dentro do prazo", com base em uma
#                   data atual fixa.
# ---------------------------------------------------------------------------


# --- CONFIGURAÇÃO E DADOS INICIAIS ---

# Define a data de referência para a verificação.
data_atual = "2025-08-12"

# Lista com as datas de vencimento dos boletos a serem analisados.
# Adicionei mais alguns para um teste mais completo.
boletos = [
    "2025-08-05",  # vencido
    "2025-08-12",  # vence hoje
    "2025-08-15",  # ainda válido
    "2025-08-01",  # vencido
    "2025-09-01",  # ainda válido
]

# Inicializa um contador para saber o total de boletos vencidos.
total_vencidos = 0

print(f"--- Relatório de Boletos (Data de Referência: {data_atual}) ---")


# ---  PROCESSAMENTO E CLASSIFICAÇÃO DOS BOLETOS ---

# Usamos um laço 'for' para percorrer cada boleto na lista.
# A função 'enumerate(boletos, start=1)' é uma forma elegante de obter
# tanto o item da lista (a data) quanto um número de ordem (começando em 1).
for numero_boleto, data_vencimento in enumerate(boletos, start=1):

    # Estrutura condicional para comparar a data de vencimento com a data atual.
    if data_vencimento < data_atual:
        situacao = "Vencido"
        # Se o boleto está vencido, incrementamos o nosso contador.
        total_vencidos += 1
    elif data_vencimento == data_atual:
        situacao = "Vence hoje"
    else: # Se não for menor nem igual, só pode ser maior.
        situacao = "Dentro do prazo"

    # Exibe o resultado formatado para cada boleto.
    print(f"Boleto: {numero_boleto} | Vencimento: {data_vencimento} | Situação: {situacao}")


# ---  EXIBIÇÃO DO RESUMO FINAL ---

# Após o loop terminar, exibe a contagem total de boletos vencidos.
print("\n--- Resumo ---")
print(f"Total de boletos vencidos: {total_vencidos}")

# --- FIM DO SCRIPT ---

        
# %%

# ---------------------------------------------------------------------------
#        EXERCÍCIO: Decodificar Mensagem Cifrada (Cifra de César)
#        AUTOR: Weslley Soares
#        DATA: 31/08/2025
#        DESCRIÇÃO: Este script decifra uma mensagem encriptada usando a
#                   Cifra de César com uma chave calculada e regras
#                   específicas de decifragem por palavra.
# ---------------------------------------------------------------------------


# ---  DADOS INICIAIS ---

texto_cifrado = "SbwKrQ eh phokRu q MDydvfulsW"


# ---  CÁLCULO DA CHAVE DE DECIFRAGEM ---

# A chave é o número de vezes que 'D', 'd' e 'W' aparecem.
# Usamos o método .count() para encontrar as ocorrências.
chave = texto_cifrado.count('D') + texto_cifrado.count('d') + texto_cifrado.count('W')

print(f"Analisando texto cifrado: '{texto_cifrado}'")
print(f"Chave de decifragem calculada: {chave}")


# ---  PROCESSO DE DECIFRAGEM ---

mensagem_decifrada = ""
palavra_atual = ""

# Adicionamos um espaço no final do texto cifrado para garantir
# que a última palavra também seja processada dentro do loop.
for caractere in texto_cifrado + " ":
    
    # Se o caractere não for um espaço, continuamos a construir a palavra atual.
    if caractere != " ":
        palavra_atual += caractere
    
    # Se encontrarmos um espaço, significa que terminámos de ler uma palavra.
    # É hora de processá-la.
    else:
        palavra_decifrada = ""
        
        # Regra: Só deciframos palavras com mais de 3 caracteres.
        if len(palavra_atual) > 3:
            # Percorremos cada letra da palavra a ser decifrada.
            for letra in palavra_atual:
                # Obtemos o código numérico da letra (Unicode).
                codigo_letra = ord(letra)
                
                # Deslocamos o código para trás (subtraímos a chave).
                novo_codigo = codigo_letra - chave
                
                # Verificação de "wrap-around" (dar a volta no alfabeto).
                if letra.islower(): # Se a letra for minúscula
                    if novo_codigo < ord('a'):
                        novo_codigo += 26 # Volta ao final do alfabeto minúsculo
                elif letra.isupper(): # Se a letra for maiúscula
                    if novo_codigo < ord('A'):
                        novo_codigo += 26 # Volta ao final do alfabeto maiúsculo
                
                # Convertemos o novo código de volta para uma letra.
                palavra_decifrada += chr(novo_codigo)
        else:
            # Se a palavra tiver 3 ou menos caracteres, mantemo-la como está.
            palavra_decifrada = palavra_atual
        
        # Adicionamos a palavra processada (e um espaço) à nossa mensagem final.
        mensagem_decifrada += palavra_decifrada + " "
        
        # Resetamos a palavra atual para começar a construir a próxima.
        palavra_atual = ""

# Removemos o espaço extra no final da mensagem.
mensagem_decifrada = mensagem_decifrada.strip()


# ---  EXIBIÇÃO DO RESULTADO FINAL ---
print("\n--- Mensagem Decifrada ---")
print(mensagem_decifrada)

# --- FIM DO SCRIPT ---





# %%
# ---------------------------------------------------------------------------
#        EXERCÍCIO: Otimização de Verificação de Sensores
#        AUTOR: Weslley Soares
#        DATA: 01/09/2025
#        DESCRIÇÃO: Este script refatora um código repetitivo para verificar
#                   a temperatura de múltiplos sensores usando uma lista
#                   e um único laço de repetição.
# ---------------------------------------------------------------------------


# ---  DADOS DE ENTRADA CENTRALIZADOS ---

# usamos uma única lista para armazenar as temperaturas.
# Isto torna o código mais limpo e fácil de expandir.
temperaturas_sensores = [28, 31, 27, 35, 29]

# O limite de temperatura é definido uma única vez.
LIMITE_TEMPERATURA = 30


# ---  LÓGICA DE VERIFICAÇÃO OTIMIZADA ---

print(f"--- A verificar sensores (Limite: {LIMITE_TEMPERATURA}°C) ---")

# Usamos um único laço 'for' para percorrer a lista de temperaturas.
# 'enumerate()' nos dá o índice (0, 1, 2...) e o valor de cada item.
for indice, temperatura in enumerate(temperaturas_sensores):
    
    # Usamos uma única estrutura condicional que é aplicada a cada temperatura.
    if temperatura > LIMITE_TEMPERATURA:
        
        # O número do sensor é o 'índice + 1' (para começar a contar do 1).
        # Adicionamos a temperatura lida na mensagem para um alerta mais informativo.
        print(f"ALERTA: Sensor {indice + 1} acima do limite! (Temperatura: {temperatura}°C)")

print("\n--- Verificação concluída. ---")

# --- FIM DO SCRIPT ---
# %%
