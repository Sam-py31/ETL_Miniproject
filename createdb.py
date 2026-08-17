from connectdb import get_connection
def createdb():
    try:

        connection = get_connection()

        print("Opening cursor...")

        cursor = connection.cursor()




        cursor.execute('''
                    create table if not exists regions (
                    region_id serial primary key,
                    region_name VARCHAR(100) not null,
                    area_code VARCHAR(100) not null

                    )
                    ''')





        cursor.execute(     """
        CREATE TABLE IF NOT EXISTS house (
            house_id SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            region_id INTEGER NOT NULL REFERENCES regions(region_id),
            average_price DECIMAL,
            monthly_change DECIMAL,
            annual_change DECIMAL,
            seasonal_adjusted_price DECIMAL
        )
        """)


        


        connection.commit()

        print("Tables created successfully!")

        cursor.close()
        connection.close()

    except Exception as e:
        print ("Failed to create database", e)