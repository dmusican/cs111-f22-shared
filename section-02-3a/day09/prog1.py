from datetime import datetime

def show_year():
    full_timestamp = str(datetime.now())
    year = full_timestamp[:4]
    print("Here is the year:", year)

def get_year():
    full_timestamp = str(datetime.now())
    year = full_timestamp[:4]
    return year



#show_year()

get_year()