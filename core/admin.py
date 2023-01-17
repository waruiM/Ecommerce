from django.contrib import admin

#importing the models
from core.models import Product,Category,CartOrderItems,CartOrder,Vendor,prod_review,ProductImages,wishlist,Address

# Register your models here.
class ProductImagesAdmin(admin.TabularInline):
    model=ProductImages

class ProductAdmin(admin.ModelAdmin):
    inlines=[ProductImagesAdmin]
    list_display=['user','title','product_image','price','category','vendor','featured','date','product_status']

class CategoryAdmin(admin.ModelAdmin):
    list_display=['title','category_image']

class VendorAdmin(admin.ModelAdmin):
    list_display=['title','vendor_image','phone']

class CartOrderAdmin(admin.ModelAdmin):
    list_display=['user','price','paid_status','order_status','order_date']

class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display=['order','invoice_no','order_image','item','quantity','price','total']

class prod_reviewAdmin(admin.ModelAdmin):
    list_display=['user','product','review','rating','date']

class WishlistAdmin(admin.ModelAdmin):
    list_display=['user','product']

class AddressAdmin(admin.ModelAdmin):
    list_display=['user','email','status','address']

admin.site.register(Product,ProductAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Vendor,VendorAdmin)
admin.site.register(CartOrder,CartOrderAdmin)
admin.site.register(CartOrderItems,CartOrderItemsAdmin)
admin.site.register(prod_review,prod_reviewAdmin)
admin.site.register(wishlist,WishlistAdmin)
admin.site.register(Address,AddressAdmin)



