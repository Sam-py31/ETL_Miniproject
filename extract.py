import csv
from pathlib import Path

bucket = Path("AssesmentProject/csvbucket")



def extract():
    content = []
    for file in bucket.glob("*.csv"):
        with file.open("r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            content.extend(parse(reader))

    return content

def parse(reader):
    data = []
    for row in reader:
        date = row["Date"].strip()
        average_price = row["Average_Price"].strip()
        region_name = row["Region_Name"].strip()
        area_code = row["Area_Code"].strip()


        if not date or not region_name or not area_code or not average_price:
            continue

        data.append(row)

    return data