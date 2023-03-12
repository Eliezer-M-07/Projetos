from random import choice

numbers = []

for i in range(1,10000+1):
    numbers.append(i)

n = choice(numbers)

print('\nOlá seja bem-vindo(a)! tente descobrir o número que o computador escolher.\n')

while True:

    try:
        un = int(input('Informe o número -> '))
        
        if un == n:
            print('\nParabéns! Você acertou. O número era {} \n'.format(n))
            break   
        elif un > n:
            print('\nO número digitado é maior.\n')
            continue
        else:
            print('\nO número digitado é menor.\n')
            continue
        
    except ValueError:
        print('\nInforme um nûmero.\n')
        
        





