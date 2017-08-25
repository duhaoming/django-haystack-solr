#!/usr/bin/env python
# encoding: utf-8

from models import Indexes

from haystack import indexes


# More typical usage involves creating a subclassed `SearchIndex`. This will
# provide more control over how data is indexed, generally resulting in better
# search.
class IndexesIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    url = indexes.CharField(model_attr='url')
    title = indexes.CharField(model_attr='title')
    content = indexes.CharField(model_attr='content')
    type = indexes.CharField(model_attr='type')

    def get_model(self):
        return Indexes

    def index_queryset(self, using=None):
        return self.get_model().objects.filter(public=True)
