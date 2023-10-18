def seasons():
    month = str(input('Enter the current month name\n'))
    # define lower register
    month = month.lower()

    if month in ["december", "january", "november"]:
        season = "winter"
    elif month in ["march", "april", "may"]:
        season = "spring"
    elif month in ["june", "july", "august"]:
        season = "summer"
    elif month in ["september", "october", "november"]:
        season = "autumn"
    else:
        season = "unknown"

    if season != "unknown":
        print(f"The season for {month} is {season}")
    return None
# what will happen if list elements start with high register?
# how .lower works?

seasons()