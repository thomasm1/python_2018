import json
import csv

sourceFile = open("json.json", "r")

json_data = json.load(sourceFile)

print(json_data["tom2"])
print(json_data["tom"])

outputFile = open("ConvertedJSON.csv", "w")

outputWriter = csv.writer(outputFile)

for name in json_data["tom2"]:
    row_array = []
    row_array.append(json_data["tom2"])
    for name in tom: 
        row_array.append(tom[name])
    outputWriter.writerow(row_array)

sourceFile.close()
outputFile.close()
