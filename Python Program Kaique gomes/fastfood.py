print('1. Hamburguer - R$ 10,00')
print('2. Batata frita - R$ 5,00')
print('3. Refrigerante - R$ 4,00')
print('4. Sorvete - R$ 2,00')

opcao = int(input('Digite a opção: '))
quantidade = int(input('Digite a quantidade: '))
nome = str(input('Digite o nome do cliente: '))

if opcao == 1:
    print('Hamburguer sendo preparado para', nome)
    print('Tempo de espera de 15 minutos')
    total = quantidade * 10
    print('Total: R$', total)
    
if opcao == 2:
    print('Batata frita sendo preparada para', nome)
    print('Tempo de espera de 10 minutos')
    total = quantidade * 5
    print('Total R$', total)

if opcao == 3:
    print('Refrigerante sendo preparado para', nome)
    print('Tempo de espera de 2 minutos')
    total = quantidade * 4
    print('Total R$', total)

if opcao == 4:
    print('Sorvete sendo preparado para', nome)
    print('Tempo de espera de 5 minutos')
    total = quantidade * 2
    print('Total R$', total)