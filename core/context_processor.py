# inherit key words same as in views.py
from core.models import Product,Category,CartOrderItems,CartOrder,Vendor,prod_review,ProductImages,wishlist,Address

# def the item you want to inherit/use

def default(request):
    categories =Category.objects.all()

    return{
        # set the context key and value
        'categories':categories

    }