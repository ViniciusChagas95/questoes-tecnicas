
# 1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
# Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
# Imprimir(SOMA);
# Ao final do processamento, qual será o valor da variável SOMA?

# Resposta: 91

'''
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K

print(SOMA)
'''

# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

'''
def is_fibonacci(number):
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    return b == number or number == 0

number = int(input("Insira um número: "))
if is_fibonacci(number):
    print(f"{number} Pertence a sequência Fibonacci.")
else:
    print(f"{number} Não pertence a sequência Fibonacci.")
'''

# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;



'''
import json

# Carregar dados do faturamento de um arquivo JSON
with open('faturamento.json', 'r') as file:
    data = json.load(file)

faturamentos = [dia['valor'] for dia in data if dia['valor'] > 0]

menor = min(faturamentos)
maior = max(faturamentos)
media = sum(faturamentos) / len(faturamentos)
dias_acima_da_media = sum(1 for valor in faturamentos if valor > media)

print(f"Menor Faturamento: {menor}")
print(f"Maior Faturamento: {maior}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")

'''

# 4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
# • SP – R$67.836,43
# • RJ – R$36.678,66
# • MG – R$29.229,88
# • ES – R$27.165,48
# • Outros – R$19.849,53

# Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  


'''
faturamento = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

total = sum(faturamento.values())
percentuais = {estado: (valor / total) * 100 for estado, valor in faturamento.items()}

for estado, percentual in percentuais.items():
    print(f"{estado}: {percentual:.2f}%")

'''



# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

'''
def reverse_string(s):
    reversed_str = ""  # String vazia para armazenar o resultado
    for char in s:  # Itera sobre cada caractere na string original
        reversed_str = char + reversed_str  # Adiciona o caractere atual ao início da nova string
    return reversed_str  # Retorna a string invertida

string = input("Enter a string: ")
print(f"Reversed string: {reverse_string(string)}")
'''