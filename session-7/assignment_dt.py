from datetime import datetime

# datetime to string
def datetime_to_str_1(dt):
    return dt.strftime("%Y-%m-%d")

def datetime_to_str_2(dt):
    return dt.strftime("%y-%m-%d")

def datetime_to_str_3(dt):
    return dt.strftime("%B %d, %Y")

def datetime_to_str_4(dt):
    return dt.strftime("%b %d, %Y")

def datetime_to_str_5(dt):
    return dt.strftime("%d %B %Y")

def datetime_to_str_6(dt):
    return dt.strftime("%A %B %d, %Y")

def datetime_to_str_7(dt):
    return dt.strftime("%a %B %d, %Y")

def datetime_to_str_8(dt):
    return dt.strftime("%Y-%m-%d %H:%M:%S")

def datetime_to_str_9(dt):
    return dt.strftime("%H:%M:%S")

def datetime_to_str_10(dt):
    return dt.strftime("%I:%M %p")

# string to datetime
def str_to_datetime_1(s):
    return datetime.strptime(s, "%Y-%m-%d")

def str_to_datetime_2(s):
    return datetime.strptime(s, "%y-%m-%d")

def str_to_datetime_3(s):
    return datetime.strptime(s, "%B %d, %Y")

def str_to_datetime_4(s):
    return datetime.strptime(s, "%b %d, %Y")

def str_to_datetime_5(s):
    return datetime.strptime(s, "%d %B %Y")

def str_to_datetime_6(s):
    return datetime.strptime(s, "%A %B %d, %Y")

def str_to_datetime_7(s):
    return datetime.strptime(s, "%a %B %d, %Y")

def str_to_datetime_8(s):
    return datetime.strptime(s, "%Y-%m-%d %H:%M:%S")

def str_to_datetime_9(s):
    return datetime.strptime(s, "%H:%M:%S")
def str_to_datetime_10(s):
    return datetime.strptime(s, "%I:%M %p")