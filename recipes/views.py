from django.contrib import messages
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render  # noqa

from utils.recipes.factory import make_recipe

from .models import Recipe


def home(request):
    recipes = Recipe.objects.all().filter(
        is_published=True
    ).order_by('-id')

    messages.success(request, 'Epa, você foi pesquisar algo que eu vi.')
    messages.error(request, 'Epa, você foi pesquisar algo que eu vi.')
    messages.warning(request, 'Epa, você foi pesquisar algo que eu vi.')

    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })


def category(request, category_id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True
        ).order_by('-id')
    )

    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category '
    })


def recipe(request, id):
    recipe = Recipe.objects.filter(
        pk=id,
        is_published=True
    ).order_by('-id').first()

    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })


def search(request):
    search_term = request.GET.get('q', '').strip()

    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True
    ).order_by('-id')

    return render(request, 'recipes/pages/search.html', context={
        'page_title': f'Search for "{search_term}"',
        'recipes': recipes,
    })


def teste(request, id):

    return render(request, 'recipes/pages/teste.html', context={
        'teste': make_recipe(),
    })
