from django.shortcuts import render,redirect,HttpResponse
from bapp.models import Blog,Category
from django.contrib.auth.decorators import login_required
from .forms import Category_form,Blog_form
from django.utils.text import slugify
from django.contrib.auth.models import  User
from .forms import Authforms
from .forms import editform

# Create your views here.

@login_required(login_url='login')
def dashboard(request):
    total_post=Blog.objects.all().count()
    total_category=Category.objects.all().count()
    context={
        'total_post':total_post,
        'total_category':total_category
    }
    return render(request,'dashboard/dashboard.html',context)




def category(request):
    return render(request,'dashboard/category.html')



# add category
def add(request):
    if request.method=='POST':
        forms=Category_form(request.POST)
        if forms.is_valid():

            forms.save()
            return redirect('category')

    else:        
        forms=Category_form()
    context={
        'forms':forms
    }
    return render(request,'dashboard/add.html',context)

# for delete 

def delete(request,id):
    category=Category.objects.get(pk=id)
    category.delete()
    return redirect('category')





def edit(request,id):
    if request.method == 'POST':
        get_object=Category.objects.get(id=id)
        forms=Category_form(request.POST)
        if forms.is_valid():
            category_name=forms.cleaned_data['category_name']
            get_object.category_name=category_name
            get_object.save()
            return redirect('category')
        
    forms=Category_form()
    context={
        'id':id,
        'forms':forms,
    }
    return render(request,'dashboard/edit.html',context)








# to display all the post

def blog(request):
    return render(request,'dashboard/blog.html')






def add_post(request):
    if request.method == 'POST':
        forms=Blog_form(request.POST,request.FILES)

        if forms.is_valid():
            post=forms.save(commit=False)
            post.author=request.user
            post.save()
            title=forms.cleaned_data['title']
            post.slug=slugify(title)+'-'+str(post.id)
            post.save()
            return redirect('blog')
        else:
            print(forms.errors)    
    forms=Blog_form()
    context={
        'forms':forms,
    }
    return render(request,'dashboard/add_post.html',context)


# for post edit

def post_edit(request,id):
    get_objects=Blog.objects.get(id=id)
    if request.method == "POST":
        print(request.POST)
        forms=Blog_form(request.POST,request.FILES,instance=get_objects)
        if forms.is_valid():
            post=forms.save()
            title=forms.cleaned_data['title']
            post.slug=slugify(title)+'-'+ str(post.id)
            post.save()
            return redirect('blog')
            



    forms=Blog_form(instance=get_objects)
    context={
        'forms':forms,
        'post':get_objects
    }
    return render(request,'dashboard/post_edit.html',context)

# for deleteing post

def post_delete(request,id):
    post=Blog.objects.get(pk=id)
    post.delete()
    return redirect('blog')



def user(request):
    all_user=User.objects.all()
    content={
        'all_user':all_user,
    }
    return render(request,'dashboard/user.html',content)





def add_user(request):
    if request.method == 'POST':
        forms=Authforms(request.POST)
        if forms.is_valid():
            forms.save()
            return redirect('user')
    forms=Authforms()
    context={
        'forms':forms
    }
    return render(request,'dashboard/add_user.html',context)





def edit_user(request,id):
    get_user=User.objects.get(id=id)
    if request.method =='POST':
        forms=editform(request.POST,instance=get_user)
        if forms.is_valid():
            forms.save()
            return redirect('user')

        else:
            print(forms.errors)    
    
    forms=editform(instance=get_user)
    context={
        'forms':forms,
        'id':id
    }
    return render(request,'dashboard/edit_user.html',context)





# for deleting user

def delete_user(request,id):
    get_obj=User.objects.get(id=id)
    get_obj.delete()
    return redirect('user')
   