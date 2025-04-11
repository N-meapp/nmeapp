from django.core.paginator import Paginator
from django.shortcuts import render,redirect
from. models import*
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from cloudinary.uploader import upload
import cloudinary.uploader
from cloudinary.exceptions import Error
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

def privacy(request):
    return render (request,'privacy_nmeapp.html')



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



def blog_post(request):
    
    if request.method == "POST":
        card_head = request.POST.get('card_head')
        modal_head = request.POST.get('modal_head')
        card_paragraph = request.POST.get('card_paragraph')
        modal_paragraph = request.POST.get('modal_paragraph')
        keyword = request.POST.get('keyword')
        image = request.FILES.get('image')
        date = request.POST.get('date')
        cloudinary_response = cloudinary.uploader.upload(image)
        cloudinary_url = cloudinary_response.get("secure_url")

        blog_data = Post(card_head=card_head,modal_head=modal_head,card_paragraph=card_paragraph,modal_paragraph=modal_paragraph,keyword=keyword,image=cloudinary_url,date=date)
        blog_data.save()
        return HttpResponse("file saved!")
    else:
        return HttpResponse("cant save this instance!")
    

def admin_panel(request):
    if "name" in request.session:
        blog = Post.objects.all()
        contact = Contact.objects.all()

        context = {
            "blog":blog,
            "contact":contact
        }
        return render (request,'admin_panel.html',context)
    else:
        return redirect('login/')


def delete_blog(request,id):
    blog = Post.objects.get(id = id)
    if blog:
        blog.delete()
    else:
        return HttpResponse("cant delete this blog!")
    return redirect('dashboard')

def delete_message(request,id):
    contact = Contact.objects.get(id = id)
    if contact:
        contact.delete()
    else:
        return HttpResponse("cant delete this message!")
    return redirect('dashboard')


def admin_register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        raw_password = request.POST.get('subject')

        hashed_password = make_password(raw_password)

        login = Login(username=username, password=hashed_password)
        login.save()

    return render(request, 'admin_register.html')



def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        raw_password = request.POST.get('password')

        try:
            user = Login.objects.get(username=username)
        except Login.DoesNotExist:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

        if check_password(raw_password, user.password):
            request.session["name"] = username

            response = redirect('dashboard')
            response['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'

            return response
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})

    else:
        if "name" in request.session:
            print("Already logged in:", request.session['name'])
            return redirect('dashboard')
        else:
            print("Login attempt")
            response = render(request, 'login.html')
            response['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
            return response
