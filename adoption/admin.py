from django.contrib import admin
from .models import Cat,Breed,Color,Vaccine,Comment,Adopted,Request,Message

admin.site.site_header = 'AdoptaCat Admin'
admin.site.register(Cat)
admin.site.register(Breed)
admin.site.register(Color)
admin.site.register(Vaccine)
admin.site.register(Comment)
admin.site.register(Adopted)
admin.site.register(Request)
admin.site.register(Message)


