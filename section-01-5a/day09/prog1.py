from datetime import datetime

def show_year():
    full_timestamp = str(datetime.now())
    year = full_timestamp[:4]
    print("The year is", year)

show_year()


