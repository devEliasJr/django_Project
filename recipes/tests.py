from django.test import TestCase
from django.urls import resolve, reverse

from recipes import views


class RecipeURLsTest(TestCase):

    def test_recipe_home_url_is_correct(self):
        url = reverse('recipes:home')
        self.assertEqual(url, '/')

    def test_recipe_category_url_is_correct(self):
        url = reverse('recipes:category', kwargs={'category_id': 1})
        self.assertEqual(url, '/recipes/category/1/')

    def test_recipe_detail_url_is_correct(self):
        url = reverse('recipes:recipe', kwargs={'id': 1})
        self.assertEqual(url, '/recipes/1/')

    def test_recipe_search_url_is_correct(self):
        url = reverse('recipes:search')
        self.assertEqual(url, '/recipes/search/')


class RecipeViewsTest(TestCase):

    def test_recipe_home_views_is_function_correct(self):
        view = resolve(reverse('recipes:home'))
        self.assertTrue(True)
        self.assertIs(view.func, views.home)

    def test_recipe_category_views_is_function_correct(self):
        view = resolve(reverse('recipes:category', kwargs={'category_id': 1}))
        self.assertTrue(True)
        self.assertIs(view.func, views.category)

    def test_recipe_recipe_views_is_correct(self):
        view = resolve(reverse('recipes:recipe', kwargs={'id': 1}))
        self.assertTrue(True)
        self.assertIs(view.func, views.recipe)

    def test_recipe_search_views_is_correct(self):
        view = resolve(reverse('recipes:search'))
        self.assertTrue(True)
        self.assertIs(view.func, views.search)


class RecipeTemplateTest(TestCase):

    def test_recipe_search_loads_correct_template(self):
        response = self.client.get(reverse('recipes:search') + '?q=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_recipe_search_raise_404_if_no_search_term(self):
        response = self.client.get(reverse('recipes:search'))
        self.assertEqual(response.status_code, 404)

    def test_recipe_search_term_is_on_page_title_and_escaped(self):
        url = reverse('recipes:search') + '?q=Teste'
        response = self.client.get(url)
        self.assertIn(
            'Search for &quot;Teste&quot;',
            response.content.decode('utf-8')
        )
