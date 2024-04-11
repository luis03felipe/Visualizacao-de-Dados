#Desenvolva uma função para determinar se um numero é primo ou não
number = 7

for i in range(2, number):
    if number % i == 0:
        print(number, "Não é primo")
        break
    else:
        print("Numero primo")    