from Implementations.queue1 import Queue

names = input().split()
n_moves = int(input())
q1 = Queue()

for name in names:
    q1.enqueue(name)

for _ in range(n_moves):
    q1.enqueue(q1.dequeue())

print(f"Pessoa da frente: {q1.peek()}")
print(f"Pessoa do fim: {q1.items[-1]}")



