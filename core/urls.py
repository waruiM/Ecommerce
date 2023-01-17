from django.urls import path
from core.views import index,product_list_view,categories_view,category_product_list_view,vender_view


## setting up the url paths for the 
app_name="core"

urlpatterns = [
    #creating a custom url path
    #path("main/",index)

        ########## products ##########

    path("", index, name="index"),
    path("products/",product_list_view, name="product-list"),

        ########## categories ##########

    path("categories/",categories_view, name="category-list"),
    # the url for the category selected
    path("categories/<catid>/",category_product_list_view, name="category-product-list"),
    # the vendor list url

        ########## vendors ##########


    path("vendors/",vender_view, name="vender-view"),


]
