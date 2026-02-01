from django.db import models

class Department(models.Model):
    d_name = models.CharField(max_length=50)
    h_head = models.CharField(max_length=50)

    def __str__(self):
        return self.d_name
