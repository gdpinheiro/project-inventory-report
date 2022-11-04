from inventory_report.inventory.product import Product


def test_cria_produto():
    test_product = Product(
        1,
        "produto",
        "empresa",
        "01/01/2020",
        "01/01/2021",
        "12345",
        "armazenar em geladeira",
    )
    assert test_product.id == 1
    assert test_product.nome_do_produto == "produto"
    assert test_product.nome_da_empresa == "empresa"
    assert test_product.data_de_fabricacao == "01/01/2020"
    assert test_product.data_de_validade == "01/01/2021"
    assert test_product.numero_de_serie == "12345"
    assert test_product.instrucoes_de_armazenamento == "armazenar em geladeira"
