


def normalize_data (rawdata):
    region = []
    house = []
    listed_regions = set()

    for row in rawdata:
        region_name = row["Region_Name"].strip()
        area_code = row["Area_Code"].strip()


        if area_code not in listed_regions:

            region.append({
                "region_name": region_name,
                "area_code": area_code
            })

            listed_regions.add(area_code)

        date = row["Date"].strip()
        average_price = row["Average_Price"].strip()
        monthly_change = row["Monthly_Change"].strip() or None
        annual_change = row["Annual_Change"].strip() or None
        seasonal_adjusted_price = row["Average_Price_SA"].strip() or None

        house.append({"date":date,
                      "area_code": area_code,
                      "average_price":average_price,
                      "monthly_change": monthly_change,
                      "annual_change": annual_change,
                      "seasonal_adjusted_price":seasonal_adjusted_price ,})


    return region, house