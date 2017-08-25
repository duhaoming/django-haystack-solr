from django.shortcuts import render

# Create your views here.

from datetime import date

from haystack.generic_views import SearchView
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from forms import SearchForm
from haystack.query import SearchQuerySet

from models import Indexes

#@api_view(('GET',))
#@permission_classes((AllowAny,))
#def api_root(request, format=None):
#    api_root = {}
#    api_root['index'] = reverse('search_view', request=request)
#    return Response(api_root)


def indexes_search(request):
    form = SearchForm()
    if 'q' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            cd = form.cleaned_data
            results = SearchQuerySet().models(Indexes).filter(content=cd['q']).load_all()
            for i in results:
                print dir(i.objects)
            total_results = results.count()
    else:
        cd = {}
        results = []
        total_results = []
    return render(request,
            'search.html',
            {'form': form,
             'cd': cd,
             'results': results,
             'total_results': total_results})
