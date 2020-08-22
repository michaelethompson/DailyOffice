from datetime import date, timedelta


class LiturgicalYear:
    def __init__(self, year, v2=False):
        # v2 = "Vatican II" and refers to the reforms made to the calendar
        # which were adopted my many Protestant denominations in the 1970's
        # The only significant change for our purposes, is the date of
        # Transfiguration Sunday, which in turn is used to calculate the number
        # of Sundays after Epiphany.
        self.init_calendar(year, v2)

    def calc_easter(self, year):
        "Returns easter as a date object."
        a = year % 19
        b = year // 100
        c = year % 100
        d = (19 * a + b - b // 4 - ((b - (b + 8) // 25 + 1) // 3) + 15) % 30
        e = (32 + 2 * (b % 4) + 2 * (c // 4) - d - (c % 4)) % 7
        f = d + e - 7 * ((a + 11 * d + 22 * e) // 451) + 114
        month = f // 31
        day = f % 31 + 1
        return date(year, month, day)

    def init_calendar(self, year, v2=False):
        self.vatican2 = v2
        self.easter = self.calc_easter(year + 1)

        # The first Sunday in Advent is always on or after November 27th
        nov27day = date(year, 11, 27).isoweekday()
        if nov27day == 7:
            self.advent1 = date(year, 11, 27)
        else:
            self.advent1 = date(year, 11, 27) + timedelta(7 - nov27day)



        self.advent4 = self.advent1 + timedelta(21)

        # Now calculate the date of the next First Sunday in Advent in order to
        # calculate Sundays after Trinity.
        nov27day = date(year + 1, 11, 27).isoweekday()
        if nov27day == 7:
            self.next_advent1 = date(year + 1, 11, 27)
        else:
            self.next_advent1 = date(year + 1, 11, 27) + timedelta(7 - nov27day)

        #Daily Office Year
        if (self.advent1.year %2 ==0 ):
            self.DailyOfficeYear = 'y1'
        else:
            self.DailyOfficeYear = 'y2'


        # First Sunday after Epiphany
        jan6day = date(year + 1, 1, 6).isoweekday()
        if jan6day == 7:
            self.epiphany1 = date(year + 1, 1, 13)
        else:
            self.epiphany1 = date(year + 1, 1, 13) - timedelta(jan6day)

        # A bunch of easy ones:
        self.epiphany = date(year + 1, 1, 6)
        if v2:
            self.transfiguration = self.easter - timedelta(49)
        else:
            self.transfiguration = self.easter - timedelta(70)
        self.septuagesima = self.easter - timedelta(63)
        self.ashWednesday = self.easter - timedelta(46)
        self.lent1 = self.ashWednesday + timedelta(4)
        self.maundyThursday = self.easter - timedelta(3)
        self.goodFriday = self.easter - timedelta(2)
        self.palmSunday = self.easter + timedelta(7)
        self.ascension = self.easter + timedelta(39)
        self.pentecost = self.easter + timedelta(49)
        self.trinity = self.easter + timedelta(56)
        self.trinityLast = self.next_advent1 - timedelta(7)
        self.pentecostLast = self.trinityLast

        # Sundays after Epiphany and Trinity/Pentecost
        # Note: Epiphany Sundays include Transfiguration
        self.epiphanySundays = (self.transfiguration - self.epiphany1).days / 7 + 1
        self.trinitySundays = (self.next_advent1 - self.trinity).days / 7 - 1
        self.pentecostSundays = self.trinitySundays + 1

        #Remaining Special Days from the Daily Lectionary
        self.dec24 = date(year, 12, 24)
        self.christmasEve = date(year, 12, 24)
        self.christmasDay = date(year, 12, 25)
        self.christmas1 = date(year, 12, 25) + timedelta(7 - (date(year, 12, 25).weekday() + 1) % 7)
        self.dec29 = date(year, 12, 29)
        self.dec30 = date(year, 12, 30)
        self.dec31 = date(year, 12, 31)
        self.holyNameEve = date(year, 12, 31)
        self.holyName = date(year + 1, 1, 1)
        self.christmas2 = self.christmas1 + timedelta(7)
        self.jan2 = date(year + 1, 1, 2)
        self.jan3 = date(year + 1, 1, 3)
        self.jan4 = date(year + 1, 1, 4)
        self.jan5 = date(year + 1, 1, 5)
        self.epiphanyEve = self.epiphany - timedelta(1)
        self.jan7 = date(year + 1, 1, 7)
        self.jan8 = date(year + 1, 1, 8)
        self.jan9 = date(year + 1, 1, 9)
        self.jan10 = date(year + 1, 1, 10)
        self.jan11 = date(year + 1, 1, 11)
        self.jan12 = date(year + 1, 1, 12)
        self.epiphany1Eve = self.epiphany1 - timedelta(1)
        self.holySaturday = self.easter - timedelta(1)
        self.ascentionEve = self.ascension - timedelta(1)
        self.pentecostEve = self.pentecost - timedelta(1)
        self.trinityEve = self.trinity - timedelta(1)
        self.holyMonday = self.easter - timedelta(6)
        self.holyTuesday = self.easter - timedelta(5)
        self.holyWednesday = self.easter - timedelta(4)

        # And finally, American Thanksgiving - which shouldn't even be here,
        # but too many people complain if it's not:
        nov1day = date(year + 1, 11, 1).isoweekday()
        if nov1day <= 4:
            self.thanksgiving = date(year + 1, 11, 26 - nov1day)
        else:
            self.thanksgiving = date(year + 1, 11, 33 - nov1day)
        #Propers for the Season after Pentecost
        d1 = date(year+1, 5, 11) - timedelta((date(year+1, 5, 11).weekday() + 1) % 7)
        d2 = d1 + timedelta(7)
        if (date(year+1, 5, 11) - d1 < d2 - date(year+1, 5, 11)):
            self.proper1 = d1
        else:
            self.proper1 = d2




def whichyear(targetdate):
    y=targetdate.year
    if(date(y,11,27).isoweekday())==7:
        a1=date(y,11,27)
    else:
        a1=date(y,11,27) + timedelta(7 - date(y,11,27).isoweekday())

    if (date(y+1, 11, 27).isoweekday()) == 7:
        a2 = date(y+1, 11, 27)
    else:
        a2 = date(y+1, 11, 27) + timedelta(7 - date(y+1, 11, 27).isoweekday())

    if(a1 <= targetdate <= a2):
        return targetdate.year
    else:
        return targetdate.year-1

def thissunday(targetdate):
    idx = (targetdate.weekday() + 1) % 7
    return targetdate - timedelta(7 + idx)


thisday=date.today()
#thisday=date(2020,5,3)
thisweekday = (thisday.isoweekday()+1)%7
thisyear=LiturgicalYear(whichyear(thisday))

seasondates=[['advent1',thisyear.advent1,thisyear.epiphany1 - timedelta(days=1)],
             ['epiphany1',thisyear.epiphany1,thisyear.ashWednesday - timedelta(days=1)],
             ['Lent',thisyear.lent1,thisyear.easter - timedelta(days=1)],
             ['easter',thisyear.easter,thisyear.pentecost - timedelta(days=1)],
             ['pentecost',thisyear.pentecost,thisyear.next_advent1 - timedelta(days=1)]
             ]

for season in seasondates:
   if(season[1] <= thisday <= season[2]):
        thisseason=season
        thisseasonweek=(thisday-season[1]).days//7+1

specialdates = [
    ['advent1', thisyear.advent1],
    ['epiphany1', thisyear.epiphany1],
    ['ashWednesday', thisyear.ashWednesday],
    ['easter', thisyear.easter],
    ['pentecost', thisyear.pentecost],
    ['advent4', thisyear.advent4],
    ['epiphany', thisyear.epiphany],
    ['transfiguration', thisyear.transfiguration],
    ['septuagesima', thisyear.septuagesima],
    ['maundyThursday', thisyear.maundyThursday],
    ['goodFriday', thisyear.goodFriday],
    ['palmSunday', thisyear.palmSunday],
    ['ascension', thisyear.ascension],
    ['trinity', thisyear.trinity],
    ['proper1', thisyear.proper1],
    ['thanksgiving', thisyear.thanksgiving],
    ['dec24', thisyear.dec24],
    ['christmasEve', thisyear.christmasEve],
    ['christmasDay', thisyear.christmasDay],
    ['christmas1', thisyear.christmas1],
    ['dec29', thisyear.dec29],
    ['dec30', thisyear.dec30],
    ['dec31', thisyear.dec31],
    ['holyNameEve', thisyear.holyNameEve],
    ['holyName', thisyear.holyName],
    ['christmas2', thisyear.christmas2],
    ['jan2', thisyear.jan2],
    ['jan3', thisyear.jan3],
    ['jan4', thisyear.jan4],
    ['jan5', thisyear.jan5],
    ['epiphanyEve', thisyear.epiphanyEve],
    ['jan7', thisyear.jan7],
    ['jan8', thisyear.jan8],
    ['jan9', thisyear.jan9],
    ['jan10', thisyear.jan10],
    ['jan11', thisyear.jan11],
    ['jan12', thisyear.jan12],
    ['epiphany1Eve', thisyear.epiphany1Eve],
    ['ashWednesday', thisyear.ashWednesday],
    ['holySaturday', thisyear.holySaturday],
    ['ascentionEve', thisyear.ascentionEve],
    ['pentecostEve', thisyear.pentecostEve],
    ['trinityEve', thisyear.trinityEve],
    ['holyMonday',thisyear.holyMonday],
    ['holyTuesday',thisyear.holyTuesday],
    ['holyWednesday',thisyear.holyWednesday]
]

for special in specialdates:
    if special[1]=thisday:
        
print((thisyear.pentecost-thisyear.proper1).days)
print((thisyear.pentecost-thisyear.proper1).days//7)
print((thisyear.trinity-thisyear.proper1).days)
print((thisyear.trinity-thisyear.proper1).days//7)

print(thisyear.DailyOfficeYear)
