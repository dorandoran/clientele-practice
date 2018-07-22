#python function that does the "hard work"

from django.http import HttpResponse
from django.shortcuts import render

def list_clientele(request):
    return HttpResponse('Hello World')

def do_calc(value1, value2):
    return value1 * value2

def test_function(request):
    tot = do_calc(10, 2)
    dude_flag = False
    people = ['Gregory', 'Mary', 'Jose', 'Jimbo', 'Other Guy']
    return render(request, 'example.html', { 'total': tot, 'people': people, 'dude_flag': dude_flag })

def special_case_2003(request):
    return HttpResponse('Special Case 2003')

def special_case(request, year):
    return HttpResponse('Return articles from %s ' % year)

def month_archive(request, year, month):
    return HttpResponse('Return articles from %s, %s ' % (year, month))

def hello(request, name):
    return HttpResponse('Hello %s' % name)