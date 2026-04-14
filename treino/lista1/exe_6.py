# Fórmula da Área do círculo: A = pi * raio²
# Fórmula do Perímetro (circunferência) do círculo: P = 2 * pi * raio


pi = 3.141592

try:

    raio = float(input("Digite o valor do circulo: "))

    perimetro =2 * pi * raio

    print(f"""

            A formula para calcular o perimetro do circulo é: 2 * pi * raio

            O perimetro do circulo é: {perimetro}
    
    """)

except ValueError:
    print("Por favor, digite um valor válido.")
