from django.contrib import admin
from .models import MainModel
# Register your models here.
@admin.register(MainModel)
class StuAdmin(admin.ModelAdmin):
    list_display=['id','Studentname','Teachername','Email','Password']
    

