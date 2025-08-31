
<div align="center">
  <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original-wordmark.svg" alt="Python Logo" width="200"/>
</div>

# 🐍 Portfólio de Exercícios de Lógica em Python

![Status](https://img.shields.io/badge/status-Concluído-green.svg)
![Python Version](https://img.shields.io/badge/python-3.9+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-lightgrey.svg)

*Uma coleção de scripts desenvolvidos para praticar e demonstrar conceitos fundamentais da programação em Python, desde a manipulação de listas e condicionais até algoritmos de criptografia e refatoração de código.*

---

## 📜 Índice de Projetos

Este repositório contém os seguintes scripts, cada um focado num desafio de lógica específico:

1.  [🏦 **Classificação de Fraude Bancária**](#-classificacao-de-fraude-bancaria)
2.  [👨‍💼 **Avaliação de Elegibilidade para Promoção**](#-avaliacao-de-elegibilidade-para-promocao)
3.  [🚚 **Análise de Risco de Entregas**](#-analise-de-risco-de-entregas)
4.  [🏭 **Diagnóstico de Alarmes de Máquina**](#-diagnostico-de-alarmes-de-maquina)
5.  [📊 **Filtro de Avaliações de Alta Performance**](#-filtro-de-avaliacoes-de-alta-performance)
6.  [💰 **Gerador de Lista de Comissões**](#-gerador-de-lista-de-comissoes)
7.  [📡 **Simulador de Tentativas de Conexão**](#-simulador-de-tentativas-de-conexao)
8.  [📦 **Reorganização de Fila de Pedidos**](#-reorganizacao-de-fila-de-pedidos)
9.  [🍎 **Demonstração de Concatenação de Listas**](#-demonstracao-de-concatenacao-de-listas)
10. [🧾 **Verificação de Boletos Vencidos**](#-verificacao-de-boletos-vencidos)
11. [🔐 **Decodificador de Cifra de César**](#-decodificador-de-cifra-de-cesar)
12. [🌡️ **Otimização de Verificação de Sensores**](#-otimizacao-de-verificacao-de-sensores)

---

## 🚀 Detalhes dos Projetos

### 🏦 Classificação de Fraude Bancária
> **Objetivo:** Analisar transações bancárias e classificá-las como normais ou suspeitas com base em regras de valor e tipo.
* **Conceitos Praticados:** `input()`, conversão de tipos (`int`), manipulação de strings (`.lower()`), estruturas condicionais (`if/elif/else`), operadores lógicos (`and`).

<details>
<summary>Clique para ver o código de exemplo</summary>

```python
limite_da_transferencia = 1000 * ANO_2_DIGITOS
valor_transacao = int(input("Digite o valor da transação:\n"))
tipo_transacao = input("\nTipo de Transação (Pix, Transferencia, Saque)").lower()

if valor_transacao > limite_da_transferencia and tipo_transacao == "transferencia":
    print("\nALERTA!!! Verificar origem da transferência.")
elif tipo_transacao == "saque":
    print("\nAlerta!! Confirmar com o cliente.")
````

\</details\>

### 👨‍💼 Avaliação de Elegibilidade para Promoção

> **Objetivo:** Avaliar se um funcionário é elegível para promoção com base em tempo de empresa e nota de avaliação.

  * **Conceitos Praticados:** Variáveis, operadores lógicos (`and`), condicionais simples.

### 🚚 Análise de Risco de Entregas

> **Objetivo:** Avaliar o risco de atraso de uma entrega com base em distância, clima e zona, demonstrando a precedência de operadores.

  * **Conceitos Praticados:** Precedência de operadores (`and` vs `or`), condicionais complexas.

### 🏭 Diagnóstico de Alarmes de Máquina

> **Objetivo:** Simular um sistema de alarme que analisa um código de falha e uma temperatura para determinar a ação corretiva.

  * **Conceitos Praticados:** `if/elif/else` em cadeia, comparações compostas (`45 <= temperatura < 55`).

### 📊 Filtro de Avaliações de Alta Performance

> **Objetivo:** Analisar uma lista de notas, filtrar as que estão acima de um limiar e exibir uma lista numerada.

  * **Conceitos Praticados:** Laços (`for`), manipulação de listas, uso de um contador manual, condicionais dentro de laços.

### 💰 Gerador de Lista de Comissões

> **Objetivo:** Criar uma lista de valores numéricos com um incremento constante até um teto definido.

  * **Conceitos Praticados:** Função `range(start, stop, step)`, conversão de `range` para `list`.

### 📡 Simulador de Tentativas de Conexão

> **Objetivo:** Simular um processo de conexão que tenta um número limitado de vezes, parando em caso de sucesso ou ao atingir o limite.

  * **Conceitos Praticados:** Laços (`while`), uso do `break`, e a cláusula `else` em laços para tratar falhas.

### 📦 Reorganização de Fila de Pedidos

> **Objetivo:** Simular a reorganização de uma fila de pedidos, demonstrando a inserção e substituição de itens numa lista.

  * **Conceitos Praticados:** Métodos de lista (`.insert()`, `.index()`), atribuição por índice, verificação com `in`.

### 🍎 Demonstração de Concatenação de Listas

> **Objetivo:** Demonstrar como combinar múltiplas listas para formar uma única lista agregada.

  * **Conceitos Praticados:** Concatenação de listas com o operador `+`, função `len()`.

### 🧾 Verificação de Boletos Vencidos

> **Objetivo:** Analisar uma lista de datas de vencimento e classificar cada boleto com base numa data de referência.

  * **Conceitos Praticados:** Comparação de strings (formato AAAA-MM-DD), `enumerate(lista, start=1)`, contadores, `if/elif/else`.

### 🔐 Decodificador de Cifra de César

> **Objetivo:** Decifrar uma mensagem encriptada com regras específicas, incluindo o cálculo da chave e a decifragem condicional por tamanho de palavra.

  * **Conceitos Praticados:** Algoritmos, manipulação de strings sem `split()`, funções `ord()` e `chr()`, lógica de "wrap-around" do alfabeto.

\<details\>
\<summary\>Clique para ver o código de exemplo\</summary\>

```python
chave = texto_cifrado.count('D') + texto_cifrado.count('d') + texto_cifrado.count('W')

if len(palavra_atual) > 3:
    for letra in palavra_atual:
        novo_codigo = ord(letra) - chave
        if letra.islower():
            if novo_codigo < ord('a'): novo_codigo += 26
        elif letra.isupper():
            if novo_codigo < ord('A'): novo_codigo += 26
        palavra_decifrada += chr(novo_codigo)
```

\</details\>

### 🌡️ Otimização de Verificação de Sensores

> **Objetivo:** Refatorar um código repetitivo para verificar a temperatura de múltiplos sensores usando uma única lista e um laço.

  * **Conceitos Praticados:** Refatoração, princípio DRY (Don't Repeat Yourself), `enumerate()`.

-----

## 🛠️ Como Executar os Scripts

Cada exercício está documentado no código-fonte e pode ser executado individualmente.

1.  **Pré-requisitos:**

      * Certifique-se de que tem o **Python 3** instalado.
      * Instale as bibliotecas externas necessárias (usadas em alguns scripts) com o comando:
        ```bash
        pip3 install tabulate
        ```

2.  **Execução:**

      * Copie o código de um exercício para um ficheiro `.py` (ex: `exercicio_fraude.py`).
      * Execute o ficheiro a partir do seu terminal:
        ```bash
        python3 exercicio_fraude.py
        ```

-----

<!-- end list -->

```

---

