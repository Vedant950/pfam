from django.shortcuts import render, redirect
from django.conf import settings
from datetime import datetime
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import MyUser, Pet, DaySchedule, TimeSchedule
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import login, logout, authenticate

# Create your views here.
def home(request):
    return render(request, 'base/home.html')

def ourProduct(request):
    return render(request, 'base/our-product.html')

def aboutUs(request):
    return render(request, 'base/about-us.html')

@login_required(login_url='login')
@csrf_protect 
def scheduler(request, pk):
    q = request.GET.get('q') if request.GET.get('q') != None else None
    if q == "add-pet": return redirect('add-pet', pk=pk)
    pets = Pet.objects.filter(user=User.objects.get(username=pk))

    if request.method == 'POST':
        days = ['sun', 'mon', 'tue', 'wed', 'thru', 'fri', 'sat']
        if DaySchedule.objects.filter(pet = pets.get(name=q)).exists():
            data = {}
            daySchedule = DaySchedule.objects.get(pet = pets.get(name=q))
            data["sun"] = daySchedule.sun_id
            data["mon"] = daySchedule.mon_id
            data["tue"] = daySchedule.tue_id
            data["wed"] = daySchedule.wed_id
            data["thru"] = daySchedule.thr_id
            data["fri"] = daySchedule.fri_id
            data["sat"] = daySchedule.sat_id
            for day in days:
                schedule = request.POST.getlist(day)[0].split(",")[:-1]
                timeSchedule = TimeSchedule.objects.get(id=data[day])
                timeSchedule.m0 = schedule[0]
                timeSchedule.m3 = schedule[1]
                timeSchedule.m6 = schedule[2]
                timeSchedule.m9 = schedule[3]
                timeSchedule.m12 = schedule[4]
                timeSchedule.m15 = schedule[5]
                timeSchedule.m18 = schedule[6]
                timeSchedule.m21 = schedule[7]
                timeSchedule.save()
        else:
            data = {}
            for day in days:
                schedule = request.POST.getlist(day)[0].split(",")[:-1]
                timeSchedule = TimeSchedule.objects.create(
                    m0 = schedule[0],
                    m3 = schedule[1],
                    m6 = schedule[2],
                    m9 = schedule[3],
                    m12 = schedule[4],
                    m15 = schedule[5],
                    m18 = schedule[6],
                    m21 = schedule[7]
                )
                data[day] = timeSchedule     
                
            daySchedule = DaySchedule.objects.create(
                pet = Pet.objects.get(user=User.objects.get(username=pk), name=q),
                sun = data["sun"],
                mon = data["mon"],
                tue = data["tue"],
                wed = data["wed"],
                thr = data["thru"],
                fri = data["fri"],
                sat = data["sat"]
            )
    try:
        shed = DaySchedule.objects.get(pet = pets.get(name=q))
    except:
        shed = None

    context = {
        "pets": pets,
        "q": q,
        "schedule" : shed,
    }
    return render(request, 'base/scheduler.html', context)

@login_required(login_url='login')
@csrf_protect 
def status(request, pk):
    q = request.GET.get('q') if request.GET.get('q') != None else None
    if q == "add-pet": return redirect('add-pet', pk=pk)
    pets = Pet.objects.filter(user=User.objects.get(username=pk))
    context = {
        "pets": pets,
        "q": q,
    }
    return render(request, 'base/status.html', context)
    
@login_required(login_url='login')
@csrf_protect 
def addPet(request, pk):
    if request.method == 'POST':
        user = User.objects.get(username=pk)
        name = request.POST.get("name")
        if Pet.objects.filter(user=user).filter(name=name).exists():
            messages.info(request, "You have already added a pet with that name.")
            return redirect("add-pet", pk=pk)
        dob = datetime.fromisoformat(request.POST.get("dob"))
        today = datetime.now()
        age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
        pet = Pet.objects.create(
                user = user,
                name = name,
                dob = dob,
                age = age,
                type = request.POST.get("type").lower(),
                breed = request.POST.get("breed"),
                add_breed = request.POST.get("add-breed"),
                gender = request.POST.get("gender"),
                height = int(request.POST.get("height")),
                weight = int(request.POST.get("weight")),
                meal = request.POST.get("meal"),
                allergies = request.POST.get("allergies"),
                dislike = request.POST.get("dislike"),
                prefer_food = request.POST.get("prefered-food"),
                activity = request.POST.get("activity"),
                help_required = request.POST.get("help-required")
        )
        return redirect("scheduler", pk=pk)

    return render(request, 'base/add-pet.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']
        send_mail(
            "There ia query from your website", 
            f"Hi! {name} here, {message}. contact me on Email-{email}, Ph-{number}", 
            settings.EMAIL_HOST_USER, 
            ["email@email.com"], 
            False
        )
    return render(request, 'base/contact-us.html')

def userLogin(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        if request.POST.get('signIn'):
            email = request.POST.get('login_email')
            password = request.POST.get('login_password')
            try:
                username = MyUser.objects.get(email=email).username
            except:
                messages.info(request, "User does not exist")
                return redirect('login')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                messages.info(request, "Invalid Credintials")
                return redirect('login')

        elif request.POST.get('signUp'):
            name = request.POST['name']
            username = request.POST['username']
            email = request.POST['email']
            password1 = request.POST['password1']
            password2 = request.POST['password2']
            if password1 == password2:
                if MyUser.objects.filter(email=email).exists():
                    messages.error(request, "Email already Used")
                    return redirect('login')
                elif User.objects.filter(username=username).exists():
                    messages.error(request, "Username already Used")
                    return redirect('login')
                else:
                    user = User.objects.create_user(username=username, password=password1)
                    user.save()
                    myuser = MyUser.objects.create(
                            user=user, 
                            name=name, 
                            email=email,
                            username=username,
                        )
                    login(request, user)
                    return redirect('home')
            else:
                messages.error(request, "Password does not match")
                return redirect('login')
        else:
            messages.error(request, "An error occured during registraion")
            return redirect('login')

    return render(request, 'base/login.html')

def userLogout(request):
    logout(request)
    return redirect('home')

def resetPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            try:
                user = MyUser.objects.get(email=email).user
            except:
                messages.info(request, "User does not exist")
                return redirect('reset-password')
            if user is not None:
                user.set_password(password1)
                user.save()
                messages.info(request, "Password Reset Successful")
                return redirect('login')
            else:
                messages.info(request, "An error occured during password reset")
        else:
            messages.info(request, "Password does not match")
            return redirect('reset-password')
    return render(request, 'base/reset-password.html')