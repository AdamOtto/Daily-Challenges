"""
The “active time” of a courier is the time between the
pickup and dropoff of a delivery. Given a set of data formatted like the following:

(delivery id, timestamp, pickup/dropoff)
Calculate the total active time in seconds.

A courier can pick up multiple orders before dropping them off.
The timestamp is in unix epoch seconds.

For example, if the input is the following:

(1, 1573280047, 'pickup')
(1, 1570320725, 'dropoff')
(2, 1570321092, 'pickup')
(3, 1570321212, 'pickup')
(3, 1570322352, 'dropoff')
(2, 1570323012, 'dropoff')
The total active time would be 1260 seconds.
"""

def Solution(ar):
    d = {}
    dropOff = None
    pickUp = None
    retVal = 0
    for i in range(len(ar)):
        if ar[i][2] == 'dropoff':
            if dropOff is not None:
                dropOff = min(dropOff, ar[i][1])
            else:
                dropOff = ar[i][1]
        else:
            if dropOff is not None:
                retVal += max(0, dropOff - pickUp)
                dropOff = None
                pickUp = None
            if pickUp is not None:
                pickUp = min(ar[i][1], pickUp)
            else:
                pickUp = ar[i][1]
    
    if dropOff is not None:
                retVal += max(0, dropOff - pickUp)
                dropOff = None
    
    return retVal

# Returns 1260
in1 = [ (1, 1573280047, 'pickup'),
        (1, 1570320725, 'dropoff'),
        (2, 1570321092, 'pickup'),
        (3, 1570321212, 'pickup'),
        (3, 1570322352, 'dropoff'),
        (2, 1570323012, 'dropoff')]
print(Solution(in1))