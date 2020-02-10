import json
import glob

result = []
for f in glob.glob("jsonfiles/nvdcve-1.1-2020.json"):
    with open(f, "r") as infile:
        result.append(json.load(infile))

with open("nvdcve_2020.json", "w") as outfile:
     json.dump(result, outfile)
    