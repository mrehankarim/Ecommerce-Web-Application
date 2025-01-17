from django.urls import path

from . import views
urlpatterns = [
    path("",views.index,name="shopHome"),
    path("about",views.about,name="aboutUs"),
    path("contact",views.contact,name="contactUs"),
    path("tracker",views.tracker,name="trackingStatus"),
    path("productView",views.productView,name="productView"),
    path("search",views.search,name="search"),
    path("checkout",views.checkout,name="checkout")
    
]
