from django.shortcuts import render
from .models import Recipes
 
# Create your views here.
def index(request):
    return render(request, 'EPR/MainPage.html', {
        "Recipes": Recipes.objects.all()
    })

def add(request):
    return render(request, "EPR/addRecipe.html")

def addRecipe(request):
    ing = request.POST.get('ingredients')
    meth = request.POST.get('method')
    nam = request.POST.get('name')
    o_ref = Recipes(name=nam, method=meth, ingredients=ing)
    o_ref.save()
            
    return render(request, 'EPR/addRecipe.html')  



