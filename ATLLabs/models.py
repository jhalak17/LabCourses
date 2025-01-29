from django.db import models

class Equipment(models.Model):
    """
    Model representing an equipment item.

    Attributes:
        name (str): The name of the equipment.
        description (str): A detailed description of the equipment.
        contents (str): The contents or components of the equipment.
        instruction (str): Instructions for using the equipment.
        price (Decimal): The price of the equipment.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    contents = models.TextField()
    instruction = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='equipment_images/', blank=True, null=True)

    def __str__(self):
        """Return a string representation of the equipment name."""
        return self.name
