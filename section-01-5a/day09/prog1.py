from datetime import datetime

def show_year():
    full_timestamp = str(datetime.now())
    year = full_timestamp[:4]
    print("The year is", year)


def get_year():
    full_timestamp = str(datetime.now())
    year = full_timestamp[:4]
    return year


get_year()


