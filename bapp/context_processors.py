
from .models import Category
from assignment.models import socail_platforms
from bapp.models import Blog
def get_category(request):
    category=Category.objects.all()
    return dict(category=category)



def get_platforms(request):
    platform=socail_platforms.objects.all()
    return dict(platform=platform)





def blog_post(request):
    all_post=Blog.objects.all()
    return dict(all_post=all_post)
