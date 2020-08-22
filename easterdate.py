import datetime




def easter_date(y):
    FirstDig = y // 100
    Remain19 = y % 19
    temp = (FirstDig - 15) // 2 + 202 - 11 * Remain19
    if (FirstDig in [21, 24, 25, 27, 28, 29, 30, 31, 32, 34, 35, 38]):
        temp = temp - 1
    elif (FirstDig in [33, 36, 37, 39, 40]):
        temp = temp - 2
    temp = temp % 30
    tA = temp + 21
    if (temp == 29):
        tA = tA - 1
    if (temp == 28 & Remain19 > 10):
        tA = tA - 1
    tB = (tA - 19) % 7
    tC = (40 - FirstDig) % 4
    if (tC == 3):
        tC = tC + 1
    if (tC > 1):
        tC = tC + 1
    temp = y % 100
    tD = (temp + temp // 4) % 7
    tE = ((20 - tB - tC - tD) % 7) + 1
    d = tA + tE
    if (d > 31):
        d = d - 31
        m = 4
    else:
        m = 3
    return datetime.datetime(y, m, d)

print(easter_date(2028))

print(datetime.datetime(2027,12,25))
print(datetime.datetime(2027,12,25).weekday())