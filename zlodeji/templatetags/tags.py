from django import template
from django.template.defaultfilters import stringfilter

from zlodeji.models import Urobil

register = template.Library()


@register.filter
@register.inclusion_tag('zlodeji/templates/zlodeji/stat.html')
@stringfilter
def count_zlocins(arg):
    tmp = Urobil.objects.filter(prezivka=arg)
    return tmp.count()

register.filter('count_zlocins', count_zlocins)
