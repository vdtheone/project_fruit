from django.urls import path
from . import views

urlpatterns = [
    path('login/',views.login_process, name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout_user,name='logout'),
    path('home/',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('our_fruits/',views.our_fruits,name='our_fruits'),
    path('testimonial/',views.testimonial,name='testimonial'),
    path('contact_us/',views.contact_us,name='contact_us'),
    path('product_view/<id>/',views.product_view,name='product_view'),
    path('profile/<id>/',views.profile,name='profile'),
    path('place_order/<id>/',views.place_order,name='place_order'),
    path('order_enrty/<id>/',views.order_enrty,name='order_enrty'),
    path('myaddress/<id>/',views.myaddress,name='myaddress'),
    path('myorder/<id>/',views.myorder,name='myorder'),
    path('mywishlist/<id>/',views.mywishlist,name='mywishlist'),
    path('mysettings/<id>/',views.mysettings,name='mysettings'),

]

