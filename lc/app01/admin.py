from django.contrib import admin

# Register your models here.
from app01.models import User01
admin.site.register(User01)
from app01.models import User02
admin.site.register(User02)