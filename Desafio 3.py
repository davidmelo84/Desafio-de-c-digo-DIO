import sys

# Lista de dicionários representando os três modelos do Amazon Bedrock
modelos_disponiveis = [
    {"nome": "Claude 3 Opus", "pontuacao_desempenho": 9, "preco_mensal": 600},
    {"nome": "Claude 3 Sonnet", "pontuacao_desempenho": 8, "preco_mensal": 450},
    {"nome": "Claude 3 Haiku", "pontuacao_desempenho": 7, "preco_mensal": 350},
]

# Função para recomendar o modelo com base no orçamento
def recomendar_modelo(modelos, orcamento):
    # Verificar se o orçamento é inferior a 250
    if orcamento < 250:
        return None, "Seu orçamento é muito baixo para recomendar um modelo adequado."

    # Filtrar os modelos que estão dentro do orçamento
    modelos_dentro_orcamento = [modelo for modelo in modelos if modelo['preco_mensal'] <= orcamento]

    # Caso nenhum modelo esteja dentro do orçamento, retornar o mais próximo
    if not modelos_dentro_orcamento:
        modelo_mais_proximo = min(modelos, key=lambda x: abs(x['preco_mensal'] - orcamento))
        return modelo_mais_proximo['nome'], "Este modelo está mais próximo do seu orçamento."

    # Encontrar o modelo com o melhor desempenho dentro do orçamento
    melhor_modelo = max(modelos_dentro_orcamento, key=lambda x: x['pontuacao_desempenho'])
    return melhor_modelo['nome'], "Melhor desempenho dentro do seu orçamento."

# Solicitar orçamento do usuário
orcamento_usuario = float(sys.stdin.read().strip())

# Chamada da função para recomendar o modelo
modelo_recomendado, motivo = recomendar_modelo(modelos_disponiveis, orcamento_usuario)

# Saída da recomendação
if modelo_recomendado:
    sys.stdout.write(modelo_recomendado + ". " + motivo + "\n")
else:
    sys.stdout.write(motivo + "\n")
