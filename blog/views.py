from django.shortcuts import render
from blog.models import Item

#def post_list(request):
#    return render(request, 'blog/index.html', {})
                  
def shoppinglist(request):
    return render(request, 'blog/shoppinglist.html', {'shoppinglist': Item.objects.all()})

def addItem(request):
    print("called 1")
    if request.methord == 'GET':
        print("called 2")
        itemname = request.GET.get('itemname-input')
        number = request.GET.get('number-input')
        print("Doing...")
        Item.objects.update(itemname, number)
        print("Done!")