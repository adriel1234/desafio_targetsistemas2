def inverter_string(texto):
    invertida = ""
    
    for i in range(len(texto) - 1, -1, -1):
        invertida += texto[i]
    
    return invertida

def main():
    texto = input("Informe a string a ser invertida: ")
    
    texto_invertido = inverter_string(texto)
    
    print(f"String invertida: {texto_invertido}")

if __name__ == "__main__":
    main()
