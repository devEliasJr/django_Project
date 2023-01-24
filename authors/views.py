from django.contrib import messages
from django.http import Http404
from django.shortcuts import redirect, render  # noqa

from .forms import RegisterForm


def register_view(request):
    register_form_data = request.session.get('register_form_data', None)
    form = RegisterForm(register_form_data)
    return render(request, 'authors/pages/register_view.html', context={
        'form': form
    })


def register_create(request):
    if not request.POST:
        raise Http404()

    POST = request.POST
    request.session['register_form_data'] = POST
    form = RegisterForm(request.POST)

    if form.is_valid():
        form.save()
        messages.success(
            request, 'Cadastro realizado com sucesso, por favor efetue o login.')  # noqa

        del (request.session['register_form_data'])

    return redirect('authors:register')
