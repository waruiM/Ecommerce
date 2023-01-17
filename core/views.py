
from django.http import HttpResponse
from django.shortcuts import render

from core.models import Product,Category,CartOrderItems,CartOrder,Vendor,prod_review,ProductImages,wishlist,Address

# Create your views here.
def index(request):
    # get the object in the Product model
    #-id arrange items based on the id 

    #### getting all the products from the db
    # shop_prod= Product.objects.all()

    ### pplying filter to the db
    # categories=Category.objects.all()
    shop_prod=Product.objects.filter(product_status="published")
    
    context={
        #  setting the key and value
        "prod":shop_prod,
        # "cat":categories
    }
    return render(request,'core/index.html',context)


#####creating product view

def product_list_view(request):
    shop_prod=Product.objects.filter(product_status="published")
    
    context={
        "prod":shop_prod
        
    }
    return render (request,'core/product-list.html',context)

#####creating categories view
def categories_view(request):
    categories=Category.objects.all()
    
    context={
        "categories":categories

    }
    return render (request,'core/categories.html',context)

#####listing the products appearing on a given category
##getting the specific category  id-catid
def category_product_list_view(request,catid):
    category=Category.objects.get(cid=catid)
    products=Product.objects.filter(product_status="published",category=category)

    context ={
        "category":category,
        "products":products
    }
    return render(request,"core/category-product-list.html",context)

# creating the vendor view
def vender_view(request):
    vendor=Vendor.objects.all()

    context={
        'vendor':vendor,
    }
    return render(request,'core/vendor-list.html',context)
