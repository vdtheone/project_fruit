from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from tools.models import Address, Product,Order,User,Wishlist,Cart
from reportlab.pdfgen import canvas  



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


def profile(request):
    no_of_ord = Order.objects.filter(user=request.user)
    no_of_wished_item = Wishlist.objects.filter(user=request.user)
    print("No of order == ",no_of_ord)
    return render(request,'tools/profile.html',{'no_of_ord':no_of_ord,'no_of_wished_item':no_of_wished_item})


def place_order(request,id):
    if(request.method == "POST"):
        all_address = Address.objects.filter(user = request.user)
        product_name = Product.objects.filter(id=id).first()
        hidden_quantity = request.POST.get('hidden_quantity')
        price = request.POST.get('hidden_price')
    return render(request,'tools/place_order.html',{'product_name':product_name,'hidden_quantity':hidden_quantity,'price':price,'myaddress':all_address})



def order_enrty(request,id):
    if(request.method == "POST"):
        selected_product = Product.objects.get(id=id)
        price = request.POST.get('price')
        quantity = request.POST.get('quantity')
        select_address = request.POST.get('select_address')
        print("select_address ========================== ",select_address)
        add_instance = Address.objects.get(id=select_address)
    
    
        ord = Order.objects.create(address = add_instance,product_id = id,user = request.user, price=int(price),quantity=int(quantity))
        print('------------->>>>>> ',ord)
        ord.save()
    return render(request,'tools/order_place_message.html')



def myaddress(request):
    all_address = Address.objects.filter(user = request.user)
    return render(request,'tools/my_address.html',{'myaddress':all_address})


def myorder(request):
    address = Address.objects.filter(user = request.user)
    myorders = Order.objects.filter(user = request.user)

    test_query = Order.objects.select_related('address').filter(user = request.user)

    return render(request,'tools/my_order.html',{'myorders':myorders,'address':address,'test_query':test_query})


def mywishlist(request):
    my_wishlist = Wishlist.objects.filter(user = request.user)
    return render(request,'tools/my_bucket.html',{'my_wishlist':my_wishlist})

def mysettings(request,id):
    if(request.method == "POST"):
        user = User.objects.get(id = id)
        user.first_name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.city = request.POST.get('city')
        user.zip = request.POST.get('zip')
        user.phone_number = request.POST.get('phone_number')
        print(user.phone_number)
        print("User = ",user)
        user.save()
    else:
        user = User.objects.get(id = id)
    return render(request,'tools/my_setting_edit.html',{'userdetails':user})


def add_new_address(request):
    if (request.method == "POST"):
        print("called============")
        country = request.POST.get('country')
        city = request.POST.get('city')
        street = request.POST.get('street')
        building = request.POST.get('building')
        apartment = request.POST.get('apartment')
        floor = request.POST.get('floor')
        postal_code = request.POST.get('postal_code')

        add_new_address = Address.objects.create(user=request.user,country=country,city=city,street=street,building=building,apartment=apartment,floor=floor,postal_code=postal_code)
        add_new_address.save()
        return redirect('myaddress')
    
    return render(request,'tools/add_new_address.html')


def make_add_default(request,id):
    print(request,id)
    Address.objects.all().update(default_add=False)
    Address.objects.filter(id=id).update(default_add=True)
    return redirect('myaddress')

def edit_address(request,id):
    if(request.method=="POST"):
        print("Called")
        user_address = Address.objects.get(id=id)
        user_address.country = request.POST.get('country')
        user_address.city = request.POST.get('city')
        user_address.street = request.POST.get('street')
        user_address.building = request.POST.get('building')
        user_address.apartment = request.POST.get('apartment')
        user_address.floor = request.POST.get('floor')
        user_address.postal_code = request.POST.get('postal_code')
        user_address.save()
        return redirect('myaddress')
    else:
        myaddress = Address.objects.get(id = id)
    return render(request,'tools/add_new_address.html',{'myaddress':myaddress})



def delete_address(request,id):
    user_address = Address.objects.get(id=id)
    user_address.delete()
    return redirect('myaddress')


def getpdf(request):  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="file.pdf"'  
    p = canvas.Canvas(response)  
    p.setFont("Times-Roman", 55)  
    p.drawString(100,700, "Hello, Javatpoint.")  
    p.showPage()  
    p.save()  
    return response  

def add_to_wishlist(request,id):
    user = User.objects.get(id = request.user.id)
    product = Product.objects.get(id=id)
    add_to_wishlist = Wishlist.objects.create(user=user,product=product)
    add_to_wishlist.save()
    return redirect('product_view',id=id)

def mycart(request):
    products_of_cart = Cart.objects.filter(user = request.user)
    return render(request,'tools/my_bucket.html',{'products_of_cart':products_of_cart})


def delete_wishlist_item(request,id):
    delete_product = Wishlist.objects.get(id=id)
    delete_product.delete()
    return redirect('mywishlist')

def add_to_cart(request,id):
    user = User.objects.get(id = request.user.id)
    product = Product.objects.get(id=id)
    add_to_cart = Cart.objects.create(user=user,product=product)
    add_to_cart.save()
    return redirect('product_view',id=id)

def delete_cartitem(request,id):
    print("====================",id)
    delete_product = Cart.objects.get(id=id)
    delete_product.delete()
    return redirect('mycart')


# User Model Fields
# city, date_joined, email, first_name, groups, id, is_active, is_staff, is_superuser, last_login, last_name, logentry, order, password, phone_number, user_permissions, username, zip
        
