class SimpleReport:
    def generate(list):
        manufacturing_date = []
        closest_expiration_date = []
        company_with_more_products = []

        for index in list:
            manufacturing_date.append(index["data_de_fabricacao"])
            closest_expiration_date.append(index["data_de_validade"])
            company_with_more_products.append(index["nome_da_empresa"])

        company = max(set(
            company_with_more_products), key=company_with_more_products.count)

        return (
            f"Data de fabricação mais antiga: {min(manufacturing_date)}\n"
            f"Data de validade mais próxima: {min(closest_expiration_date)}\n"
            f"Empresa com mais produtos: {company}"
        )
