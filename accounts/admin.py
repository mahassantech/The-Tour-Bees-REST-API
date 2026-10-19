from django.contrib import admin
from .models import RegisterModel

@admin.register(RegisterModel)
class RegisterModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "username",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "role",
        "profile_photo",
    )

    list_filter = ("role",)

    search_fields = (
        "username",
        "first_name",
        "last_name",
        "email",
        "phone_number",
    )
