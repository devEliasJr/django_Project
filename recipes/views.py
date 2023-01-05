from django.http import HttpResponse


def home(request):
    return HttpResponse('Home')


def contato(request):
    return HttpResponse('contato')


def sobre(request):
    return HttpResponse('sobre')
