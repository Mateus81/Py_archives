class Main():
    def main():
        while True:
            peso: float = float(input('Informe o peso (kg): '))
            altura: float = float(input('Informe a altura (m): '))
            imc: float = peso / (altura * altura)

            if imc < 18.5:
                print('Resultado: Magreza')
                print('Grau: 0')

            elif 18.5 <= imc <= 24.9:
                print('Resultado: Normal')
                print('Grau: 0')

            elif 25.0 <= imc <= 29.9:
                print('Resultado: Sobrepeso')
                print('Grau: 1')

            elif 30.0 <= imc <= 39.9:
                print('Resultado: Obesidade')
                print('Grau: 2')

            elif imc >= 40:
                print('Resultado: Obesidade Grave')
                print('Grau: 1')


Main.main()
