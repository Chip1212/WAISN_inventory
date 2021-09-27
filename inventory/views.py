from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.contrib.auth.decorators import login_required


# Create your views here.

from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login


from .models import Item

from django.urls import reverse

from django.core.mail import send_mail



def index(request):
    item_list = Item.objects.order_by('-Item_quantity')
    
    context = {
        'item_list':item_list,
    }
    
    return render(request, 'inventory/index.html', context)


def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, 'inventory/detail.html', {'item': item})

def new_item(request):
    return render(request, 'inventory/new_item.html')


    

def manage(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    try:
        quantity = request.POST['quantity']
    except (KeyError, Item.DoesNotExist):

        return render(request, 'inventory/detail.html', {
            'item': item,
            'error_message': "You didn't select a choice.",
        })

    else:

        # deletes item
        if request.POST.get("Delete"):
            item.delete()
        else:
            #sets quantity when used hasn't deleted from manage page
            item.Item_quantity = int(quantity)
            item.save()

            #sending email when stock is empty
            if item.is_empty():
                send_mail('Inventory item empty',
                       'The inventory system indicates that your supply of '
                        + item.Item_name + ' is empty. Have a nice day!',
                        'test.email.for.waisn.interview@gmail.com',
                        [request.user.email],
                        fail_silently=False,
                        )

        return HttpResponseRedirect(reverse('inventory:index'))

def create_item(request):
    item = Item(Item_name = request.POST['name'], Item_quantity = int(request.POST['quantity']))
    #item.Item_name = request.POST['name']
    item.Item_quantity = request.POST['quantity']
    if item.Item_name == "":
        return render(request, 'inventory/new_item.html', {
            'error_message': "Name cannot be blank.",
        })

    item.save()
    return HttpResponseRedirect(reverse('inventory:index'))
