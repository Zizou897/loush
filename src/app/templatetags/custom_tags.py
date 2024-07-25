from django import template

register = template.Library()

@register.simple_tag
def my_enumerate(queryset):
    for index, item in enumerate(queryset):
        yield index, item 