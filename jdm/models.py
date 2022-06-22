from django.db import models
from django.contrib.auth.models import User

        
class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, null=True, blank=True)
    last_name = models.CharField(max_length=20, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    avatar = models.ImageField(upload_to='img', null=True, blank=True)
    date_of_birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.username
    

class Brand(models.Model):
    name = models.CharField(max_length=25)
    photo = models.ImageField(upload_to='img', null=True)
    
    def __str__(self):
        return self.name
        
        
class Body(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    
    
class Transmission(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    
    
class DriveType(models.Model):
    name = models.CharField(max_length=25)
    
    def __str__(self):
        return self.name
    

class Car(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)
    photo1 = models.ImageField(upload_to='img', null=True, blank=True)
    photo2 = models.ImageField(upload_to='img', null=True, blank=True)
    photo3 = models.ImageField(upload_to='img', null=True, blank=True)
    photo4 = models.ImageField(upload_to='img', null=True, blank=True)
    body = models.ForeignKey(Body, on_delete=models.CASCADE)
    sits = models.CharField(max_length=1)
    created = models.CharField(max_length=4)
    transmission = models.ForeignKey(Transmission, on_delete=models.CASCADE)
    drive_type = models.ForeignKey(DriveType, on_delete=models.CASCADE)
    engine_name = models.CharField(max_length=25)
    engine_volume = models.CharField(max_length=25)
    pover = models.CharField(max_length=25)
    moment = models.CharField(max_length=25)
    about = models.TextField(max_length=5000)
    little_more_title = models.TextField(max_length=100, null=True, blank=True)
    little_more = models.TextField(max_length=1500, null=True, blank=True)
    
    def __str__(self):
        return f'Марка - {self.brand}: Модель - {self.model}'
    
    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Car'


class Comment(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(max_length=200)
    created = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'Comment - {self.title}'

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comment'
        ordering = ['-id']
        

class Post(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    content = models.TextField(max_length=1000, null=True, blank=True)
    photo = models.ImageField(upload_to='img', null=True, blank=True)

    def __str__(self):
        return f'Post - {self.name}'
    
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Post'