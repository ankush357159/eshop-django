from urllib import request
from django.http import HttpResponse
from django.views import View
from django.shortcuts import redirect, render
from store.models import Category, Product



# print(make_password('acsd'))
# print(check_password( 'acsd','pbkdf2_sha256$320000$Q3vXmHVDphBTXh2yomyPBW$qG0DX9WDyLwkPVDIGXxcy3F6D9LARP/FOZ2WId/gniE='))

class Index(View):
    def post(self, request):
        product = request.POST.get('product')
        remove = request.POST.get('remove')
        print('Product: ',product)
        cart = request.session.get('cart')
        print('Cart: ',cart)
        if cart:
            quantity = cart.get(product)
            if quantity:
                if remove:
                    if quantity<=1:
                        cart.pop(product)
                    else:
                        cart[product]  = quantity-1
                else:
                    cart[product]  = quantity+1

            else:
                cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        # print(product)
        # print(request.session)
        print('Cart Items: ',cart)
        return redirect('homepage')




    def get(self, request):

        cart = request.session.get('cart')
        if not cart:
            request.session['cart'] = {}
        # print('Session: ', request.session)
        products = None
        # request.session.get('cart').clear()
        categories = Category.get_all_categories()
        categoryId = request.GET.get('category')
        if categoryId:
            products = Product.get_all_products_by_categoryId(categoryId)
            
        else:
            products = Product.get_all_produdcts()
        
        data = {}
        data['products'] = products
        data['categories'] = categories
        # print(data['products'])
        # print('You are: ', request.session.get('email'))
        return render(request, 'index.html', data)






    

        





       


       

    

