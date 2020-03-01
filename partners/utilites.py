from datetime import datetime
from os.path import splitext

def get_timestamp_path_logo_partners(instance, filename):
    return '%s%s%s' % ('partners/logo/', datetime.now().timestamp(), splitext(filename)[1])
