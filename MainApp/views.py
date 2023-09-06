from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.
def home(request):
    '''
    text = """
            <h1>"Изучаем django"</h1>
            <strong>Автор</strong>: <i>Иванов И.И.</i>
            """
    return HttpResponse(text)
    '''
    context = {
        'name': 'Петров Иван Николаевич',
        'email': 'petrovin@gmail.com',
        'page_name': 'home'
    }
    return render(request, 'index.html', context)

def about(request):
    text = """
            <title> About </title>
            <header>
                / <a href='/'>Home</a> / <a href='/items/'>Items</a> / <a href='/about/'>About</a> /
            </header>
            <strong>Имя</strong>: <i>Иван</i><br>
            <strong>Отчество</strong>: <i>Иванович</i><br>
            <strong>Фамилия</strong>: <i>Иванов</i><br>
            <strong>телефон</strong>: <i>8-923-600-01-02</i><br>
            <strong>email</strong>: <i>ivanovii@gmail.com</i>
            """

    return HttpResponse(text)



'''
items = [
        {"id": 1, "name": "Кроссовки abibas", "quantity": 5},
        {"id": 2, "name": "Куртка кожаная", "quantity": 2},
        {"id": 5, "name": "Coca-cola 1 литр", "quantity": 12},
        {"id": 7, "name": "Картофель фри", "quantity": 0},
        {"id": 8, "name": "Кепка", "quantity": 124},
        ]
'''

def items_list(request):
    items = Item.objects.all()
    context = {'items': items,
               'page_name': 'items_list'}
    return render(request, 'items_list.html', context)

    '''
    response = "<h1>Список товаров:</h1>"
    response += "<ol>"
    for item in items:
        response += f"<li><a href='/item/{item['id']}/'>{item['name']}</a></li>"
    response += "</ol>"
    
    return HttpResponse(response)
    '''



def item_info(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
        context = {'item': item,
                   'page_name': 'item_info'}
        return render(request, 'item_info.html', context)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f'Товар c id={item_id} не найден')

    '''
    for item in items:
        if item["id"] == item_id:
            context = {'item': item}
            return render(request, 'item_info.html', context)
    return HttpResponseNotFound(f'Товар c id={item_id} не найден')
    '''
    '''
    for item in items:
        if item["id"] == item_id:
            found_item = item
            break
        else:
            found_item = None
    
    if found_item:
        response = f"""
                    <h1>Информация о товаре с id={item_id}</h1>
                    <p>Название: {found_item['name']}</p>
                    <p>Количество: {found_item['quantity']}</p>
                    <a href='/items/'> Назад к списку товаров </a>
                    """ 
    else:
        response = f"""
                    <h1>Товар c id={item_id} не найден</h1>
                    <a href='/items/'> Назад к списку товаров </a>
                    """
    
    return HttpResponse(response)
    '''

