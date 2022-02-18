from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Rahbariyat)

class TadbirlarModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":('name',)}
    list_display = ('name','slug','sanasi')

admin.site.register(Images)
admin.site.register(Tadbirlar,TadbirlarModelAdmin)
admin.site.register(Maktab)
admin.site.register(Biz_xaqimizda)
admin.site.register(Foydalanuchi)