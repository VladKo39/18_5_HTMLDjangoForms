from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
from django.views.generic import TemplateView

def games(request):
    games1="Минер"
    games2="Морской бой"
    games3="Русское лото"
    my_games= {'games': [games1,games2,games3]}
    context={'my_games':my_games,}
    return render(request, 'fourth_task/games.html',context)

def bascet(request):
    return render(request, 'fourth_task/cart.html')

def page_main(request):
    return render(request, 'fourth_task/platform.html')

