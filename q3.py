import xml.etree.ElementTree as ET


def carregar_xml(arquivo_xml):
    tree = ET.parse(arquivo_xml)
    return tree.getroot()


def extrair_faturamento(root):
    faturamento_list = []
    for dia in root.findall('Dia'):
        data = dia.get('data')
        faturamento = dia.find('Faturamento')
        if faturamento is not None:
            valor = float(faturamento.find('Valor').text)
            numero_vendas = int(faturamento.find('NumeroVendas').text)
            if valor > 0:
                faturamento_list.append({
                    'data': data,
                    'valor': valor,
                    'numero_vendas': numero_vendas
                })
    return faturamento_list


def calcular_media(faturamento_list):
    soma = sum(f['valor'] for f in faturamento_list)
    cont = len(faturamento_list)
    return soma / cont if cont > 0 else 0


def main():   
    arquivo_xml = 'fonte.xml'
    root = carregar_xml(arquivo_xml)
    faturamento_list = extrair_faturamento(root)

    for f in faturamento_list:
        print(f)

    media = calcular_media(faturamento_list)
    print(f"Média de faturamento: {media}")

if __name__ == "__main__":
    main()
