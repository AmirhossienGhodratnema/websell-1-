from django.db import models
from ckeditor.fields import RichTextField

class karbaruser(models.Model):
    username = models.CharField(max_length=200,verbose_name="نام کاربری")
    first_name = models.CharField(max_length=200,verbose_name="نام")
    last_name = models.CharField(max_length=200,verbose_name="نام خانوادگی")
    tell = models.CharField(max_length=200,verbose_name="موبایل")
    email = models.EmailField(max_length=200,verbose_name="ایمیل")


    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural="تنظیمات کاربران"