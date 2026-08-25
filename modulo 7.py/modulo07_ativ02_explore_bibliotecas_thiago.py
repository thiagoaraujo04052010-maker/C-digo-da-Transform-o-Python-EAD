'''
Programador: as variaveis, serão inseridas no app - BACK-End

Dev: existe a interação com o usuario - Web Design (Front-End)

'''
import utilidades

import datetime
from faker import Faker


fake = Faker('pt_BR')


print('***Dados Criados - Prova de Matemática ***')
print(f'Nome de Mentira: {fake.name()}')
print(f'E-mail de mentira: {fake.email()}')
print(f'Numero de Mentira: {fake.cellphone_number()} ')


print(f'Dados da Prova de Mentira ***')
agora = datetime.datetime.now()
print(f'Sua Prova foi concluida: {agora.strftime('%H:%M %d/%m/%y')}')


num1 = 10
num2 = 5

print('⚙ 🧱Teste de Utilidades ⚙ 🧱')
print(f'Números utilizados: {num1} e {num2}')


print(f' Usando Adição ({num1} + {num2}) :', utilidades.soma(num1, num2))



print(f' Usando Subtração ({num1} - {num2}) :', utilidades.subtrair(num1, num2))



print(f' Usando Multiplicação ({num1} * {num2}) :', utilidades.multiplicar(num1, num2))



print(f' Usando Divisão  ({num1} / {num2}) :', utilidades.dividir(num1, num2))



print(f' Usando Divisão Inteira  ({num1} // {num2}) :', utilidades.divisao_inteira(num1, num2))



print(f' Usando Resto da Divisão  ({num1} % {num2}) :', utilidades.resto_divisao(num1, num2))



print(f' Usando Potenciação  ({num1} ^ {num2}) :', utilidades.potencia(num1, num2))



print("\n=== TESTE DE SEGURANÇA (DIVISÃO POR ZERO) ===")
print(f' Usando Divisão por Zero', utilidades.dividir(10, 0))