from django import template
from django.template.defaultfilters import stringfilter
from django.db.models import Sum
from collections import Counter
from zlodeji.models import *

register = template.Library()


@register.filter
@register.inclusion_tag('zlodejs/stat.html')
@stringfilter
def count_zlocins(arg):
    tmp = Urobil.objects.filter(prezivka=arg)
    return tmp.count()


register.filter('count_zlocins', count_zlocins)


@register.filter
@register.inclusion_tag('zlodejs/stat.html')
@stringfilter
def count_skolenia(arg):
    tmp = BolNa.objects.filter(prezivka=arg)
    return tmp.count()


register.filter('count_skolenia', count_skolenia)


@register.filter
@register.inclusion_tag('zlodejs/stat.html')
@stringfilter
def count_vybavenie(arg):
    tmp = Vlastnil.objects.filter(prezivka=arg)
    return tmp.count()


register.filter('count_vybavenie', count_vybavenie)


@register.filter
@register.inclusion_tag('zlodejs/stat.html')
@stringfilter
def count_povolenia(arg):
    tmp = Dostal.objects.filter(prezivka=arg)
    return tmp.count()


register.filter('count_povolenia', count_povolenia)


@register.filter
@register.inclusion_tag('zlodejs/index.html')
@stringfilter
def sum_korist(arg):
    total = 0
    for tmp in Urobil.objects.filter(prezivka=arg):
        total += tmp.id_zlocinu.hodnota_korist
    return total


register.filter('sum_korist', sum_korist)


@register.filter(name='sum_koristi')
@register.simple_tag
@stringfilter
def sum_koristi(*args, **kwargs):
    list_zlodejov = {}
    for x in Urobil.objects.all():
        if x.prezivka.prezivka not in list_zlodejov:
            list_zlodejov[x.prezivka.prezivka] = x.id_zlocinu.hodnota_korist
        else:
            list_zlodejov[x.prezivka.prezivka] += x.id_zlocinu.hodnota_korist
    return dict(Counter(list_zlodejov).most_common(10))


register.filter('sum_koristi', sum_koristi)\


@register.filter(name='sum_zlocinov')
@register.simple_tag
@stringfilter
def sum_zlocinov(*args, **kwargs):
    list_zlodejov = {}
    for x in Urobil.objects.all():
        if x.prezivka.prezivka not in list_zlodejov:
            list_zlodejov[x.prezivka.prezivka] = 1
        else:
            list_zlodejov[x.prezivka.prezivka] += 1
    return dict(Counter(list_zlodejov).most_common(10))


register.filter('sum_zlocinov', sum_zlocinov)
