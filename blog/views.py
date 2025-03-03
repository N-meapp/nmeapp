from django.core.paginator import Paginator
from django.shortcuts import render
from. models import*

# Create your views here.
def base(request):
    return render(request, 'base.html')
def home(request):
    return render (request,'index.html')
def about(request):
    return render (request,'about.html')
def register(request):
    return render (request,'register.html')
def services(request):
    return render (request,'services.html')

def faq(request):
    return render (request,'faq.html')

# def sitemap(request):
#     return render (request,'sitemap.xml')

def blog_list(request):
    blogs = Post.objects.all().order_by('-created_at')  # Get all blogs ordered by latest
    paginator = Paginator(blogs, 8)  # 8 blogs per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)  # Get current page

    return render(request, 'blog.html', {'page_obj': page_obj})


def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        message = request.POST.get('message')

        contact_data=Contact(name=name,subject=subject,email=email,message=message)
        contact_data.save()



    return render (request,'contact.html')