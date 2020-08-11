from django.shortcuts import render, redirect
from django.http import HttpResponse

import datetime
# Create your views here.
def home(request):
    hour = datetime.datetime.now().strftime('%d %b, %Y - %H:%M:%S')
    ctx = {'hour': hour}
    return render(request, 'base/base.html', ctx)