import calculadora

def main():
    a = 2
    b = 3
    soma = calculadora.somar(a,b)
    print(f'{a} + {b} = {soma}')
    subtracao = calculadora.subtrair(a,b)
    print(f'{a} - {b} = {subtracao}')
    multiplicacao = calculadora.multiplicar(a,b)
    print(f'{a} * {b} = {multiplicacao}')
    divisao = calculadora.dividir(a,b)
    print(f'{a} / {b} = {divisao}')

main()