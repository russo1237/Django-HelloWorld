from django.db import models

# Create your models here.
class message(models.Model):
    msg = models.CharField(max_length=64)

    def __str__(self):
        return "%s"%(self.msg)

