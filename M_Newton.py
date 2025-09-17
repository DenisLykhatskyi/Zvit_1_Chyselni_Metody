import math

def f(x: float) -> float:
    return 5 * math.sin(x) - x + 0.5

def f_prime(x: float) -> float:
    return 5 * math.cos(x) - 1

def newton_method(x0: float, epsilon: float, max_iterations: int = 50):
    x_prev = x0
    print("----Метод Ньютона----")
    print(f"Початкове наближення x0 = {x_prev}")

    for i in range(1, max_iterations + 1):
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

    print("Метод не збігся за максимальну кількість ітерацій.")
    return None

if __name__ == "__main__":
    EPSILON = 0.001
    B = 2.5
    x0_newton = B 
    
    root_n = newton_method(x0_newton, EPSILON)
    
    if root_n is not None:
        print(f"Знайдений корінь: {root_n:.6f}")
        print(f"Перевірка f(корінь): {f(root_n):.6f}")