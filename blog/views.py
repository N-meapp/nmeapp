from django.core.paginator import Paginator
from django.shortcuts import render,redirect,get_object_or_404
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
        print("Dashboard accessed, session name:", request.session.get("name"))
        return render (request,'admin_panel.html',context)

    else:
        print("No session found, returning simple response")
        # return HttpResponse("You are not logged in.")
        return render(request, 'login.html')

def update_blog(request):
    if request.method == 'POST':
        blog_id = request.POST.get('id')
        print(f"Received blog ID: {blog_id}")
        if not blog_id:
            return HttpResponse("Blog ID not received", status=400)
        
        blog = get_object_or_404(Post, id=blog_id)
        
        # Update text fields
        blog.card_head = request.POST.get('card_head')
        blog.modal_head = request.POST.get('modal_head')
        blog.card_paragraph = request.POST.get('card_paragraph')
        blog.modal_paragraph = request.POST.get('modal_paragraph')
        blog.keyword = request.POST.get('keyword')

        # Check for new image
        new_image = request.FILES.get('image')
        if new_image:
            # Extract public_id from existing image URL
            if blog.image:
                try:
                    public_id = blog.image.split("/")[-1].split(".")[0]
                    cloudinary.uploader.destroy(public_id)
                except Exception as e:
                    print(f"Error deleting old image: {e}")

            # Upload new image
            cloudinary_response = cloudinary.uploader.upload(new_image)
            cloudinary_url = cloudinary_response.get("secure_url")
            blog.image = cloudinary_url

        blog.save()
        return redirect('dashboard')

    return redirect('dashboard')

        

     

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
    print("Login view HIT!", request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        raw_password = request.POST.get('password')

        print(username, raw_password)

        try:
            user = Login.objects.get(username=username)
        except Login.DoesNotExist:
            return render(request, 'login.html', {'show_alert': True})

        
        if check_password(raw_password, user.password):
            request.session["name"] = username

            response = redirect('dashboard')
            response['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
            response['Pragma'] = 'no-cache'
            response['Expires'] = '0'
            print("Login successful, session name:", request.session.get("name"))

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
        

def logout(request):
    request.session.flush()  # Clears all session data
    return render(request, 'login.html',)
