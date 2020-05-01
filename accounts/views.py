from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if form.is_valid and profile_form.is_valid():
            user = form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            messages.success(request, ('สมัครสมาชิกสำเร็จ!'))
            return redirect('signup') 
    else:
        form = UserCreationForm()
        profile_form = ProfileForm()
        context = {
            'form':form,
            'profile_form':profile_form
        }
    return render(request, 'signup.html',context)
@login_required
def profile(request):
    args= {'user':request.user}
    return render(request, 'profile.html', args)

@login_required
def edit(request, id):
    post = get_object_or_404(Profile,id=id)
    if request.method == 'POST':
        form = ProfileForm(request.POST or None,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,('อัพเดตข้อมูลโปรไฟล์แล้ว!'))
            return redirect('profile')
    else:
        form = ProfileForm(instance=post)
    context ={
        'form':form,
        'post':post,
    }
    return render(request, 'profile_edit.html',context)
