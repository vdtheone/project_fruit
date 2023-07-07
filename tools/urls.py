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
    path('profile/',views.profile,name='profile'),
    path('place_order/<id>/',views.place_order,name='place_order'),
    path('order_enrty/<id>/',views.order_enrty,name='order_enrty'),
    path('myaddress/',views.myaddress,name='myaddress'),
    path('myorder/',views.myorder,name='myorder'),
    path('mywishlist/',views.mywishlist,name='mywishlist'),
    path('mysettings/<id>/',views.mysettings,name='mysettings'),
    path('add_new_address/',views.add_new_address,name='add_new_address'),
    path('make_add_default/<id>/',views.make_add_default,name='make_add_default'),
    path('edit_address/<id>/',views.edit_address,name='edit_address'),
    path('delete_address/<id>/',views.delete_address,name='delete_address'),
    path('pdf',views.getpdf),
    path('add_to_wishlist/<id>/',views.add_to_wishlist,name='add_to_wishlist'),
    path('mycart/',views.mycart,name='mycart'),
    path('delete_wishlist_item/<id>/',views.delete_wishlist_item,name='delete_wishlist_item'),
    path('add_to_cart/<id>/',views.add_to_cart,name='add_to_cart'),
    path('delete_cartitem/<id>/',views.delete_cartitem,name='delete_cartitem'),

]

