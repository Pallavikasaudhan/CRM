from django.contrib import admin
from . models import Enquiry
from . models import Customer
from . models import Login
# Register your models here.
admin.site.register(Enquiry)
admin.site.register(Customer)
admin.site.register(Login)