from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from tools.models import Product,Order,User



# Create your views here.

def login_process(request):
    if(request.method == "POST"):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username).first()
        if user:
            if user.check_password(password):
                login(request, user)
                return redirect('/tools/home/')
            else:
                return HttpResponse("wrong password")
        return HttpResponse("wrong username")
    return render(request,'tools/login.html')


def signup(request):
    if(request.method == "POST"):
        first_name = request.POST.get('name')
        password = request.POST.get('password')
        username = request.POST.get('username')
        email = request.POST.get('email')

        city = request.POST.get('city')
        zip = request.POST.get('zip')
        phone_number = request.POST.get('phone')

        create_new_user = User.objects.create(first_name=first_name, username=username,email=email,phone_number=phone_number,city=city,zip=zip)
        
        create_new_user.set_password(password)
        create_new_user.save()
        print("=======================================",create_new_user)
        return render(request,'tools/login.html')
    return render(request,'tools/registration.html')


def home(request):
    products = Product.objects.all()
    return render(request,'tools/home.html',{'products':products})


def logout_user(request):
    logout(request)
    return redirect('/tools/home/')


def about(request):
    return render(request,'tools/about.html')


def our_fruits(request):
    products = Product.objects.all()
    return render(request,'tools/fruit.html',{'products':products})


def testimonial(request):
    return render(request,'tools/testimonial.html')


def contact_us(request):
    return render(request,'tools/contact.html')


def product_view(request,id):
    product = Product.objects.filter(id=id).first()
    return render(request,'tools/product_view.html',{'product':product})


def profile(request,id):
    no_of_ord = Order.objects.filter(user=request.user)
    print("No of order == ",no_of_ord)
    return render(request,'tools/profile.html',{'no_of_ord':no_of_ord})


def place_order(request,id):
    if(request.method == "POST"):
        product_name = Product.objects.filter(id=id).first()
        hidden_quantity = request.POST.get('hidden_quantity')
        price = request.POST.get('hidden_price')
        print(product_name)
        # print(price)
        # print(hidden_quantity)
        # print(request.POST)
        # details = {
        #     'product_name':product_name,
        #     'price':price,
        #     'hidden_quantity':hidden_quantity,
        #     'id':id
        # }
    return render(request,'tools/place_order.html',{'product_name':product_name,'hidden_quantity':hidden_quantity,'price':price})



def order_enrty(request,id):
    if(request.method == "POST"):
        selected_product = Product.objects.get(id=id)
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')

        print('========================================',request.user)
        print(price)
        print(selected_product)
        print(request)
    
        ord = Order.objects.create(product_id = id,user = request.user, price=int(price),quantity=int(quantity))
        print('------------->>>>>> ',ord)
        ord.save()
    return render(request,'tools/order_place_message.html')



def myaddress(request,id):
    return render(request,'tools/my_address.html')


def myorder(request,id):
    return render(request,'tools/my_order.html')


def mywishlist(request,id):
    return render(request,'tools/my_bucket.html')

def mysettings(request,id):
    return render(request,'tools/my_setting_edit.html')



        
