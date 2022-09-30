from datetime import datetime

def show_year():
    full_timestamp = str(datetime.now())
    year = full_timestamp[:4]
    print("The year is", year)


def get_year():
    full_timestamp = str(datetime.now())
    year = full_timestamp[:4]
    return int(year)


result = get_year()
print("The current year is", result)
print("Again, the current year is", result)
print("Next year is", result+1)
print("Last year was", result-1)


