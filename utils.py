from datetime import datetime

def generate_timestamps():
    #Generating time stamps
    unformatted_time = datetime.now()
    formatted_time = unformatted_time.strftime("%Y%m%d%H%M%S")

    return formatted_time

generate_timestamps()