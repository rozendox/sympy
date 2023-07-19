from sympy import symbols, Matrix

# Definindo as variáveis simbólicas para os componentes dos vetores
x, y, z = symbols('x y z')

# Função para criar um vetor com componentes x, y e z
def criar_vetor(x, y, z):
    return Matrix([x, y, z])

# Função para realizar a soma de dois vetores
def soma_vetores(vetor1, vetor2):
    return vetor1 + vetor2

# Função para realizar a subtração de dois vetores
def subtrair_vetores(vetor1, vetor2):
    return vetor1 - vetor2

# Função para calcular o produto escalar de dois vetores
def produto_escalar(vetor1, vetor2):
    return vetor1.dot(vetor2)

# Função para calcular o produto vetorial de dois vetores
def produto_vetorial(vetor1, vetor2):
    return vetor1.cross(vetor2)

# Exemplo de uso do script
if __name__ == "__main__":
    vetor_a = criar_vetor(1, 2, 3)
    vetor_b = criar_vetor(4, 5, 6)

    print("Vetor A:", vetor_a)
    print("Vetor B:", vetor_b)

    soma_resultado = soma_vetores(vetor_a, vetor_b)
    print("Soma:", soma_resultado)

    subtracao_resultado = subtrair_vetores(vetor_a, vetor_b)
    print("Subtração:", subtracao_resultado)

    produto_escalar_resultado = produto_escalar(vetor_a, vetor_b)
    print("Produto Escalar:", produto_escalar_resultado)

    produto_vetorial_resultado = produto_vetorial(vetor_a, vetor_b)
    print("Produto Vetorial:", produto_vetorial_resultado)
