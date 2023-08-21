from django.contrib import admin
from .models import Category,Product,Payment
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","category_name")


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id","pname","price","description","qty",
                    "image","cat")
    
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('cardno','cvv','exp','balance')
    

admin.site.register(Category,CategoryAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Payment,PaymentAdmin)

# Admin Id & Pass.... Ajelct