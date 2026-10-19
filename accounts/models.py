
from django.db import models
from django.contrib.auth.models import AbstractUser


class RegisterModel(AbstractUser):

    class Role(models.TextChoices):
        ADMIN = "admin", "Admin"
        CUSTOMER = "customer", "Customer"
        TOUR_ORGANIZER = "tour_organizer", "Tour Organizer"

    email = models.EmailField(unique=True)

    phone_number = models.CharField(
        max_length=11,
        unique=True
    )
    
    profile_photo = models.ImageField(
    upload_to="profile_photos/",
    blank=True,
    null=True
)

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.CUSTOMER
    )

    def __str__(self):
        return self.username
