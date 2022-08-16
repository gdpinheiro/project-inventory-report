import csv
import json
import xmltodict

from ..reports.complete_report import CompleteReport

from ..reports.simple_report import SimpleReport


class Inventory:
    def import_data(path, type):
        with open(path, "r") as file:
            if path.endswith(".csv"):
                reader = csv.DictReader(file)
                data = list(reader)

            if path.endswith(".json"):
                data = json.load(file)

            if path.endswith(".xml"):
                xml_file = file.read()
                parsed_file = xmltodict.parse(xml_file)
                data = parsed_file["dataset"]["record"]

            if type == "simples":
                return SimpleReport.generate(data)
            return CompleteReport.generate(data)
