def breakdown_time(seconds):
    ### Replace with your own code (begin) ###
    if type(seconds) is not int or seconds < 0:
        return -1
    
    if seconds == 0:
        return {}
    
    hour = seconds // 3600
    remainder = seconds % 3600
    minute = remainder // 60
    second = remainder % 60
    
    result = {3600: hour, 60: minute, 1: second}

    
    return {key: value for key, value in result.items() if value != 0}
    pass
    ### Replace with your own code (end)   ###
