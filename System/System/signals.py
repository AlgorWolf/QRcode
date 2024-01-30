import qrcode
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files.base import ContentFile
from PIL import Image
from io import BytesIO

from .models import Info

@receiver(post_save, sender=Info)
def generate_qrcode(sender, instance, created, **kwargs):
    # Check if the instance is being created to avoid recursion on subsequent saves
    if created:
        # Create a QR code instance
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # Add data to the QR code (customize this part based on your model fields)
        qr.add_data(f"https://bscqrcode.onrender.com/id/{instance.id}")
        qr.make(fit=True)

        # Create an image from the QR code
        img = qr.make_image(fill_color="black", back_color="white")

        # Save the image to a BytesIO buffer
        buffer = BytesIO()
        img.save(buffer, format="PNG")

        # Save the BytesIO buffer to the ImageField
        instance.qrcode.save(f"qrcode_{instance.id}.png", ContentFile(buffer.getvalue()), save=False)
        instance.save()
