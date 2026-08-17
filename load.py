from connectdb import get_connection

def load_data(regions, houses):
    try:
        connection = get_connection()

        print("Opening cursor...")

        cursor = connection.cursor()
        region_ids = {}
        for region in regions:
            cursor.execute("""
            INSERT INTO regions (region_name, area_code)
            VALUES (%s, %s)
            RETURNING region_id
            """,
            (
                region["region_name"],
                region["area_code"]

            )
            )
            region_id = cursor.fetchone()[0]

            region_ids[region["area_code"]] = region_id
        for data in houses:
            region_id = region_ids[data["area_code"]]
            cursor.execute("""
            INSERT INTO house (date, region_id, average_price, monthly_change, annual_change, seasonal_adjusted_price)
            VALUES (%s, %s, %s, %s, %s, %s)
            """,
            (
                data["date"],
                region_id,
                data["average_price"],
                data["monthly_change"],
                data["annual_change"],
                data["seasonal_adjusted_price"]

            )
        )

        connection.commit()
        print("Data Loaded")
        cursor.close()
        connection.close()

    except Exception as e:
        print("Load failed", e)
