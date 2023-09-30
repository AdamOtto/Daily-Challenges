"""
Given a clock time in hh:mm format, determine, to the nearest degree, the angle between the hour and the minute hands.

Bonus: When, during the course of a day, will the angle be zero?
"""
def Solution(hh, mm):
    if mm > 60 or hh > 12:
        return False
    if hh == 12:
        hh = 0
    if mm == 60:
        mm = 0
        hh += 1
    
    mmAngle = (mm / 60) * 360.0
    hhAngle = ((hh / 12 ) * 360) + ( (mm / 60) * 30)
    retVal = abs(hhAngle - mmAngle)
    return min(retVal, 360 - retVal)


for hour in range(0, 13):
    minute = 0
    while minute < 60:
        if int(Solution(hour, minute)) == 0:
            print(str(hour) + ":" + str(minute) + " angle is 0")
        minute += 0.1