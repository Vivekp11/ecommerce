from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from cart.models import Cart, CartItem




# Create your views here.
# def prodDetail(request):
#
#     return render(request, 'cart.html')
def cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart
def prodDetail(request, total=0, counter=0, cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=cart_id(request))
        cart_items= CartItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            total = cart_item.sub_total
            counter += cart_item.quantity

    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))