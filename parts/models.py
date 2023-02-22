from django.db import models

class Part(models.Model):
    designation = models.CharField(max_length=128)
    part_number = models.CharField('Part number', max_length=7)


    def __str__(self):
        return self.designation
