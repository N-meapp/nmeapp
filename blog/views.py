from django.core.paginator import Paginator
from django.shortcuts import render,redirect,get_object_or_404
from. models import*
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
from cloudinary.uploader import upload
import cloudinary.uploader
from cloudinary.exceptions import Error
from django.db.models import Q
from django.db.models.functions import Cast
from django.db.models import CharField
from django.urls import reverse
from django.contrib import messages



# Create your views here.
def base(request):
    return render(request, 'base.html')
def home(request):
    testimonials = Testimonial.objects.all()
    return render(request, "index.html", {"testimonials": testimonials})

def message(request):
    if request.method == "POST":
        try:
            Enquiry.objects.create(
                full_name=request.POST.get("full_name"),
                email=request.POST.get("email"),
                phone=request.POST.get("phone"),
                business_name=request.POST.get("business_name"),
                business_category=request.POST.get("business_category"),
                subject=request.POST.get("subject"),
                message=request.POST.get("message"),
            )
            return JsonResponse({"success": True})

        except Exception as e:
            return JsonResponse({
                "success": False,
                "errors": {"server": str(e)}
            }, status=400)

    return render(request, "message.html")

def about(request):
    # Get all team members from database
    team_members = TeamMember.objects.all()

    context = {
        "team_members": team_members
    }

    return render(request, 'about.html', context)
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

def blogs(request):
    query = request.GET.get('q', '').strip()

    blogs = Post.objects.all().order_by('-created_at')

    if query:
        date_filter = Q()

        # Try parsing date formats safely
        date_formats = [
    "%Y-%m-%d",      # 2026-01-09
    "%d-%m-%Y",      # 09-01-2026
    "%d/%m/%Y",      # 09/01/2026

    "%b %d %Y",      # Jan 09 2026
    "%b %d, %Y",     # Jan 09, 2026 ✅ NEW

    "%B %d %Y",      # January 09 2026
    "%B %d, %Y",     # January 09, 2026 ✅ NEW

    "%Y",            # 2026
]


        parsed_date = None
        for fmt in date_formats:
            try:
                parsed_date = datetime.strptime(query, fmt)
                break
            except ValueError:
                continue

        # If a valid date is found → filter created_at
        if parsed_date:
            if len(query) == 4:  # year only
                date_filter = Q(created_at__year=parsed_date.year)
            else:
                date_filter = Q(created_at__date=parsed_date.date())

        blogs = blogs.filter(
            Q(card_head__icontains=query) |
            Q(card_paragraph__icontains=query) |
            Q(keyword__icontains=query) |
            Q(modal_head__icontains=query) |
            Q(modal_paragraph__icontains=query) |
            Q(date__icontains=query) |   # text date (optional)
            date_filter
        ).distinct()

    paginator = Paginator(blogs, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'blog.html', {
        'page_obj': page_obj,
        'query': query
    })


def blog_detail(request, id):
    post = get_object_or_404(Post, id=id)

    # 👉 Latest 3 blogs (excluding current one – optional but recommended)
    latest_blogs = Post.objects.exclude(id=post.id).order_by('-created_at')[:3]

    return render(request, 'blog_detail.html', {
        'post': post,
        'latest_blogs': latest_blogs
    })






from django.http import JsonResponse
from .forms import ContactForm
# def contact(request):

#     if request.method == "POST":
#         name = request.POST.get('name')
#         subject = request.POST.get('subject')
#         email = request.POST.get('email')
#         message = request.POST.get('message')

#         contact_data=Contact(name=name,subject=subject,email=email,message=message)
#         contact_data.save()
#     return render (request,'contact.html')

def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'contact.html', {'form': ContactForm(), 'success': True})
        else:
            return render(request, 'contact.html', {'form': form})
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})


def contact_submit(request):
    if request.method == "POST":
        Contact.objects.create(
            name=request.POST.get("name"),
            email=request.POST.get("email"),
            phone=request.POST.get("phone"),
            subject=request.POST.get("subject"),
            message=request.POST.get("message"),
        )
        # redirect to your custom admin panel instead of contact page
        return redirect("dashboard")  # your admin_panel URL name
    return redirect("contact")


def delete_enquiry(request, id):
    if request.method == "POST":
        Contact.objects.filter(id=id).delete()  # delete the enquiry
    return redirect("dashboard")  # redirect to admin panel
 # reload admin panel

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

        blog_data = Post(
            card_head=card_head,
            modal_head=modal_head,
            card_paragraph=card_paragraph,
            modal_paragraph=modal_paragraph,
            keyword=keyword,
            image=cloudinary_url,
            date=date
        )
        blog_data.save()

        # Add message
        messages.success(request, "Blog added successfully!")
        return redirect('dashboard')  
def admin_panel(request):
    if "name" not in request.session:
        return render(request, 'login.html')

    blog = Post.objects.all()
    contact = Contact.objects.all()
    messages = Enquiry.objects.all().order_by("-created_at")
    team_members = TeamMember.objects.all()
    testimonials = Testimonial.objects.all().order_by('-id')

    # Get the page parameter from URL (default: dashboard)
    page = request.GET.get('page', 'dashboard')

    context = {
        "blog": blog,
        "contact": contact,
        "messages": messages,
        "team_members": team_members,
        "testimonials": testimonials,
        "page": page,
    }

    # ✅ THIS LINE WAS MISSING
    return render(request, "admin_panel.html", context)
def delete_message(request, id):
    if request.method == "POST":
        msg = get_object_or_404(Enquiry, id=id)
        msg.delete()
        return redirect("dashboard")
    return redirect("dashboard")  # redirect for GET requests


    
