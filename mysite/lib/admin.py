from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import *

admin.site.register(Authors)
admin.site.register(Books)
admin.site.register(Genres)

