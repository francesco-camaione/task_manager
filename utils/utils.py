from datetime import datetime

def getSqlDatetime() -> str:
    now = datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')
