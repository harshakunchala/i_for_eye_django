from django.contrib import admin
from .models import Book, Ngo_details, Volunteer, Recording

# Register your models here.
admin.site.register(Book)
admin.site.register(Volunteer)
admin.site.register(Recording)
admin.site.register(Ngo_details)