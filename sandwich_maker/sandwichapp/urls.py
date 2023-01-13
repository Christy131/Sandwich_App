from django.urls import path
from sandwichapp.views import SandwichappView, IngredientsView, SandwichesView, MenuView

urlpatterns = [path('', SandwichappView.as_view(), name='sandwich'),
    path('ingredients/<str:ingredient_type>', IngredientsView.as_view(), name='ingredients_list'),
    path('random/', SandwichesView.as_view(), name='sandwich_random'),
    path('menu/', MenuView.as_view(), name='menu')]