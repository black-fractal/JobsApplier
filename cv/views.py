from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
import django.contrib.auth as dj_auth


# Create your views here.
from cv.api.linkedin_django import get_auth_url, get_auth_access_token, get_application
from cv.api.voyager import get_info
from cv.models.Login import LoginForm
from cv.models.Signup import SignupForm
from cv.models.Userprofile import Userprofile


def index(request):
    # if request.method == "POST":
    #     profile_id = request.POST.get('profile_id', '')
    #     if profile_id:
    # url = get_auth_url()
    # print(url)
    # return render(request, 'index.html', {"url": url})
    return cv(request)


def code(request):
    # auth_code = request.GET.get('code', '')
    # application = get_application(get_auth_access_token(auth_code))
    # # print(application.get_connections())
    # print(application.get_profile(selectors=['id', 'first-name', 'last-name', 'location', 'distance', 'skills', 'educations']))
    # print(application.get_skills())
    # return render(request, 'index.html', {"url": ""})
    return cv(request)


def login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    elif request.method == "POST":
        f = LoginForm(data=request.POST)
        if f.is_valid():
            username = f.cleaned_data.get('username')
            password = f.cleaned_data.get('password')
            user = dj_auth.authenticate(username=username, password=password)
            if user is not None:
                dj_auth.login(request, user)
                return HttpResponseRedirect('/')
    else:
        f = LoginForm()
    return render(request, 'registration/login.html', {'form': f})


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/')
    elif request.method == "POST":
        f = SignupForm(request.POST)
        if f.is_valid():
            f.save()
            username = f.cleaned_data['username']
            new_user = User.objects.get(username=username)
            prof = Userprofile(user=new_user)
            prof.save()
            return redirect('login')
    else:
        f = SignupForm()
    return render(request, 'registration/signup.html', {'form': f})


def cv(request):
    if request.user.is_authenticated:
        skills = Userprofile.objects.filter(user=request.user)[0].skills
        educations = Userprofile.objects.filter(user=request.user)[0].education
        experiences = Userprofile.objects.filter(user=request.user)[0].experience
        if skills:
            skills = skills.split(',')
        if experiences:
            experiences = experiences.split(',')
        if educations:
            educations = educations.split(',')
        info = {"skills": skills, "educations": educations, "experiences": experiences}
        print(info)
        if request.method == "POST":
            username = request.POST.get('username', '')
            if username:
                prev_info = Userprofile.objects.get(user=request.user)
                info = get_info(username)
                prev_info.skills = ','.join(info['skills'])
                prev_info.education = ','.join(info['educations'])
                print(info['experiences'])
                prev_info.experience = ','.join(info['experiences'])
                prev_info.save()

        return render(request, 'cv.html', info)
    else:
        return HttpResponseRedirect('/login')
