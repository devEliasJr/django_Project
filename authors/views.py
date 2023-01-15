from django.shortcuts import render  # noqa


def register_view(request):
    return render(request, 'authors/pages/register_view.html')
