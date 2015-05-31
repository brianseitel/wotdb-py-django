from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpRequest
from django.core.urlresolvers import reverse
from django.views import generic
from django.template.loader import get_template

from .models import Character, Place, Interview, PointOfView, Book, Chapter
# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'characters/index.html'

    def get_context_data(self, **kwargs):
        context               = super(IndexView, self).get_context_data(**kwargs)
        context['characters'] = Character.objects.all().extra(order_by=['name'])
        context['page']       = self.request.GET.get('page')
        return context

class BookIndex(generic.ListView):
    template_name = 'books/index.html'
    context_object_name = 'chapters_list'
    paginate_by = 25

    def get_queryset(interviews):
        return Book.objects.all()

class BookView(generic.DetailView):
    model = Book
    template_name = 'books/detail.html'


class ChapterView(generic.DetailView):
    model = Chapter
    template_name = 'chapters/index.html'

class CharacterList(generic.ListView):
    template_name = 'characters/list.html'
    context_object_name = 'character_list'
    paginate_by = 25

    def get_queryset(character_list):
        return Character.objects.all() 

    def get_context_data(self, **kwargs):
        context = super(CharacterList, self).get_context_data(**kwargs)
        context['request'] = self.request
        return context

class CharacterView(generic.DetailView):
    model = Character
    template_name = 'characters/detail.html'

    def get_context_data(self, **kwargs):
        context = super(CharacterView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page')
        context['page'] = page
        return context

class InterviewList(generic.ListView):
    template_name = 'interviews/index.html'
    context_object_name = 'interviews'
    paginate_by = 25

    def get_queryset(interviews):
        return Interview.objects.all()

class InterviewDetail(generic.DetailView):
    model = Interview
    template_name = 'interviews/detail.html'

class PointOfViewList(generic.ListView):
    template_name = 'povs/index.html'
    context_object_name = 'books_list'
    paginate_by = 25

    def get_queryset(interviews):
        return Book.objects.all()

class PointOfViewDetail(generic.DetailView):
    model = PointOfView
    template_name = 'povs/detail.html'


class PlacesIndexView(generic.ListView):
    template_name = 'places/index.html'
    context_object_name = 'places_list'
    paginate_by = 25

    def get_queryset(places_list):
        return Place.objects.all()

class PlaceView(generic.DetailView):
    model = Place
    template_name = 'places/detail.html'

    def get_context_data(self, **kwargs):
        context = super(PlaceView, self).get_context_data(**kwargs)
        page = self.request.GET.get('page')
        context['character_list'] = CharacterList.as_view()
        context['page'] = page
        return context