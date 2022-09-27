from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        1,
        "farinha",
        "Farinini",
        "01-05-2021",
        "02-06-2023",
        "1234567891",
        "instrucao1",
    )

    result = (
        f"O produto {product.nome_do_produto}"
        f" fabricado em {product.data_de_fabricacao}"
        f" por {product.nome_da_empresa} com validade"
        f" até {product.data_de_validade}"
        f" precisa ser armazenado {product.instrucoes_de_armazenamento}."
    )

    assert product.__repr__() == result
