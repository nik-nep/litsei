from datetime import datetime
from os.path import splitext


def get_timestamp_path_cover(instance, filename):
    return '%s%s%s' % ('library/cover/', datetime.now().timestamp(), splitext(filename)[1])

def get_timestamp_path_book(instance, filename):
    return '%s%s%s' % ('library/book/', datetime.now().timestamp(), splitext(filename)[1])

def get_timestamp_path_book_author(instance, filename):
    return '%s%s%s' % ('library/book/author/', datetime.now().timestamp(), splitext(filename)[1])
