'''
Your task in order to complete this Kata is to write a function which formats a duration, 
given as a number of seconds, in a human-friendly way.

If it is zero, it just returns "now".
Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.

format_duration(62)    # returns "1 minute and 2 seconds"
format_duration(3662)  # returns "1 hour, 1 minute and 2 seconds"

For the purpose of this Kata, a year is 365 days and a day is 24 hours.
Note that spaces are important.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and "

A component will not appear at all if its value happens to be zero. 
Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.

A unit of time must be used "as much as possible". 
It means that the function should not return 61 seconds, but 1 minute and 1 second instead. 
'''


def format_duration(seconds):
    
    result = []

    if seconds == 0:
        return 'now'

    # YEARS
    if seconds >= 31536000:
        years_count = int(seconds/31536000)

        if years_count < 2:
            result.append("1 year")
        else:
            result.append(str(years_count) + " years")
    
        seconds = seconds - (31536000 * years_count)

    # DAYS
    if seconds >= 86400:
        days_count = int(seconds/86400)

        if days_count < 2:
            result.append("1 day")
        else:
            result.append(str(days_count) + " days")
    
        seconds = seconds - (86400 * days_count)

    # HOURS
    if seconds >= 3600:
        month_count = int(seconds/3600)

        if month_count < 2:
            result.append("1 month")
        else:
            result.append(str(month_count) + " months")
    
        seconds = seconds - (3600 * month_count)

    # MINUTES
    if seconds >= 60:
        minutes_count = int(seconds/60)

        if minutes_count < 2:
            result.append("1 hour")
        else:
            result.append(str(minutes_count) + " hours")
    
        seconds = seconds - (60 * minutes_count)

    # SECONDS
    if seconds > 0:
        if seconds == 1:
            result.append("1 second")
        else:
            result.append(str(seconds) + " seconds")
    

    # RESULT STRING
    result_text = ''

    if len(result) == 1:
        result_text += str(result[0])

    else:
        for index, item in enumerate(result):
            result_text += item

            if index < (len(result) - 2):
                result_text += ', '

            elif index == (len(result) - 2):
                result_text += ' and '

    return result_text


print(format_duration(42536000))

print(format_duration(1)) # 1 second
print(format_duration(62)) # 1 minute and 2 seconds
print(format_duration(120)) # 2 minutes
print(format_duration(3600)) # 1 hour
print(format_duration(3662)) # 1 hour, 1 minute, 2 seconds


# year 31536000
# hour 3600
# minute 60


