from django.db import models
from django.contrib.auth import get_user_model
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill
from django.utils import timezone
User = get_user_model()


class Color(models.Model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class Vaccine(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Breed(models.Model):
    breed_type = models.CharField(max_length=50)
    def __str__(self):
        return self.breed_type

class Cat(models.Model):
    GENDER = (
        ('Male', 'ผู้'),
        ('Female', 'เมีย'),
    )
    name = models.CharField(max_length=30,null=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=10,choices=GENDER)
    breed = models.ForeignKey(Breed,null=True,on_delete=models.SET_NULL)
    color = models.ManyToManyField(Color)
    vaccines = models.ManyToManyField(Vaccine, blank=True)
    nature = models.TextField(max_length=200)
    location = models.CharField(max_length=100)
    entrydate = models.DateTimeField(auto_now_add=True)
    poster = models.ForeignKey(User ,on_delete=models.CASCADE)
    image = ProcessedImageField(default='default.jpg', upload_to='cat_pics',processors=[ResizeToFill(300,200)],format='JPEG',options={'quality': 120})
    status = models.BooleanField(default=False)
    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default='ความคิดเห็น',max_length=300)
    post = models.ForeignKey(Cat,related_name='comments' ,on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}-{}'.format(self.post.name, str(self.user.username))  

class Adopted(models.Model):
    cat = models.OneToOneField(Cat,on_delete=models.CASCADE,null=True)
    adoptername = models.CharField(max_length=100,default='ชื่อผู้รับเลี้ยง')
    location = models.CharField(max_length=100,default='อำเภอ,จังหวัด')
    contact = models.EmailField(max_length=70,blank=True)
    date = models.DateField()
    def __str__(self):
        return '{}-{}'.format(self.cat.name, str(self.adoptername))


class Request(models.Model):
    HOUSE = (
        ('Single', 'บ้านเดี่ยว'),
        ('Shop', 'อาคารพาณิชย์หรือตึกแถว'),
        ('Town', 'ทาวน์เฮาส์'),
        ('Flat ', 'แฟลตหรืออาพาร์ตเม้นต์'),
        ('Condominium ', 'คอนโดมิเนียม'),
    )
    FENCE=(
        ('Yes', 'มีรั้ว'),
        ('No', 'ไม่มีมีรั้ว')
    )
    ANSWER=(
        ('Yes', 'ใช่'),
        ('No', 'ไม่ใช่')
    )
    requester = models.ForeignKey(User ,on_delete=models.CASCADE)
    cat =  models.ForeignKey(Cat,related_name='requests' ,on_delete=models.CASCADE)
    location = models.CharField(max_length=100,)
    housetype = models.CharField(max_length=40,choices=HOUSE)
    fencedetail = models.CharField(max_length= 15,choices=FENCE)
    budget = models.PositiveIntegerField()
    pets = models.CharField(max_length=10,choices=ANSWER)
    message = models.TextField(max_length=200)
    date = models.DateField(auto_now_add=True)
    contact = models.CharField(max_length=40,default='หมายเลขโทรศัพท์')
    email = models.EmailField(max_length=70,blank=True)
    social = models.CharField(max_length=70,default='FB/LINE/IG ID')
    def __str__(self):
            return '{}-{}'.format(self.cat.name, str(self.requester.username))

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField(default='ข้อความ',max_length=300)
    parent = models.ForeignKey(Request,related_name='messages' ,on_delete=models.CASCADE)
    
    def __str__(self):
        return '{}-{}-reply to {}'.format(self.parent.cat.name, str(self.user.username), str(self.parent.requester) )