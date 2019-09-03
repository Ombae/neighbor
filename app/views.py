from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import PostComment,PostImageForm,PostProfile
from .models import Images, Profiles, Comments

# Create your views here.
@login_required(login_url='/accounts/register/')
def index(request):
    images = Images.get_all_images()
