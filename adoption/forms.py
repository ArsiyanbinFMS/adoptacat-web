from django import forms
from .import models
from .models import Vaccine, Color, Comment, Adopted, Message
from django.forms.widgets import CheckboxSelectMultiple

class AdoptedForm(forms.ModelForm):
    adoptername = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'ชื่อผู้รับเลี้ยงแมว',
    }))
    location = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'อำเภอ,จังหวัด',
    }))
    contact = forms.CharField(widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder': 'อีเมลติดต่อ',
    }))
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class':'form-control',
        'placeholder': 'วันที่ถูกรับเลี้ยง',
    }))
    class Meta:
        model = models.Adopted
        fields = ['adoptername','location','contact','date']

class CatForm(forms.ModelForm):
    class Meta:
        model = models.Cat
        fields = ['name','age','gender','color','breed','vaccines','nature','location','image','status']
        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control','cols':'15'}),
            'age': forms.NumberInput(attrs={'class':'form-control'}),
            'gender': forms.Select(attrs={'class':'form-control'}),
            'nature': forms.Textarea(attrs={'class':'form-control'}),
            'location': forms.TextInput(attrs={'class':'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(CatForm, self).__init__(*args, **kwargs)
        self.fields['vaccines'].widget = CheckboxSelectMultiple()
        self.fields['vaccines'].queryset= Vaccine.objects.all()
        self.fields['color'].widget = CheckboxSelectMultiple()
        self.fields['color'].queryset= Color.objects.all()

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder': 'พิมพ์ความคิดเห็นที่นี่',
        'rows':'5',  
    }))
    class Meta:
        model = Comment
        fields = ('content',)

class MessageForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class':'form-control',
        'placeholder': 'พิมพ์ข้อความที่นี่',
        'rows':'5',  
    }))
    class Meta:
        model = Message
        fields = ('content',)

