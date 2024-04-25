
def total_time(start_hour, start_min, end_hour, end_min):
    if start_hour > end_hour: # total hours in minues
        start_hour = -12+start_hour
    if start_min > end_min:
        start_min = -60+start_min
    return str(end_hour-start_hour)+":"+ str(end_min-start_min)

def get_hour(start_time, end_time):
    start_hour, start_min = start_time.split(":")[:2] 
    end_hour,end_min = end_time.split(":")[:2]
    return total_time(int(start_hour),int(start_min), int(end_hour), int(end_min))

def total_hour(hour_list):
    hour = 0
    mint = 0
    for item in hour_list:
        hour += int(item.split(":")[0])
        mint += int(item.split(":")[1])
    hour+=mint//60
    mint%=60
    return str(hour)+":"+str(mint)

