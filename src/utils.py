
def total_time(start_hour, start_min, end_hour, end_min):
    if start_hour > end_hour: # total hours in minues
        start_hour = -12+start_hour
    if start_min > end_min:
        start_min = -60+start_min
    return str(end_hour-start_hour)+":"+ str(end_min-start_min)

def get_hour(start_time, end_time):
    start_hour = int(start_time[:2]) 
    start_min = int(start_time[3:])
    end_hour = int(end_time[:2])
    end_min = int(end_time[3:])
    return total_time(start_hour, start_min, end_hour, end_min)

def total_hour(hour_list):
    hour = 0
    mint = 0
    for item in hour_list:
        hour += int(item[:1])
        mint += int(item[2:])
    hour += mint//60
    mint%=60
    return str(hour)+":"+str(mint)