def add_testimonial(request):
    if request.method == "POST":
        name = request.POST.get('name')
        rating = request.POST.get('rating')
        opinion = request.POST.get('opinion')
        image = request.FILES.get('image')

        Testimonial.objects.create(
            name=name,
            rating=rating,
            opinion=opinion,
            image=image
        )
    return redirect('dashboard')  # or testimonials_page


def edit_testimonial(request, id):
    testimonial = Testimonial.objects.get(id=id)

    if request.method == "POST":
        testimonial.name = request.POST.get("name")
        testimonial.rating = request.POST.get("rating")
        testimonial.opinion = request.POST.get("opinion")

        if request.FILES.get("image"):
            testimonial.image = request.FILES.get("image")

        testimonial.save()
        return redirect("dashboard")  # change if needed



# Delete testimonial
def delete_testimonial(request, id):
    testimonial = get_object_or_404(Testimonial, id=id)
    testimonial.delete()
    return redirect('dashboard')
def add_team_member(request):
    if request.method == "POST":
        TeamMember.objects.create(
            name=request.POST.get("name"),
            designation=request.POST.get("designation"),
            sentence=request.POST.get("sentence"),
            photo=request.FILES.get("photo"),
        )
    return redirect("dashboard")  # ✅ FIXED


def update_team_member(request, id):
    member = get_object_or_404(TeamMember, id=id)

    if request.method == "POST":
        member.name = request.POST.get("name")
        member.designation = request.POST.get("designation")
        member.sentence = request.POST.get("sentence")

        if request.FILES.get("photo"):
            member.photo = request.FILES.get("photo")

        member.save()

    return redirect("dashboard")  # ✅ FIXED


def delete_team_member(request, id):
    member = get_object_or_404(TeamMember, id=id)
    member.delete()
    return redirect("dashboard")  # ✅ FIXED

def update_blog(request):
    if request.method == 'POST':

        blog_id = request.POST.get('id')
        if not blog_id:
            return HttpResponse("Blog ID missing", status=400)

        blog = get_object_or_404(Post, id=blog_id)

        # Update text fields
        blog.card_head = request.POST.get('card_head')
        blog.modal_head = request.POST.get('modal_head')
        blog.card_paragraph = request.POST.get('card_paragraph')
        blog.modal_paragraph = request.POST.get('modal_paragraph')
        blog.keyword = request.POST.get('keyword')
        blog.date = request.POST.get('date')

        # Image update
        new_image = request.FILES.get('image')
        if new_image:
            # delete old image safely
            if blog.image:
                cloudinary.uploader.destroy(blog.image.public_id)

            uploaded = cloudinary.uploader.upload(new_image)
            blog.image = uploaded['secure_url']

        blog.save()
        return redirect('dashboard')

    return redirect('dashboard')
        

     

def delete_blog(request, id):
    blog = get_object_or_404(Post, id=id)

    # delete image from cloudinary
    if blog.image:
        public_id = blog.image.public_id
        cloudinary.uploader.destroy(public_id)

    blog.delete()
    return redirect('dashboard')

def delete_contact(request,id):
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


from django.utils import timezone
from datetime import timedelta
from datetime import datetime
def login(request):
    print("Login view HIT!", request.method)
    if request.method == 'POST':
        username = request.POST.get('username')
        raw_password = request.POST.get('password')

        print(username, raw_password)
        if "name" in request.session:
            print('haaaaaaiiii')
        else:
            print('loggiinnn pageee')

        holder = Login.objects.first()

        current_time = timezone.now()
        if holder.last_failed_login is not None:
            if timezone.is_naive(holder.last_failed_login):
                # Assume naive datetime is in your current timezone (e.g., Asia/Kolkata)
                aware_last_failed_login = timezone.make_aware(holder.last_failed_login, timezone.get_current_timezone())
            else:
                aware_last_failed_login = holder.last_failed_login

            if current_time < aware_last_failed_login + timedelta(hours=2) and holder.rate_limit == 5:
                print('Wait for a 2 hour time period')
                return render(request, 'login.html', {'ratelimit': True})
        
            else:
                if holder.rate_limit >=5:
                    holder.rate_limit = 0
                    holder.save()
                
                try:
                    user = Login.objects.get(username=username)
                except Login.DoesNotExist:
                    holder.rate_limit +=1
                    holder.last_failed_login = timezone.now()
                    holder.save()
                    return render(request, 'login.html', {'show_alert': True})
                    # return render(request, 'login.html', {'show_alert': True})

                
                if check_password(raw_password, user.password):
                    request.session["name"] = username
                    # print(request.session['name'],'nameeeeee')
                    holder.rate_limit = 0
                    holder.save()
                    response = redirect('dashboard')
                    response['Cache-Control'] = 'no-store, no-cache, must-revalidate, proxy-revalidate'
                    response['Pragma'] = 'no-cache'
                    response['Expires'] = '0'
                    print("Login successful, session name:", request.session.get("name"))

                    return redirect('dashboard')
                else:
                    holder = Login.objects.first()
                    
                    holder.rate_limit +=1
                    holder.last_failed_login = timezone.now()
                    holder.save()
                    # print('the rate limit :',user.rate_limit)
                    return render(request, 'login.html', {'error': 'Invalid credentials'})
        else:
            holder.last_failed_login = current_time
            holder.save()
            return redirect('login')

    else:
        if "name" in request.session:
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
    return redirect('login')
