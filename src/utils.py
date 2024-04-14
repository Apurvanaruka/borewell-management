
def total_time(start_hour, start_min, end_hour, end_min):
    
    if start_hour > end_hour: # total hours in minues
        start_hour = -12+start_hour
    if start_min > end_min:
        start_min = -60+start_min

    return (end_hour-start_hour, end_min-start_min)



