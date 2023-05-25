from calculator import Calculator


def main():
    print("Calculadora v.1")
    print("Digite qual operação quer realizar: ")
    print()
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

    tipo_operacao = int(input())

    a = float(input("Digite o primeiro numero: "))
    b = float(input("Digite o segundo numero: "))

    calculadora = Calculator(a, b)

    operacoes = {
        1: calculadora.sum,
        2: calculadora.subtract,
        3: calculadora.multiplication,
        4: calculadora.divider
    }

    if tipo_operacao in operacoes:
        resultado = operacoes[tipo_operacao]()
        print(resultado)
    else:
        print("Operação Inválida.")


if __name__ == '__main__':
    main()
