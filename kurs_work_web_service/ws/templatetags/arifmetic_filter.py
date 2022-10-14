from django import template

register = template.Library()


def div_by_3(value):
    if value % 3 == 0:
        return True
    else:
        return False


register.filter('div_by_3', div_by_3)
