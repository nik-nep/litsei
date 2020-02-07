from datetime import datetime
from os.path import splitext

def get_timestamp_path(instance, filename):
    return '%s%s' % (datetime.now().timestamp(), splitext(filename)[1])

def get_timestamp_path_article(instance, filename):
    return '%s%s%s' % ('articles/', datetime.now().timestamp(), splitext(filename)[1])

def get_timestamp_path_article_photo(instance, filename):
    return '%s%s%s' % ('articles/photo/', datetime.now().timestamp(), splitext(filename)[1])

def get_timestamp_path_article_video(instance, filename):
    return '%s%s%s' % ('articles/video/', datetime.now().timestamp(), splitext(filename)[1])
