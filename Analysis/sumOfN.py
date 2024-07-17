import time

def sum_of_n(n):
    start = time.time()

    the_sum = 0

    for i in range(1, n+1):
        the_sum = the_sum + i

    end = time.time()

    return the_sum, end - start

def sum_of_gauss(n):
    start = time.time()
    
    res = (n * (n + 1) / 2)
    
    end = time.time()
    return res, end - start

print("-----> O(n) version <-----")    

for i in range(5):
    print("Sum is %d required %10.7f seconds"%sum_of_n(100000))

print("-----> O(1) version <-----")

for i in range(5):
    print("Sum is %d required %10.7f seconds"%sum_of_gauss(100000))


