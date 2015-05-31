from django import template
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

register = template.Library()

from wotdb_search.models import Character, PointOfView

def character_list(context, characters, page):
    paginator = Paginator(characters, 25)

    try:
        character_list = paginator.page(page)
    except PageNotAnInteger:
        character_list = paginator.page(1)
    except EmptyPage:
        character_list = paginator.page(paginator.num_pages)

    return {
        'is_paginated': True,
        'character_list': character_list
    }
register.inclusion_tag('characters/list.html', takes_context=True)(character_list)

def pov_list(context, character, page):
    povs = PointOfView.objects.all().filter(character_id=character.id).order_by('book__number')
    paginator = Paginator(povs, 10)

    try:
        pov_list = paginator.page(page)
    except PageNotAnInteger:
        pov_list = paginator.page(1)
    except EmptyPage:
        pov_list = paginator.page(paginator.num_pages)

    return {
        'is_paginated': True,
        'pov_list': pov_list
    }
register.inclusion_tag('povs/list.html', takes_context=True)(pov_list)