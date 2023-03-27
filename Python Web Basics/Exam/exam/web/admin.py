from django.contrib import admin

# Register your models here.
from django.contrib import admin
from exam_30_10_22.web.models import Profile, Car

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    pass
