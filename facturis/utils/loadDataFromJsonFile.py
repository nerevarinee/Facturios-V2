import json


def loadDataFromJsonFile(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
                data = list(reversed(data))
                factures = data
    return factures

if __name__ == "__main__":
    pass