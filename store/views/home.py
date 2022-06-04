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
        cart = request.session.get('cart')
        if cart:
            cart[product] = 1
        else:
            cart = {}
            cart[product] = 1

        request.session['cart'] = cart
        # print(product)
        return redirect('homepage')




    def get(self, request):
        products = None
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






    

        





       


       

    

