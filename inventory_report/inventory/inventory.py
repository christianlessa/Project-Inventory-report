from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport
import csv
import json


class Inventory:
    @classmethod
    def extract_data(clas, path):
        data = []

        if path.endswith(".csv"):
            with open(path) as files:
                for index in csv.DictReader(files):
                    data.append(index)
        elif path.endswith(".json"):
            with open(path) as json_files:
                data = json.load(json_files)
        return data

    @classmethod
    def import_data(clas, path, type):
        data = clas.extract_data(path)

        if type == "simples":
            return SimpleReport.generate(data)
        elif type == "completo":
            return CompleteReport.generate(data)
        else:
            ValueError
