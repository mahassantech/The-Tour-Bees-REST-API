from django.db import models
from django.conf import settings

class TourPackageModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.ImageField(
        upload_to="tour_images/",
        blank=True,
        null=True
    )

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="tour_packages"
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
