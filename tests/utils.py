from datetime import datetime, timedelta

def get_current_date():
    current_date = datetime.now().strftime("%Y-%m-%d")
    return current_date

def get_future_date():
    current_date = datetime.now()
    future_date = current_date + timedelta(days=5)
    formatted_date = future_date.strftime("%Y-%m-%d")
    return formatted_date

def change_date_format(date):
    date_parts = date.split('-')
    changed_date = date_parts[2] + '-' + date_parts[1] + '-' + date_parts[0]
    return changed_date