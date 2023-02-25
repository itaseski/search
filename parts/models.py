from django.db import models

from django.core.validators import FileExtensionValidator

class Category(models.Model):

    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )

    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    slug = models.SlugField()
    code = models.CharField(max_length=256)
    #image = models.ImageField(blank=True, upload_to='images/')
    image_file_name = models.FileField(blank=True, upload_to='catalog/images/', validators=[FileExtensionValidator(['pdf', 'doc', 'svg'])])
    status = models.CharField(max_length=12, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['code', ]



class Part(models.Model):

    STATUS = (
        ('True', 'True'),
        ('False', 'False')
    )

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    position_on_drawing = models.CharField('pos', max_length=3, blank=True)
    references = models.CharField(max_length=1024, blank=True)
    part_number = models.CharField(max_length=7, unique=True)
    quantity = models.IntegerField(default=1)
    part_replacement_number = models.CharField(max_length=7, blank=True)
    designation = models.CharField(max_length=128)
    info = models.CharField(max_length=64, blank=True)
    note = models.CharField(max_length=64, blank=True)
    status = models.CharField(max_length=12, choices=STATUS)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.designation
    
    class Meta:
        ordering = ['category', 'position_on_drawing']

    

 



