from inventory_report.reports.simple_report import SimpleReport
from collections import Counter


class CompleteReport(SimpleReport):
    def generate(list):
        simple_report = SimpleReport.generate(list)
        companies = []

        simple_report += "\nProdutos estocados por empresa:\n"
        for index in list:
            companies.append(index["nome_da_empresa"])

        amount_company = Counter(companies)
        for first, end in Counter(amount_company.items()):
            simple_report += f"- {first}: {end}\n"

        return simple_report
