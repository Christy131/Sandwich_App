from django.shortcuts import render
from django.views import View
import random

# Create your views here.

ingredients ={
    'meats': ['turkey', 'veggie burger', 'ham', 'roast beef', 'steak', 'chicken', 'meat ball', 'bacon'],
    'cheeses': ['provolone', 'pepper jack', 'swiss', 'chedder', 'mozzaerella', 'american'],
    'toppings': ['onions', 'tomato', 'lettuce', 'avacado', 'pickles', 'banana peppers', 'olives'],
    'breads': ['white', 'wheat','pretzel', 'sub roll', 'crossiant'],
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
    
        