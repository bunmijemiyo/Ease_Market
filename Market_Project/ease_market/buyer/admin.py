from django.contrib import admin

# Register your models here.

from .models import Buyer
from seller.models import Seller

admin.site.register(Buyer)
