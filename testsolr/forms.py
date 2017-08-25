#!/usr/bin/env python
# encoding: utf-8

from django import forms


class SearchForm(forms.Form):
    q = forms.CharField()
