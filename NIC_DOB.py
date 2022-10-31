n = input("NIC number: ")

while len(n) != 0:
    if len(n) == 12:
        y = int(n)//10**8

        m_list = [31,29,31,30,31,31,30,31,30,31,30,31]
        m = int(n[4]+n[5]+n[6])

        tot_d = 0
        month = 0
        for i in m_list:
            tot_d += i
            month += 1
            if tot_d >= m:
                g = "Male"
                break
            elif m > 500 and tot_d + 500 >= m:
                 g = "Female"
                 m = m - 500
                 break
        day = m_list[month-1] - (tot_d - m)
        print("year:"+str(y)+"\n"+"Month:"+str(month)+"\n"+"Day:"+str(day)+"\n"+"Gender:"+g)
        #n = input("NIC number: ")
        #200065201334
    else:
        print('wrong input')
    n = input("NIC number: ")
    
    
