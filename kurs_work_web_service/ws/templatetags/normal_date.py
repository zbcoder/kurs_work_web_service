from datetime import datetime
import time
import datetime

from django import template

register = template.Library()


def normal_date(value):

    return value


register.filter('normal_date', normal_date)
