def duration(seconds: int):
    if seconds is not None:
        seconds = int(seconds)
        day = seconds // (3600 * 24)
        hour = seconds // 3600 % 24
        minute = seconds % 3600  // 60
        second = seconds % 3600 % 60
        if day > 0:
            return '{:2d} day {:2d} hour {:2d} min {:2d} sec'.format(day, hour, minute, second)
        elif hour > 0:
            return '{:2d} hour {:2d} min {:2d} sec'.format(hour, minute, second)
        elif minute > 0:
            return '{:2d} min {:2d} sec'.format(minute, second)
        elif second > 0:
            return '{:2d} sec'.format(second)
    return '_'

print(duration(53))
print(duration(153))
print(duration(4153))
print(duration(400153))