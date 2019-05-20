def timeConversion(s):
    # print(s[3:-2])
    hour = s[:2]
    notation = s[-2:]
    min_sec = s[3:-2]
    time = ''
    if notation == 'PM' and hour != '12':
        time = '{:02d}'.format(int(hour) + 12)+ ':' + min_sec
    elif notation == 'AM' and hour == '12':
        time = '00:' + min_sec
    else:
        time = '{:02d}'.format(int(hour))+ ':' + min_sec
    print(time)
    return time

# timeConversion('07:05:45AM')
timeConversion('12:45:54PM')