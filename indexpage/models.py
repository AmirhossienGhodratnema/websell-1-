
from email.headerregistry import Address
from django.db import models
from ckeditor.fields import RichTextField


class indexdb(models.Model):
    base_title = models.CharField(max_length=2000,verbose_name="سر تیتر صفحه اصلی")
    base_subtitle = RichTextField(verbose_name="متن زیر سر تیتر صفحه اصلی")
    base_pic = models.ImageField(upload_to='indexfolder/photos/%y/%m/%d/',verbose_name="عکس بالای سایت زیر متن")

    vijegi_right_title = models.CharField(max_length=2000,verbose_name="ویژگی های دوست داشتنی تیتر سمت راست")
    vijegi_right_subtitle = RichTextField(verbose_name="ویژگی های دوست داشتنی متن سمت راست")
    vijegi_center_title = models.CharField(max_length=2000,verbose_name="ویژگی های دوست داشتنی تیتر وسط")
    vijegi_center_subtitle = RichTextField(verbose_name="ویژگی های دوست داشتنی متن وسط")
    vijegi_left_title = models.CharField(max_length=2000,verbose_name="ویژگی های دوست داشتنی تیتر سمت چپ")
    vijegi_left_subtitle = RichTextField(verbose_name="ویژگی های دوست داشتنی متن سمت چپ")

    anva_angir_text = RichTextField(verbose_name="متن انواع انجیر")
    anva_angir_pic = models.ImageField(upload_to='indexfolder/photos/%y/%m/%d/',verbose_name="عکس تیتر انواع انجیر")
    
    ravand_tolid_angir_title_ok_1 = models.CharField(max_length=2000,verbose_name="روند تولید تیتر اصلی 1")
    ravand_tolid_angir_title_1 = models.CharField(max_length=2000,verbose_name="روند تولید تیتر 1 ")
    ravand_tolid_angir_subtitle_1 = models.CharField(max_length=2000,verbose_name="روند تولید زیر تیتر 1")
    ravand_tolid_angir_text_1 = RichTextField(verbose_name="روند تولید متن 1")
    ravand_tolid_angir_pic_1 = models.ImageField(upload_to='indexfolder/photos/%y/%m/%d/',verbose_name="روند تولید عکس 1")
    
    ravand_tolid_angir_title_ok_2 = models.CharField(max_length=2000,verbose_name="روند تولید تیتر اصلی 2")
    ravand_tolid_angir_title_2 = models.CharField(max_length=2000,verbose_name="روند تولید تیتر 2 ")
    ravand_tolid_angir_subtitle_2 = models.CharField(max_length=2000,verbose_name="روند تولید زیر تیتر 2")
    ravand_tolid_angir_text_2 = RichTextField(verbose_name="روند تولید متن 2")
    ravand_tolid_angir_pic_2 = models.ImageField(upload_to='indexfolder/photos/%y/%m/%d/',verbose_name="روند تولید عکس 2")
    
    ravand_tolid_angir_title_ok_3 = models.CharField(max_length=2000,verbose_name="روند تولید تیتر اصلی 3")
    ravand_tolid_angir_title_3 = models.CharField(max_length=2000,verbose_name="روند تولید تیتر 3 ")
    ravand_tolid_angir_subtitle_3 = models.CharField(max_length=2000,verbose_name="روند تولید زیر تیتر 3")
    ravand_tolid_angir_text_3 = RichTextField(verbose_name="روند تولید متن 3")
    ravand_tolid_angir_pic_3 = models.ImageField(upload_to='indexfolder/photos/%y/%m/%d/',verbose_name="روند تولید عکس 1")
    
    ravand_tolid_angir_title_ok_4 = models.CharField(max_length=2000,verbose_name="روند تولید تیتر اصلی 4")
    ravand_tolid_angir_title_4 = models.CharField(max_length=2000,verbose_name="روند تولید تیتر 4 ")
    ravand_tolid_angir_subtitle_4 = models.CharField(max_length=2000,verbose_name="روند تولید زیر تیتر 4")
    ravand_tolid_angir_text_4 = RichTextField(verbose_name="روند تولید متن 4")
    ravand_tolid_angir_pic_4 = models.ImageField(upload_to='indexfolder/photos/%y/%m/%d/',verbose_name="روند تولید عکس 4")

    moshtarian_text_1 = RichTextField(verbose_name="مشتریان متن 1")
    moshtarian_name_1 = models.CharField(max_length=2000,verbose_name="مشتریان نام 1")
    moshtarian_location_1 = models.CharField(max_length=2000,verbose_name="مشتریان مکان 1")
    
    moshtarian_text_2 = RichTextField(verbose_name="مشتریان متن 2")
    moshtarian_name_2 = models.CharField(max_length=2000,verbose_name="مشتریان نام 2")
    moshtarian_location_2 = models.CharField(max_length=2000,verbose_name="مشتریان مکان 2")
    
    moshtarian_text_3 = RichTextField(verbose_name="مشتریان متن 3")
    moshtarian_name_3 = models.CharField(max_length=2000,verbose_name="مشتریان نام 3")
    moshtarian_location_3 = models.CharField(max_length=2000,verbose_name="مشتریان مکان 3")
    
    soal_title_1 = models.CharField(max_length=2000,verbose_name="سوالات متداول تیتر 1")
    soal_text_1 = RichTextField(verbose_name="سوالات متداول متن  1")
    
    soal_title_2 = models.CharField(max_length=2000,verbose_name="سوالات متداول تیتر 2")
    soal_text_2 = RichTextField(verbose_name="سوالات متداول متن  2")

    soal_title_3 = models.CharField(max_length=2000,verbose_name="سوالات متداول تیتر 3")
    soal_text_3 = RichTextField(verbose_name="سوالات متداول متن  3")

    soal_title_4 = models.CharField(max_length=2000,verbose_name="سوالات متداول تیتر 4")
    soal_text_4 = RichTextField(verbose_name="سوالات متداول متن  4")

    def __str__(self):
        return self.base_title
    class Meta:
        verbose_name_plural="صفحه اصلی"





class indexselldb(models.Model):
    pic_name = models.CharField(max_length=2000,verbose_name="نام عکس")
    pic = models.ImageField(upload_to='indexdb/photos/%y/%m/%d/',verbose_name="عکس محصول")
    def __str__(self):
        return self.pic_name
    class Meta:
        verbose_name_plural="عکس محصولات در صفحه اصلی"





class footerdb(models.Model):
    my_address = models.CharField(max_length=2000,verbose_name="آدرس")
    my_mail = models.CharField(max_length=2000,verbose_name="ایمیل")
    my_tell = models.CharField(max_length=2000,verbose_name="تلفن")
    my_facebook = models.CharField(max_length=2000,verbose_name="فیس بوک")
    my_twitter = models.CharField(max_length=2000,verbose_name="توئیتر")
    my_instagram = models.CharField(max_length=2000,verbose_name="اینستاگرام")
    
    def __str__(self):
        return self.my_tell
    class Meta:
        verbose_name_plural="فوتر"
