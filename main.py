import connectdb
import createdb
import extract, transform, load
import time

def create_db_func():
    createdb.createdb()

def wait_for_db():
    while True:
        try:
            with connectdb.get_connection():

                print("Database is ready!")
            return
        except Exception as e:
            print(f"Waiting for database setup... {e}")
            time.sleep(2)

def main():
    rawdata = extract.extract()
    regions, houses = transform.normalize_data(rawdata)
    load.load_data(regions, houses)



if __name__ == "__main__":
    wait_for_db()
    create_db_func()
    main()