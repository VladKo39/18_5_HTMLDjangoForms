from django.shortcuts import render

def games(request):
    games1="Минер"
    games2="Морской бой"
    games3="Русское лото"
    context= {
        'games1': games1,
        'games2': games2,
        'games3':games3,
    }
    return render(request, 'third_task/games.html',context)

def bascet(request):
    return render(request, 'third_task/cart.html')

def page_main(request):
    return render(request, 'third_task/platform.html')


