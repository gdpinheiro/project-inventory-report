from inventory_report.inventory.product import Product


def test_relatorio_produto():
    test_product = Product(
        1,
        "produto",
        "empresa",
        "01/01/2020",
        "01/01/2021",
        "12345",
        "armazenar em geladeira",
    )

    assert (
        test_product.__repr__() == f"O produto {test_product.nome_do_produto}"
        f" fabricado em {test_product.data_de_fabricacao}"
        f" por {test_product.nome_da_empresa}"
        f" com validade até {test_product.data_de_validade}"
        f" precisa ser armazenado {test_product.instrucoes_de_armazenamento}."
    )
