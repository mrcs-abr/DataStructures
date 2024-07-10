import sys

n = int(input())
rabbitX, rabbitY = map(float, input().split())
foxX, foxY = map(float, input().split())

rabbit_speed = 1
fox_speed = 2
holes = []
    
for _ in range(n):
    holeCord = input().split()
    holeCord = [float(i) for i in holeCord]
    holes.append(holeCord)

for i in range(len(holes)):
    x = holes[i][0]
    y = holes[i][1]
    rab_distance = ((rabbitX - x)**2 + (rabbitY - y)**2)**(1/2)
    fox_distance = ((foxX - x)**2 + (foxY - y)**2)**(1/2)

    rab_time = rab_distance / rabbit_speed
    fox_time = fox_distance / fox_speed

    if rab_time < fox_time:
        print(f"O coelho pode escapar pelo buraco ({x:.3f}, {y:.3f}).")
        sys.exit()

print("O coelho nao pode escapar.")



    






    
    


    

    
