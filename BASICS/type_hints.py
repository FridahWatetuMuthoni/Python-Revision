"""
download => pip install mypy
mypy => used to check the type hints
"""

def meow(n: int) -> None:
    """ 
    Meow n times.
    :param n : Number of times to meow
    :type n : int
    :raise TypeError: if n is not an int
    :return : None
    """
    for _ in range(n):
        print("meow")

number: int = int(input("Enter a number: "))
meow(number)

numbers = [100, 50, 2]
nums = [*numbers]
print(nums)

for index, value in enumerate(numbers):
    print(f"Index: {index}, Value: {value}")