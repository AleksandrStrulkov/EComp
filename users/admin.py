from django.contrib import admin

# Register your models here.
from django.contrib import admin
from users.models import User


# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'avatar', 'phone', 'country', 'is_staff', 'is_active')
    list_filter = ('email',)
    search_fields = ('email',)
