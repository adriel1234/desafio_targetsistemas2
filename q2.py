def fibonacci_contains(n):
    if n < 0:
        return False
    
    # Início da sequência de Fibonacci
    a, b = 0, 1
    list = []
    # Gera a sequência até que o valor de b seja maior ou igual a n
    while a <= n:
        # print(a," ",b)
        if a == n:
            return True
        a, b = b, a + b
        list.append(a)
    print(list) 
    return False

def main():
    # Solicitar ao usuário que insira um número
    num = int(input("Informe um número: "))
    
    # Verificar se o número pertence à sequência de Fibonacci
    if fibonacci_contains(num):
        print(f"O número {num} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {num} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    main()