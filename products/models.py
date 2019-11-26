from django.db import models

# Create your models here.

class Product(models.Model):
    ARTEFACTS = (
        
        ('HIS', 'History'),
        ('CUL', 'Culture'),
        ('REL', 'Religion'),
        ('MED', 'Media'),
    )
    
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="images")
    details = models.CharField(max_length=255)
    history = models.TextField()
    quantity = models.IntegerField()
    artefact = models.CharField(max_length=2, choices=ARTEFACTS)
    posted_date = models.DateTimeField(blank=True, null=True)