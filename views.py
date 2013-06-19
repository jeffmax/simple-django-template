from django import forms
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def main(request):
    return render_to_response('index.html')
