
print('Digite 1 número e aperte enter, faça isso 3 vezes:')
num1 = int(input())

num2 = int(input())
num3 = int(input())

menor: int = num1
maior: int = num2
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
if num1 > num2 and num1 > num3:
    maior = num1
if num3 > num2 and num3 > num1:
    maior = num3

print(f'O menor número é o {menor}')
print(f'O maior número é o {maior}')
