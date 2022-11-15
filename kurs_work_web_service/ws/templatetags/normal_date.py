from datetime import datetime
import time
import datetime

from django import template

register = template.Library()


def normal_date(value):

    return value


def get_page(value):
    try:
        page_numb = value.split('/').pop().split('?').pop().strip()
        if page_numb == '':
            page_numb = 1
    except:
        page_numb = 1
    return page_numb


register.filter('normal_date', normal_date)
register.filter('get_page', get_page)

