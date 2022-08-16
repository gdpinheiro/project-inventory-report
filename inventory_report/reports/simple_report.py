from collections import Counter


class SimpleReport:
    def generate(product_list):
        data_fabricacao_list = []
        data_validade_list = []
        nome_empresa_list = []

        for item in product_list:
            data_fabricacao_list.append(item["data_de_fabricacao"])
            data_validade_list.append(item["data_de_validade"])
            if item.__contains__("nome_da_empresa"):
                nome_empresa_list.append(item["nome_da_empresa"])

        oldest_date = sorted(data_fabricacao_list)[0]
        newest_date = sorted(data_validade_list)[0]
        most_common_company = Counter(nome_empresa_list).most_common(1)[0][0]

        return (
            f"Data de fabricação mais antiga: {oldest_date}\n"
            f"Data de validade mais próxima: {newest_date}\n"
            f"Empresa com mais produtos: {most_common_company}"
        )
