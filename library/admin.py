from django.contrib import admin
from . models import ExtraUserInfo,Book,BookInstance,IsseBook

# Register your models here.

admin.site.register(ExtraUserInfo)
admin.site.register(Book)
admin.site.register(BookInstance)
admin.site.register(IsseBook)
