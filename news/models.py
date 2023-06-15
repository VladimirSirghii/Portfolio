from django.db import models

# Create your models here.


class Articles(models.Model):
    title = models.CharField('Denumirea', max_length=50)
    anons = models.CharField('Anunt', max_length=300)
    full_text = models.TextField('Articol')
    date = models.DateTimeField('Data publicarii')

    def __str__(self):  
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Stire'
        verbose_name_plural = 'Stiri'
