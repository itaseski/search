from django.db import models

# Create your models here.

class Manual(models.Model):

    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )

    category = models.ForeignKey('parts.Category', on_delete=models.CASCADE)
    overview = models.TextField(blank=True)
    specification = models.TextField(blank=True)
    function_description = models.TextField(blank=True)
    work_description = models.TextField(blank=True)
    status = models.CharField(max_length=12, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.category
    
    class Meta:
        ordering = ['category',]
