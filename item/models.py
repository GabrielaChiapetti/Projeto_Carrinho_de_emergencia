from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#id (primary key) #é automático
#item (string), #expiration_date(date) #feito
#created_date (date) #feito

#drawer (foreign key), show (boolean), owner (foreign key)
#picture (imagem)
class Category(models.Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Item(models.Model): #todos esses campos serão obrigatórios
    item = models.CharField(max_length=50)
    expiration_date = models.DateField()
    created_date = models.DateTimeField(default=timezone.now)
    amount = models.IntegerField(default=1)
    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/')
    category = models.ForeignKey(Category, 
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True
                                 )
    
    owner = models.ForeignKey(User, 
                                 on_delete=models.SET_NULL,
                                 blank=True, null=True
                                 )

    def __str__(self) -> str:
        return f'{self.item}'