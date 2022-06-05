from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from django.views import View

from store.models.customer import Customer



class Login(View):
    def get(self, request):
        if request.method == 'GET':
            return render(request, 'login.html') 

    def post(self, request):
        email = request.POST.get('email')    
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        print(repr(customer))
        print(email, password)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                request.session['email'] = customer.email
                return redirect('homepage')
            else:
                error_message = "Email or Password is invalid!!"
        else:
            error_message = "Email or Password is invalid!!"
        return render(request, 'login.html', {'error': error_message}) 

def logout(request):
    request.session.clear()
    return redirect('login')