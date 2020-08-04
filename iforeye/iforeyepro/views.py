from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Book, Volunteer, Ngo_details, Recording
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'home.html')


def NGOreg(request):
    return render(request, 'NGO_reg.html')


def volreg(request):
    return render(request, 'Vol_reg.html')



def login(request):
    return render(request, 'login.html')

def loginvol(request):
    return render(request,'loginvol.html')

def about(request):
    return render(request,'about.html')


def audio(request,name):
    if request.method == "POST":
        audio=request.POST.get('audio')
        # name=request.POST.get('name')
        # print(name)
        # print("*******")
        # book1=
        book1 = Book.objects.all()
        for x in book1:
            if x.name==name:
                ngo=Recording(name=x, audio_file=audio,)
                ngo.save()
                # print(x.name)
                return render(request, 'home.html')
    return render(request,'home.html')

def selectaudio(request,name):
    # if request.method == "POST":
    recording=Recording.objects.all()
    # print(name)
    # print("((((((((")
    # print(recording)
    li = []
    for x in recording:
        # print("*****")
        # print(x.name)
        # print(name)
        # print("******")
        # print(x.audio_file)
        if x.name.name==name:
            # print("HIIIIII")
            li.append(x)
            # print(li)
        # print("nnnnnnnnn")
    # print(li)
    print("*****")
    return render(request,'Audios_screen .html',{'li': li,'name':name})


def dbbook(request):
    if request.method == "POST":
        name=request.POST.get('booktitle')
        file=request.POST.get('file')
        # name=request.POST.get('name')
        # print(name)
        # print("*******")
        # book1=
        book2=Book(name=name,author='harsha',jonour='harsha',language='harsha',text_file=file)
        book2.save()

    return render(request,'home.html')

def finalselect(request,name,name1):
    if request.method == "POST":
        print(name)
        print(name1)
        # print(i)
        # print(i)
        # name=request.POST.get('booktitle')
        # file=request.POST.get('file')
        # name=request.POST.get('name')
        # print(name)
        # print("*******")
        # book1=
        # book2=Book(name=name,author='harsha',jonour='harsha',language='harsha',text_file=file)
        # book2.save()

    return render(request,'home.html')

def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # print(name)
        # print(email)
        ngo = Ngo_details(name=name, phone=phone_number, email=email, password=password)
        ngo.save()
    return render(request, 'home.html')

def booksupload(request):
    return render(request,'Book_upload.html')

def Volunteers(request):
    if request.method == "POST":
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        age = request.POST.get('age')
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(name)
        print(email)
        print(phone_number)
        print(password)
        print(age)
        vol = Volunteer(name=name, age=age, phone=phone_number, email=email, password=password)
        vol.save()
    return render(request, 'home.html')


def login_view(request):
    if request.method == 'POST':
        u_name = request.POST.get('email')
        u_pass = request.POST.get('password')
        ngo = Ngo_details.objects.all()
        print(u_name)
        print(u_pass)
        # print(ngo)
        flag = 0
        for x in ngo:
            # print(x.name)
            # print(x.password)
            if x.name == u_name and x.password == u_pass:
                flag = 1
                break
        print(flag)
        if flag == 1:
            book = Book.objects.all()
            return render(request, 'NGO.html',{'book':book})

    return render(request, "login.html")

def loginvolun(request):
    if request.method == 'POST':
        u_name = request.POST.get('email')
        u_pass = request.POST.get('password')
        ngo = Volunteer.objects.all()
        print(u_name)
        print(u_pass)
        # print(ngo)
        flag = 0
        for x in ngo:
            # print(x.name)
            # print(x.password)
            if x.name == u_name and x.password == u_pass:
                flag = 1
                break
        print(flag)
        if flag == 1:
            book=Book.objects.all()

            return render(request, 'Volunteer.html',{'book':book})

    return render(request, "login.html")


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))
