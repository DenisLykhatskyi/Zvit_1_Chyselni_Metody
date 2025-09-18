import math

def f(x: float) -> float:
    return 5 * math.sin(x) - x + 0.5

def f_prime(x: float) -> float:
    return 5 * math.cos(x) - 1
    
def f_double_prime(x: float) -> float:
    return -5 * math.sin(x)

def get_user_input():
    while True:
        try:
            a = float(input("Введіть початок інтервалу a: "))
            b = float(input("Введіть кінець інтервалу b: "))
            epsilon = float(input("Введіть бажану точність ε: "))
            
            if a >= b or epsilon <= 0 or f(a) * f(b) >= 0:
                print("ПОМИЛКА: Вхідні дані невірні або на інтервалі немає гарантованого кореня.\n")
                continue
                
            return a, b, epsilon
        except ValueError:
            print("ПОМИЛКА: Введено не число. Спробуйте ще раз.\n")

def newton_method(x0: float, epsilon: float):
    x_prev = x0
    print(f"\nПочаткове наближення x0 = {x_prev}")

    for i in range(1, 51):
        f_val = f(x_prev)
        f_prime_val = f_prime(x_prev)

        if abs(f_prime_val) < 1e-12:
            print("Помилка: похідна близька до нуля.")
            return None
            
        x_next = x_prev - f_val / f_prime_val
        error = abs(x_next - x_prev)
        print(f"Ітерація {i}: x = {x_next:.6f}, Похибка = {error:.6f}")
        
        if error < epsilon:
            print(f"Результат знайдено за {i} ітерацій.")
            return x_next
        x_prev = x_next

    print("Метод не збігся.")
    return None


a, b, epsilon = get_user_input()

x0_newton = a

root_n = newton_method(x0_newton, epsilon)

if root_n is not None:
    print(f"\nЗнайдений корінь: {root_n:.6f}")
    print(f"Перевірка f(корінь): {f(root_n):.6f}")