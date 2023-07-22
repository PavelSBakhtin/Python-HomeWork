# Создайте функцию генератор чисел Фибоначчи.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield b
        a, b = b, a + b

for i in fibonacci(int(input('Enter Fibo sequence number: '))):
    print(i, end=' ')

# # Бесконечный:
# #
# def fibonacci():
#     a, b = 0, 1
#     while True:
#         yield b
#         a, b = b, a + b

# fibo = fibonacci() # создаёт генератор
# for i in fibo: # вытягиваем по одному значению
#     print(i)
