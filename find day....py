m_list1 = [31,29,31,30,31,31,30,31,30,31,30,31]
m_list2 = [31,28,31,30,31,31,30,31,30,31,30,31]
d_list = ['mon','tue','wed','thu','fri','sat','sun']


year = int(input("Year: "))
month = int(input("Month: "))               #19/5/2021~wed
day = int(input("Day: "))
while year>1900:
    if (year%400 == 0) or (year%100 != 0 and year%4 == 0):
        m_list = m_list1
    else:
        m_list = m_list2
    print(m_list)
    days = 0 
    for j in range(1900,year):
        if (year%400 == 0) or (year%100 != 0 and year%4 == 0):
            days = days + 366
        else:
            days = days + 365

    for i in range(month-1):
        days += m_list[i]

    days += day

    rd = (days) % 7

    day_n = d_list[rd]
    print(day_n)       
    year = int(input("Year: "))
    month = int(input("Month: "))               
    day = int(input("Day: "))



