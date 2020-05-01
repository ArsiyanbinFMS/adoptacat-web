from django.db import models
from django.contrib.auth.models import User
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = ProcessedImageField(default='default.jpg', upload_to='profile_pics',processors=[ResizeToFill(200,200)],format='JPEG',options={'quality': 60})
    location = models.CharField(max_length=100,default='อำเภอ,จังหวัด')
    phone = models.CharField(max_length=10,blank=True,null=True)
    age = models.PositiveIntegerField()
    def __str__(self):
        return f'{self.user.username} Profile'
    
