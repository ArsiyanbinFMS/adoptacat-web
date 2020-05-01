from django.shortcuts import render, redirect ,reverse ,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from accounts.models import Profile
from adoption import forms
from .forms import CatForm, CommentForm, AdoptedForm, MessageForm
from .models import Cat, Comment, Adopted, Request, Message, Request

def homepage(request):
    latest = Cat.objects.order_by('-entrydate')[0:3]
    context={
        'latest' : latest
    }
    return render(request,'adoption/index.html',context )


def catlist(request):
    allcat = Cat.objects.all().order_by('-entrydate')
    context = {
        'allcat': allcat,
    }
    return render(request, 'adoption/catlist.html',context)

    

@login_required
def addcat_page(request):
    if request.method == 'POST':
        form =forms.CatForm(request.POST,request.FILES)
        if form.is_valid():
            #save cat to catdb
            instant = form.save(commit=False)
            instant.poster = request.user
            instant.save()
            form.save_m2m()
            messages.success(request, ('แมวของคุณถูกเพิ่มแล้ว!'))
            return redirect('mycatlist')
    else:
        form = forms.CatForm()
    return render(request, 'adoption/cat_form.html',
        {'form':form}
        ) 

@login_required
def mycatlist(request):
    mycats = Cat.objects.filter(poster=request.user).order_by('-entrydate')
    
    context = { 
        'mycats': mycats,
        
        }
    return render(request, 'adoption/my_catlist.html', context)

@login_required
def delete(request, cat_id):
    item = Cat.objects.get(pk=cat_id)
    item.delete()
    messages.success(request, ('ข้อมูลแมวถูกลบออกแล้ว!'))
    return redirect('mycatlist')

#ใส่ชื่อแบบฟอร์มใหม่ด้วยนะ
@login_required
def edit(request, id):
    post = get_object_or_404(Cat,id=id)
    if request.method == 'POST':
        form = CatForm(request.POST or None,instance=post)
        if form.is_valid():
            form.save()
            messages.success(request,('ข้อมูลแมวถูกอัพเดตแล้ว!'))
            return redirect('mycatlist')
    else:
        form = CatForm(instance=post)
    context ={
        'form':form,
        'post':post,
    }
    return render(request, 'adoption/edit.html',context)

@login_required
def catinfo(request,id):
    cat = get_object_or_404(Cat,id=id)
    comments = Comment.objects.filter(post=cat).order_by('-timestamp')
    if request.method =='POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            comment = Comment.objects.create(post=cat, user=request.user, content=content)
            comment.save()
            return redirect(reverse("catinfo", kwargs={
                'id': cat.pk
            }))
    else:
        comment_form=CommentForm()

    context = {
        'catinfo':cat,
        'comments':comments,
        'comment_form':comment_form,
        }
    return render(request,'adoption/catinfo.html',context)

@login_required
def adoptedcat(request):
    cat = Cat.objects.filter(status=True).order_by('-entrydate')
    context = {
        'cat': cat,
    }
    return render(request, 'adoption/adopted_cat.html',context)

@login_required
def adoptedinfo(request,id):
    post = get_object_or_404(Cat,id=id)
    info = Adopted.objects.get(cat=post)
    context = {
        'info':info,
        }
    return render(request,'adoption/adopted_info.html',context)

@login_required
def myrequestlist(request):
    mylist = Request.objects.filter(requester=request.user).order_by('-date')
    context = { 
        'mylist': mylist,
        
        }
    return render(request, 'adoption/my_requestlist.html', context)

@login_required
def requestlist(request,id):
    post = get_object_or_404(Cat,id=id)
    allrequest = Request.objects.filter(cat=post).order_by('-date')
    context = { 
        'allrequest': allrequest, 
        }
    return render(request, 'adoption/request_list.html', context)

@login_required
def requestinfo(request,id):
    info = get_object_or_404(Request,id=id)
    ms = Message.objects.filter(parent=info).order_by('-timestamp')
    if request.method =='POST':
        message_form = MessageForm(request.POST or None)
        if message_form.is_valid():
            content = request.POST.get('content')
            msg = Message.objects.create(parent=info, user=request.user, content=content)
            msg.save()
            return redirect(reverse("request_info", kwargs={
                'id': info.pk
            }))
    else:
        message_form = MessageForm()

    context = {
        'info':info,
        'ms':ms,
        'message_form':message_form,
        }
    return render(request,'adoption/request_info.html',context)