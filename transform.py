


def normalize_data (rawdata):
    region = []
    house = []
    listed_regions = set()

    for row in rawdata:
        region_name = row["region_name"].strip()
        area_code = row["area_code"].strip()


        if area_code not in listed_regions:

            region.append({
                "region_name": region_name,
                "area_code": area_code
            })

            listed_regions.add(area_code)

        date = row["date"].strip()
        average_price = row["average_price"].strip()

        house.append({"date":date,
                      "area_code": area_code,
                      "average_price":average_price,
                        })


    return region, house