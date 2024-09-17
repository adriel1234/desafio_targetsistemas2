# Valores de faturamento por estado

def iniciar_dicionario():
    faturamento_estados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
    }

    return faturamento_estados


def total_faturamento(dicionario):
    faturamento_total = sum(dicionario.values())
    return faturamento_total

def main():   
    percentuais = {}
    faturamento_estados = iniciar_dicionario()
    faturamento_total = total_faturamento(faturamento_estados) 
    print(faturamento_estados)
    for estado, faturamento in faturamento_estados.items():
        percentuais[estado] = (faturamento / faturamento_total) * 100
        print(f"{estado}: {percentuais[estado]:.2f}%")



if __name__ == "__main__":
    main()

