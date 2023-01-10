from datetime import date, datetime

t = str(date.today()).split("-")
month = t[1].replace("0","") if (t[1][0] == "0") else t[1]

todays_date = month + '/' + t[2] + "/" + t[0]
end_date = "3/3/2023"

class DateException(Exception):
    pass

def check_date(date1):
    s = [int(x) for x in date1.split("/")]
    
    if (len(s) != 3) or (s[0] > 12) or (s[1] > 31) or (s[2] < 0):
        raise DateException("Date formatted incorrectly!")

    if (s[2] > 9 and s[2] < 100):
        s[2] = "20" + s[2]

    return s

def convert_to_min(d):
    l = [int(x) for x in d.split(":")]
    hours, mins, secs = 23 - l[0], 60 - l[1], 60 - l[2]
    return f"{hours} Hours {mins} Minutes {secs} Seconds left today!\n"

if (len(todays_date.split("/")) == 3):
    m1, d1, y1 = check_date(todays_date)
    m2, d2, y2 = check_date(end_date)
    days_left = (date(y2, m2, d2) - date(y1, m1, d1)).days
    print(f"\n{days_left} days left until Spring break!")
    print(f"{days_left/7:.2f} weeks left!")

print(convert_to_min(datetime.now().strftime("%H:%M:%S")))