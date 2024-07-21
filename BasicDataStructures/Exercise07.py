from Implementations.stack import Stack

number_of_clothes = int(input())
stack_of_clothes = Stack()
total_time = 0

for _ in range(number_of_clothes):
    type_of_clothing, color, time = input().split()
    time = int(time)
    total_time += time
    clothes = {"Type": type_of_clothing, "Color": color, "Time": time}
    stack_of_clothes.push(clothes)

for _ in range(stack_of_clothes.size()):
    item = stack_of_clothes.pop()
    print(f"Tipo: {item['Type']}, Cor: {item['Color']}")

print(f"Total de roupas: {number_of_clothes}")
print(f"Total de tempo: {total_time}")




