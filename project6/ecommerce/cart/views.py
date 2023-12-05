from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from ecomapp.models import product
from . models import Cart, CartItem
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.
def cart_id(request):
    cart=request.session.session_key
    if not cart:
        cart=request.session.create()
    return cart

def add_cart(request, product_id):
    prod = product.objects.get(id=product_id)
    try:
        cart=Cart.objects.get(cart_id=cart_id(request))
    except Cart.DoesNotExist:
        cart= Cart.objects.create(cart_id=cart_id(request))
        cart.save(),
    try:
        cart_item=CartItem.objects.get(prod=prod, cart=cart)
        if cart_item.quantity < cart_item.prod.stock:
            cart_item.quantity += 1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            prod=prod,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')
def cart_detail(request, total=0, counter=0, cart_items=None):
    try:
        cart=Cart.objects.get(cart_id=cart_id(request))
        cart_items= CartItem.objects.filter(cart=cart,active=True)
        for cart_item in cart_items:
            # total += cart_item.sub_total
            total += (cart_item.quantity * cart_item.prod.price)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(request, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))


def delete_item(request, item_id):
    cart = Cart.objects.get(cart_id=cart_id(request))
    prod = get_object_or_404(product, id=item_id)
    cart_item = CartItem.objects.get(prod=prod, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')
    # # Get the cart by its identifier or return a 404 error if it doesn't exist
    # CartItem.objects.get(prod=item_id).delete()
    # # cart.delete()
    # return render(request, 'cart.html')
def cart_remove(request,product_id):
    cart = Cart.objects.get(cart_id=cart_id(request))
    prod=get_object_or_404(product,id=product_id)
    cart_item=CartItem.objects.get(prod=prod,cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect('cart:cart_detail')