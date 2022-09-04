from django.shortcuts import render, reverse
from django.http import HttpResponse


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def home_view(request):
    pages = {
        #'Главная страница': reverse('home')
    }

    for rec in DATA:
        pages[rec] = 'spisok_ingr/' + rec + '/?servings=1'

    context = {
        'pages': pages
    }
    return render(request, 'calculator/home.html', context)

def spisok_ingr(request, op1):
    ingr_name = op1
    try:
        ingr_count = int(request.GET.get('servings', 1))
    except:
        ingr_count = 1
    context = {}
    if ingr_name in DATA:
        context['recipe'] = {}
        for ingr in DATA[ingr_name]:
         context['recipe'][ingr]= DATA[ingr_name][ingr] * ingr_count
    return render(request, 'calculator/index.html', context)


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
