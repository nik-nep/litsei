from datetime import datetime
from os.path import splitext

def get_timestamp_path_announcement(instance, filename):
    return '%s%s%s' % ('announcement/photo/', datetime.now().timestamp(), splitext(filename)[1])
