from django.shortcuts import render
from blog.models import Item

#def post_list(request):
#    return render(request, 'blog/index.html', {})
                  
def shoppinglist(request):
    return render(request, 'blog/shoppinglist.html', {'shoppinglist': Item.objects.all()})

#def toggleItem(request):
#    if request.methord == 'GET':
#        itemname = request.GET.get('itemname-input')
#        number = request.GET.get('number-input')
#        if (Item.objects.contains(itemname, number) == False):
#            Item.objects.update(itemname, number)
#            print(f"Added '{itemname} ({number})' to the shoppinglist!'")
#        elif (Item.objects.contains(itemname, number) == True):
#            del Item.objects.get(itemname, number)
#            print(f"Removed '{itemname} ({number})' to the shoppinglist!'")
