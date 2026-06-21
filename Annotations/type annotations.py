def calculate(a: int, b: int) -> int:
    return a + b


def greet(name: str) -> str:
    return f"Hello, {name}"


def is_adult(age: int) -> bool:
    return age >= 18


def divide(num1: float, num2:float) -> float:
    return num1 / num2


# when function does not reeturn ant thing use "None"

def cal_maximum(a: int, b: int, c: int) -> None:
    print(f"Maximum of a, b, c is {max(a,b,c)}")

cal_maximum(5, 8, 11)


#list as input
def max_marks(marks: list[int]) -> int:
    return max(marks)


# list can contains both int and str
def print_list(lst: list[int | str]):
    print(lst)