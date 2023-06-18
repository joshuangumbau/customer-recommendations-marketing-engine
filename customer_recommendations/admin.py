from django.contrib import admin

# Register your models here.

from .models import Customer, Recommendations

admin.site.register(Customer)

admin.site.register(Recommendations)