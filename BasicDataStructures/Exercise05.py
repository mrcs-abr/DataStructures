from Implementations.stack import Stack

weight_plates = Stack()
total_weight_moved = 0
plates_removed = 0
current_plate = 0

while 1:
    item = int(input())
    if item == 0:
        break
    
    weight_plates.push(item)

if not weight_plates.isEmpty():
    plate_requested = int(input())

    while 1:
        current_plate = weight_plates.pop()
        total_weight_moved += current_plate
        plates_removed += 1

        print(f"Peso retirado: {current_plate}")
        
        if current_plate == plate_requested:
            break
else:
    print(f"Peso retirado: {current_plate}")

print(f"Anilhas retiradas: {plates_removed}")
print(f"Peso total movimentado: {total_weight_moved}")













