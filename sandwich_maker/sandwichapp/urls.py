from django.urls import path
from sandwichapp.views import SandwichappView, IngredientsView, SandwichesView

urlpatterns = [path('', SandwichappView.as_view(), name='sandwich'),
    path('ingredients/<str:ingredient_type>', IngredientsView.as_view(), name='ingredients_list'),
    path('random/', SandwichesView.as_view(), name='sandwich_random')]