from django import template

register = template.Library()

@register.filter
def sort_by_start_time(shifts):
    return sorted(shifts, key=lambda x: x.start_time)