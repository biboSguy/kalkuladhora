def calculadora():
    print("Calculadora legal 2023 atualizada")
    while True:
        try:

            def soma(a, b):
                return a + b

            def subtrai(a, b):
                return a - b

            def multiplicação(a, b):
                return a * b

            def divide(a, b):
                if b != 0:
                    return a / b
                else:
                    return "Erro: Divisão por zero"
                
            def potenciação(a, b):
                return a ** b

            def radiciacao(a, b):
                return a ** (1 / b)




            print ("calculadora V2")
            num1 = float(input("escolha primeiro numero:"))
            print (num1)

            print ('''
somar = 1
subtração = 2
multiplicação = 3
divisão = 4
potenciação = 5
radiciação = 6
''')

            oper = float(input("escolha a operação:"))

            if oper in [1, 2, 3, 4, 5, 6]:
                num2 = float(input("escolha o segundo numero:"))


            if oper == 1:
                    resultado = soma(num1, num2)
                    print("a soma é:",resultado,"")
            elif oper ==2:
                resultado = subtrai(num1, num2)
                print("a subtração é:",resultado,"")
            elif oper ==3:
                resultado = multiplicação(num1, num2)
                print("a multiplicação é:",resultado,"")
            elif oper ==4:
                resultado = divide(num1, num2)
                print("a divisão é:",resultado,"")
            elif oper ==5:
                resultado = potenciação(num1, num2)
                print("a pontecia é:",resultado,"")
            elif oper ==6:
                resultado = radiciacao(num1, num2)
                print("a radiciação é:",resultado,"")

            else:
                print("operação invalida, tente novamente")

        except ValueError:
            print("Por favor, digite números válidos.")
calculadora()
