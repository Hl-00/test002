from django.contrib import admin

# Register your models here.
from management import models

admin.site.register(models.UserInfo)

admin.site.register(models.meter)

admin.site.register(models.inventory)

