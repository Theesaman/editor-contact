from django.contrib import admin
from .models import Contact, Gallery


# Register your models here.

admin.site.register((Gallery,Contact))