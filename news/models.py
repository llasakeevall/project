from django.db import models

# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(
        null= True, blank= True,
        upload_to='newImage/'
    )
    desc = models.TextField(blank=True)
    

    def __str__(self) :
        return self.title 
    
    class Meta:
        verbose_name_plural = 'Новости'

class AboutUs(models.Model):
    title = models.CharField(max_length=30)
    desc = models.TextField()

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Страница о нас'

class Reviews(models.Model):
    title = models.CharField(max_length=50, verbose_name="ФИО")
    desc = models.TextField(verbose_name="отзывы")

    def __str__(self):
        return self.title
    class Meta:
        verbose_name_plural = 'отзывы'
        

    