print('Bem vindo ao cálculo de Índice de Massa Corporal(IMC).')
while True:
    p = input('Digite o seu peso em Kg: ')
    h = input('Digite a sua altura em centímetros: ')
    if p.isnumeric() and h.isnumeric():
        p = float(p)
        h = float(h)
        h = (h / 100)
        imc = (p / h ** 2)
        if imc < 18.5:
            print('Você está abaixo do peso. O seu IMC vale {:.1f}'.format(imc))
            break
        elif 18.5 <= imc < 25:
            print('Você está no peso ideal. O seu IMC vale {:.1f}'.format(imc))
            break
        elif 25 <= imc < 30:
            print('Você está na faixa de sobrepeso. O seu IMC vale {:.1f}'.format(imc))
            break
        elif 30 <= imc < 40:
            print('Você está na faixa de obesidade. O seu IMC vale {:.1f}'.format(imc))
            break
        elif imc >= 40:
            print('Voce está na faixa de obesidade mórbida. O seu IMC vale {:.1f}'.format(imc))
            break
