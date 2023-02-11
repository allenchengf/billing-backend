from django.db import models



class Customer(models.Model):

    PROPERTY_CHOICES = (
        ('Presales', 'Presales'),
        ('Existing', 'Existing'),
        ('Terminated', 'Terminated')
    )

    customer_name = models.CharField(max_length=255, blank=True, null=True)
    customer_id = models.CharField(max_length=255, unique=True)
    customer_property = models.CharField(verbose_name="Task status", max_length=20, choices=PROPERTY_CHOICES, default='Presales')
    am = models.CharField(max_length=128, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True, auto_now=True)

    def __str__(self):
        return self.customer_id
