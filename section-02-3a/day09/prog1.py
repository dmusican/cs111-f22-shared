from datetime import datetime

def show_year():
    full_timestamp = str(datetime.now())
    year = full_timestamp[:4]
    print("Here is the year:", year)

def get_year():
    full_timestamp = str(datetime.now())
    year = full_timestamp[:4]
    return int(year)



#show_year()

result = get_year()
print("Your year, my friends, is", result)
print("Here it is again, my friend", result)
print("Last year, was", result-1)
print("Next year, is", result+1)