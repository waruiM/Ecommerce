from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauths.models import User

STATUS_CHOICE=(
    ("process","Processing"),
    ("shipped","Shipped"),
    ("delivered","Delivered")
)
STATUS=(
    ("draft","Draft"),
    ("disabled","Disabled"),
    ("rejected","Rejected"),
)

PROD_STATUS=(
    ("process","Processing"),
    ("rejected","Rejected"),
    ("in_review","In_review"),
    ("published","Published"),
)


RATING=(
    (1,"★☆☆☆☆"),
    (2,"★★☆☆☆"),
    (3,"★★★☆☆"),
    (4,"★★★★☆"),
    (5,"★★★★★")
)


# creating the user folder and saving the image uploded
def user_directory_path(instance,filename):
    #geting the user id 
    return 'user_{0}/{1}'.format(instance.user.id,filename)

# Creating the model for categories.
class Category (models.Model):
    # creating custom id for the items
    cid= ShortUUIDField(unique=True,length=10, max_length=20, prefix="cag",alphabet="abcdef012345")

    title=models.CharField(max_length=100,default="food")
    image=models.ImageField(upload_to="category")

    # naming for the admin section
    class Meta:
        verbose_name_plural="Categories"

    def category_image(self):
        # replacing the s from  %s with the values paced in the above category section
        return mark_safe('<img src="%s"width="50" height="50"/>' % (self.image.url))   

    def __str__(self):
        return self.title

class Tags(models.Model):
    pass

# vendor section
class Vendor(models.Model):
    vid=ShortUUIDField(unique=True,length=10,max_length=25,prefix="ven",alphabet="abcdef012345")

    title= models.CharField(max_length=100,default="vendor 1")
    cover_image=models.ImageField(upload_to=user_directory_path,null=True,blank=True)
    image=models.ImageField(upload_to=user_directory_path)
    description=models.TextField(null=True,blank=True,default="you need it I got you")

    address=models.CharField(max_length=100,blank=True)
    phone=models.CharField(max_length=100,blank=False)
    chat_resp_time=models.CharField(max_length=100,default="100")
    shipping_on_time=models.CharField(max_length=100,default="100")
    authenticat_rat=models.CharField(max_length=100,default="70")
    warant_period=models.CharField(max_length=100,default="12 days") 
    # ondeletion function
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True,null=True,blank=True)

    # naming to appear in the admin section
    class Meta:
        verbose_name_plural="Vendors"

    def vendor_image(self):
        # replacing the s from  %s with the values paced in the above category section
        return mark_safe('<img src="%s" width="50" height="50"/>' % (self.image.url))    

    def __str__(self):
        return self.title

#creating the model for products
class Product(models.Model):
    pid=ShortUUIDField(unique=True,length=10,max_length=25,prefix="prd",alphabet="abcdef012345")
    
    # ondeletion function
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    category=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,related_name="category")

    vendor=models.ForeignKey(Vendor,on_delete=models.SET_NULL,null=True,related_name="products")


    title= models.CharField(max_length=100,default="product A")
    image=models.ImageField(upload_to=user_directory_path)
    description=models.TextField(null=True,blank=True,default="best in town")

    price=models.DecimalField(max_digits=999999999999999,decimal_places=2,default="1.99")
    old_price=models.DecimalField(max_digits=999999999999999,decimal_places=2,default="2.99")

    specifications=models.TextField(null=True,blank=True)
    #tags=models.ForeignKey(Tags,on_delete=models.SET_NULL,null=True,blank=True)

    product_status=models.CharField(choices=PROD_STATUS,max_length=20,default="in_review")

    status=models.BooleanField(default=True)
    in_stock=models.BooleanField(default=True)
    featured=models.BooleanField(default=False)
    digital=models.BooleanField(default=False)

    sku=ShortUUIDField(unique=True, length=4, max_length=12, prefix="sku", alphabet="0123456789")

    date=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(null=True,blank=True)

    class Meta:
        verbose_name_plural="Products"

    def product_image(self):
        return mark_safe('<img src="%s"width="50" height="50"/>' % (self.image.url))

    def __str__(self):
        return self.title

    #getting discount percentage
    def prd_percentage(self):
        new_price=(self.price/self.old_price)*100
        new_price=100 - new_price
        return new_price

class ProductImages(models.Model):
    images=models.ImageField(upload_to="product-images",default="product.jpg")
    Product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Product Images"

##################################################cart,order,orderItems#######################################
class CartOrder(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    price=models.DecimalField(max_digits=9999999999999999999,decimal_places=2,default="1.99")
    paid_status=models.BooleanField(default=False)
    order_date=models.DateTimeField(auto_now_add=True)
    order_status=models.CharField(choices=STATUS_CHOICE,max_length=20,default="Processing")

    class Meta:
        verbose_name_plural="Cart Order"


class CartOrderItems(models.Model):
    order=models.ForeignKey(CartOrder,on_delete=models.CASCADE)
    invoice_no=ShortUUIDField(unique=True,length=10,max_length=25,prefix="inv",alphabet="abcdef01234556")
    product_status=models.CharField(max_length=200)
    item=models.CharField(max_length=200)
    image=models.CharField(max_length=200)
    quantity=models.IntegerField(default=0)
    price=models.DecimalField(max_digits=999999999999,decimal_places=2,default="1.99")
    total=models.DecimalField(max_digits=999999999999,decimal_places=2,default="1.99")

    class Meta:
        verbose_name_plural="Cart order Items"

    def order_image(self):
        # replacing the s from  %s with the values paced in the above category section
        return mark_safe('<img src="/media/%s" width="50" height="50"/>' % (self.image.url))    

################################################product review,wishlist,address############################
class prod_review(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,blank=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    review=models.TextField()
    rating=models.IntegerField(choices=RATING,default=3)
    date=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="Product_reviews"

    def __str__(self):
        return self.product.title

    def get_rating(self):
        return self.rating

##wishlist
class wishlist(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    date=models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural="Wishlists"

    def __str__(self):
        return self.product.title

##address book
class Address(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    email=models.EmailField(max_length=254)
    address=models.CharField(max_length=100)
    status=models.BooleanField(default=False)    

    class Meta:
        verbose_name_plural="Addresses"


