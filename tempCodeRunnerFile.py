import math

def f(x: float) -> float:
    return 5 * math.sin(x) - x + 0.5

def f_prime(x: float) -> float:
    return 5 * math.cos(x) - 1

def phi_convergent(x: float, lambda_val: float) -> float:
    return x + lambda_val * f(x)

def get_user_input():
    while True:
        try:
            a_str = input("Введіть початок інтервалу a: ")
            b_str = input("Введіть кінець інтервалу b: ")
            eps_str = input("Введіть бажану точність ε: ")
            
            a = float(a_str)
            b = float(b_str)
            epsilon = float(eps_str)

            if a >= b:
                print("ПОМИЛКА: Початок інтервалу 'a' має бути меншим за кінець 'b'. Спробуйте ще раз.\n")
                continue
            
            if epsilon <= 0:
                print("ПОМИЛКА: Точність ε має бути додатним числом. Спробуйте ще раз.\n")
                continue

            if f(a) * f(b) >= 0:
                print(f"ПОМИЛКА: На інтервалі [{a}, {b}] немає гарантованого кореня. Оберіть інший інтервал.\n")
                continue
            
            return a, b, epsilon

        except ValueError:
            print("ПОМИЛКА: Введено не число. Будь ласка, вводьте тільки числа. Спробуйте ще раз.\n")

def simple_iteration_method(x0: float, lambda_val: float, epsilon: float, max_iterations: int = 50):
    x_prev = x0
    print("\nМетод Простої Ітерації")
    print(f"Початкове наближення x0 = {x_prev}")
    print(f"Розрахований параметр λ = {lambda_val:.4f}")

    for i in range(1, max_iterations + 1):
        x_next = phi_convergent(x_prev, lambda_val)
        error = abs(x_next - x_prev)
        print(f"Ітерація {i}: x = {x_next:.6f}, Похибка = {error:.6f}")
        if error < epsilon:
            print(f"Результат знайдено за {i} ітерацій.")
            return x_next
        x_prev = x_next
        
    print("Метод не збігся за максимальну кількість ітерацій.")
    return None

if __name__ == "__main__":
    a, b, epsilon = get_user_input()
    
    f_prime_a = f_prime(a)
    f_prime_b = f_prime(b)
    
    lambda_val = -1 / f_prime_a if abs(f_prime_a) > abs(f_prime_b) else -1 / f_prime_b

    x0_si = a
    
    root_si = simple_iteration_method(x0_si, lambda_val, epsilon)
    
    if root_si is not None:
        print(f"\nЗнайдений корінь: {root_si:.6f}")
        print(f"Перевірка f(корінь): {f(root_si):.6f}")