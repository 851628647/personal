import datetime
import logging
import os
import re
from django.conf import settings

log_path = settings.LOG_PATH
log_save_days = int(settings.LOG_SAVE_DAYS)

# change time region
"""
def beijing(sec, what):
    beijing_time = datetime.datetime.now() + datetime.timedelta(hours=8)
    return beijing_time.timetuple()
logging.Formatter.converter = beijing
"""

def print_log(message, type = "info"):
    """
        print message to log
    """
    today = datetime.date.today().strftime('%Y%m%d')
    logging.basicConfig(
        filename=os.path.join(settings.LOG_PATH, today), 
        format='%(asctime)s \t %(levelname)s \t %(message)s', 
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.INFO
    )
    if type == "info":
        logging.info(message)
    if type == "error":
        logging.error(message)

def clear_history_log():
    """
       remove history log file
    """
    today = datetime.date.today().strftime('%Y%m%d')
    remove_day = (datetime.date.today() - datetime.timedelta(days=log_save_days)).strftime('%Y%m%d')
    for f in os.listdir(log_path):
        if re.match(r'\d{8}',f) and f < remove_day:
            rm_log_file = os.path.join(log_path,f)
            os.system('rm -f {rm_log_file}'.format(rm_log_file=rm_log_file))
