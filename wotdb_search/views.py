from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, HttpRequest
from django.core.urlresolvers import reverse
from django.views import generic
from django.template.loader import get_template
from elasticsearch import Elasticsearch
import json

from .models import Character, Place, Interview, PointOfView, Book, Chapter, Job
# Create your views here.

def search(request):
    query = request.POST['terms']
    es = Elasticsearch()
    res = es.search(index="wotdb_character",doc_type="all", body={
        "query": {
            "bool": {
                "should": [
                    {
                        ## Match specific fields first
                        "multi_match": {
                            "query": query,
                            "boost": 2,
                            "fuzziness": 1,
                            "fields": ["name","channeler_type","clan","sept","gender","society","job"]
                        }
                    },
                    {
                        # Lower the score for description matches -- probably weakest
                        "match": { "description": { "query": query, "boost": 0.1, "fuzziness": 2}}
                    },
                    {
                        ## Everything else gets normal scores
                        "query_string": { "query": query, "default_operator": "OR" }
                    }
                ]
            }
        },
        "fields": ["id", "name", "job", "job_id", "country", "country_id", "city", "city_id"],
        "size": 25,
        "from": 0
    })

    context = {'results': res["hits"]["hits"]}
    print context
    return render(request, 'search/results.html', context)

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

class JobDetail(generic.DetailView):
    model = Job
    template_name = 'jobs/detail.html'

    def get_context_data(self, **kwargs):
        context = super(JobDetail, self).get_context_data(**kwargs)
        page = self.request.GET.get('page')
        context['characters'] = Character.objects.all().filter(job_id=self.kwargs['pk']).extra(order_by=['name'])
        context['page'] = page
        return context

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