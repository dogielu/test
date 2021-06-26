def remainder(days):
    years=days // 365
    months =(days%365)//30
    days_rem=(days%365) % 30
    return "{} year(s) {} month(s) and {} day(s) remain.".format(years,months,days_rem)
