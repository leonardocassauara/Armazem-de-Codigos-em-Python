number = int(input('Digite um número entre 0 e 20: '))
number_extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
while number not in range(0, 21):
    number = int(input('Tente novamente. Digite um número entre 0 e 20: '))
print(f'Você digitou o número {number_extenso[number]}')
