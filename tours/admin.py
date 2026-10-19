from django.contrib import admin
from .models import TourPackageModel


@admin.register(TourPackageModel)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "title",
        "price",
        "start_date",
        "end_date",
        "created_by",
        "created_at",
    )

    search_fields = ("title", "description")
    list_filter = ("start_date", "end_date")
