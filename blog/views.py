from django.shortcuts import render
from blog.models import Item

#def post_list(request):
#    return render(request, 'blog/index.html', {})
                  
def shoppinglist(request):
    return render(request, 'blog/shoppinglist.html', {'shoppinglist': Item.objects.all()})