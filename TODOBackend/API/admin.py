from django.contrib import admin
from .models import Todo, Priority

# Register your models here.

admin.site.register(Todo)
admin.site.register(Priority)
