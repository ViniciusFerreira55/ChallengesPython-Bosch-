import math
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))
delta = (b*b)-4*a*c
x1 = (-b + math.sqrt(delta))/(2*a)
x2 = (-b - math.sqrt(delta))/(2*a)
print(f"{a:.0f}x^2 {b:.0f}x{c:.0f} = 0")
print("O valor de delta:",delta)
print(f"O valor de x1 é {x1:.2f}, e o de x2 é {x2:.2f}")


