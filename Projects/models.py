from django.db import models

# Create your models here.
class ProjectShow(models.Model):
    prject_id = models.AutoField
    
    link = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Project/images', default="")
    project_name = models.CharField(max_length=100)
    desc = models.TextField()
    desc2 = models.TextField(blank=True)
    
    def __str__(self):
        return self.project_name
    
    