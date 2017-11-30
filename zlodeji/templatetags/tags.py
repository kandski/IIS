from django import template
from django.template.defaultfilters import stringfilter

from zlodeji.models import *

register = template.Library()


@register.filter
@register.inclusion_tag('zlodeji/templates/zlodeji/stat.html')
@stringfilter
def count_zlocins(arg):
    tmp = Urobil.objects.filter(prezivka=arg)
    return tmp.count()

register.filter('count_zlocins', count_zlocins)

@register.filter
@register.inclusion_tag('zlodeji/templates/zlodeji/stat.html')
@stringfilter
def count_skolenia(arg):
    tmp = BolNa.objects.filter(prezivka=arg)
    return tmp.count()

register.filter('count_skolenia', count_skolenia)

@register.filter
@register.inclusion_tag('zlodeji/templates/zlodeji/stat.html')
@stringfilter
def count_vybavenie(arg):
    tmp = Vlastnil.objects.filter(prezivka=arg)
    return tmp.count()

register.filter('count_vybavenie', count_vybavenie)\

@register.filter
@register.inclusion_tag('zlodeji/templates/zlodeji/stat.html')
@stringfilter
def count_povolenia(arg):
    tmp = Dostal.objects.filter(prezivka=arg)
    return tmp.count()

register.filter('count_povolenia', count_povolenia)