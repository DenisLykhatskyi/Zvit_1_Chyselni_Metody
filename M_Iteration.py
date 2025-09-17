import math

def f(x: float) -> float:
    return 5 * math.sin(x) - x + 0.5

def phi_convergent(x: float, lambda_val: float) -> float:
    return x + lambda_val * f(x)

def simple_iteration_method(x0: float, lambda_val: float, epsilon: float, max_iterations: int = 50):
    x_prev = x0
    print("----Метод Простої Ітерації----")
    print(f"Початкове наближення x0 = {x_prev}")
    print(f"Параметр λ = {lambda_val}")

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
    EPSILON = 0.001
    A = 2.5
    LAMBDA = 0.181
    x0_si = A
    
    root_si = simple_iteration_method(x0_si, LAMBDA, EPSILON)
    
    if root_si is not None:
        print(f"Знайдений корінь: {root_si:.6f}")
        print(f"Перевірка f(корінь): {f(root_si):.6f}")