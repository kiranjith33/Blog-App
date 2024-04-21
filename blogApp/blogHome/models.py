from django.db import models
from ckeditor.fields import RichTextField,RichTextFormField

from django_ckeditor_5.fields import CKEditor5Field



# Create your models here.




class Blog(models.Model):
    
    
    name = models.CharField(max_length=50,default="")
    title = models.CharField(max_length=100,default="")
    id = models.AutoField(primary_key=True)
    shortDesc = models.CharField(max_length=100,default="")
    time = models.DateTimeField(auto_now_add = True)
    content = RichTextField()
    thumbnail = models.ImageField(upload_to="blogimages")




    def __str__(self) -> str:
        return self.name