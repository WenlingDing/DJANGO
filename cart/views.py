from django.shortcuts import render, get_object_or_404, redirect
from tracker_app.models import Feature
from tracker_app.views import feature
from .forms import AddToCartForm
# Create your views here.

def add_to_cart(request, id):
    post = get_object_or_404(Feature, pk=id)
    cart = request.session.get('cart', {})
    
    add_to_cart_form = AddToCartForm(request.POST)
    qty = add_to_cart_form['qty']
    

    # if the user has not addd the product to the cart
    # initialize it and set its qty to 1
    if id not in cart:
        cart[id] = {
            'product': {
              'id': id,
              'title': post.title,
              'price': 100
            },
            'qty': int(qty.value())
        }
    else:
        # if the product already exists in the cart, increment its qty by 1
        cart[id]['qty'] = cart[id]['qty'] +  int(qty.value())
    
    request.session['cart'] = cart
    
    return redirect(feature)
    
def view_cart(request):
    cart = request.session.get('cart', {})
    print(cart)
    return render(request, 'view_cart.html', {
        'cart':cart
    })
    
def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    del cart[id]
    request.session['cart'] = cart
    return redirect(view_cart)
    
def remove_all_from_cart(request):
    request.session['cart'] = {}
    return redirect(feature)