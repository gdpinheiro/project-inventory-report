import csv

from ..reports.complete_report import CompleteReport

from ..reports.simple_report import SimpleReport


class Inventory:
    def import_data(path, type):
        with open(path, "r") as file:
            reader = csv.DictReader(file)
            data = list(reader)
            if type == "simples":
                return SimpleReport.generate(data)
            return CompleteReport.generate(data)
