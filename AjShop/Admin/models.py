from django.db import models

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

    class Meta:
        db_table= "Category"



class Product(models.Model):
    pname = models.CharField(max_length=20)
    price = models.FloatField(default= 200)
    description = models.CharField(max_length= 200)
    #size = models.FloatField(max_length=20)
    qty = models.IntegerField( 10)
    image = models.ImageField(default= 'Abc.jpd', upload_to= 'Images')
    cat = models.ForeignKey(to= 'Category', on_delete=models.CASCADE)

    class Meta:
        db_table= "Product"

class UserInfo(models.Model):
    uname = models.CharField(max_length= 20, primary_key= True)
    password = models.CharField(max_length= 20)
    email = models.EmailField(max_length=100)

    class Meta:
        db_table = "UserInfo"

class Payment(models.Model):
    cardno = models.CharField(max_length=20)
    cvv = models.CharField(max_length=4)
    exp = models.CharField(max_length=20)
    balance = models.FloatField(max_length=10000)

    class Meta:
        db_table = "Payment"



#username -- anujs
#password -- 1234
# card no. 333	cvv 333	 d o exp. 12/2025	amount 30000.0
# card no. 222	cvv 222	 d o exp. 12/2025	amount 30000.0
# database Paswword AJ@280197