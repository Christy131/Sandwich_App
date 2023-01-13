from django.shortcuts import render
from django.views import View
import random

# Create your views here.

ingredients ={
    'meats': ['turkey', 'veggie burger', 'ham', 'roast beef', 'steak', 'chicken', 'meat ball', 'bacon'],
    'cheeses': ['provolone', 'pepper jack', 'swiss', 'chedder', 'mozzaerella', 'american', 'colby', 'gouda'],
    'toppings': ['onions', 'tomato', 'lettuce', 'avacado', 'pickles', 'banana peppers', 'olives', 'mayo'],
    'breads': ['white', 'wheat','pretzel', 'sub roll', 'crossiant', 'multi-grain', 'tortilla', 'pocket bread'],
}

class SandwichappView(View):
    def get(self, request):
        return render(
            request = request,
            template_name = 'sandwichapp.html',
            context = {'ingredients': ingredients.keys()})
            
class IngredientsView(View):
    def get(self, request, ingredient_type):
        return render (
            request=request,
            template_name='Ingredients_list.html',
            context={
                'ingredients': ingredients[ingredient_type],
                'ingredient_type':ingredient_type
            }
        )

class SandwichesView(View):
    def get(self, request):
        meats=ingredients['meats']
        meat=random.choice(meats)
        cheeses=ingredients['cheeses']
        cheese=random.choice(cheeses)
        toppings=ingredients['toppings']
        topping=random.choice(toppings)
        breads=ingredients['breads']
        bread=random.choice(breads)
        return render(
        request=request,
        template_name='sandwich_random.html', 
        context={
            'meat': meat,
            'cheese': cheese,
            'topping': topping,
            'bread': bread
             } 
        ) 
class MenuView(View):    
    def get(self, request):
        return render(
            request, 
            "menu.html",
            context={
                "meats": ingredients["meats"],
                "cheeses": ingredients["cheeses"],
                "toppings": ingredients["toppings"],
            }
        )  