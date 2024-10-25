import os
print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3.Ativar restaurante')
print('4. Sair/n')

opcao_escolhida = int(input('Escolha uma opção: '))
print ('Você escolheu a opção', opcao_escolhida)
# print(type(opcao_escolhida))
# print(type(1))
 # opcao_escolhida = int(opcao_escolhida) a partir da variável colocar  como inteiro!
 
os.system('cls')
def finalizar_app():
  # os.system('clear') no mac
    print('Finalizar o app\n')
   
if opcao_escolhida == 1:
    print('Cadastrar restaurantes\n')
elif opcao_escolhida == 2:
    print('Listar restaurantes\n')
elif opcao_escolhida == 3:
    print('Ativar restaurante\n')
else:
    finalizar_app
    print('Finalizar o app\n')
   