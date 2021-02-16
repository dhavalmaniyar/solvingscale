from django.contrib import admin
from .models import Inquiry
# Register your models here.
class BookInquiry(admin.ModelAdmin):
    list_display=('date','name','inquiry')

admin.site.register(Inquiry,BookInquiry)