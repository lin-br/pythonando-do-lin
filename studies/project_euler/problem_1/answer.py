from functools import reduce

"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""
if __name__ == '__main__':
    total = [number for number in range(1000) if (number % 3) == 0 or (number % 5) == 0]
    print(reduce(lambda x, y: x + y, total))
