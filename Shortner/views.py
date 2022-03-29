from django.shortcuts import render
from django.contrib import messages
from django.utils.safestring import mark_safe
from rest_framework.response import Response
from . models import URLData
from . forms import URLDataForm
from . serializers import URLDataSerializers
from django.shortcuts import redirect
import string
import random
from decouple import config

from newspaper import Article
from PIL import Image
import requests

#Declare Key Varaibles
BASE_LIST='0123456789abcdefghijklmnopqrstuvwxyz./:'
BASE_DICT=dict((c,idx) for idx,c in enumerate(BASE_LIST))
host = config('host')
port = config('port')

def appendPrefix(entry):
    match=['http','https']
    if any(x in entry for x in match):
        return entry
    else:
        return('https://'+str(entry))

global url_text

def get_form(request):
    if request.method=='POST':
        form=URLDataForm(request.POST)
        if form.is_valid():
            fullurl=form.cleaned_data['EnterURL']
            fullurladj=appendPrefix(fullurl)

            article=Article(fullurladj)
            article.download()
            article.parse()

            messages.info(request, mark_safe('{}'.format(article.text)))
            images = []
            for img in article.images:
                images.append(Image.open(requests.get(img, stream = True).raw))
            form=URLDataForm()
            return render(request, 'myform/form.html', {'form':form})
    form=URLDataForm()
    return render(request, 'myform/form.html', {'form':form})

