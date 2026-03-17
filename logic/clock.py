from datetime import datetime

def get_time():
    # Returns current time as a string in HH:MM format
    return datetime.now().strftime("%H:%M")

def get_date():
    # Returns current date as a string in Day DD Mon format
    # e.g. "Sunday 15 Mar"
    return datetime.now().strftime("%A %d %b")

def get_time_of_day():
    hour = datetime.now().hour
    
    if hour < 12:
        return "morning"
    elif hour < 18:
        return "afternoon"
    else:
        return "evening"
    
# Only runs when executing this file directly, not when imported
if __name__ == "__main__":
    print(get_time())
    print(get_date())