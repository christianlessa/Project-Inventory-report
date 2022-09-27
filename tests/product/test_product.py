from inventory_report.inventory.product import Product


def test_cria_produto():
    product = Product(
        id=1,
        nome_do_produto="Camera",
        nome_da_empresa="Amazon",
        data_de_fabricacao="2022-01-10",
        data_de_validade="2023-01-10",
        numero_de_serie="1234567891",
        instrucoes_de_armazenamento="instrucao1",
    )

    assert product.id == 1
    assert product.nome_do_produto == "Camera"
    assert product.nome_da_empresa == "Amazon"
    assert product.data_de_fabricacao == "2022-01-10"
    assert product.data_de_validade == "2023-01-10"
    assert product.numero_de_serie == "1234567891"
    assert product.instrucoes_de_armazenamento == "instrucao1"
