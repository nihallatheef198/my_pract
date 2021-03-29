from django.shortcuts import render
from django.views import generic
from django.http import HttpResponse
# Create your views here.
import random

def password_gen(request):
    return render(request,'pwdgen_app/home.html')

def about(request):
    return render(request,'pwdgen_app/about.html')

def password_view(request):
    char_set = 'abcdefghijklmnopqrstuvwxyz'
    password = ''
    len = int(request.POST.get('len'))

    if request.POST.get('caps'):
        char_set += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if request.POST.get('schr'):
        char_set += '!@#$%^&*'
    if request.POST.get('num'):
        char_set += '1234567890'

    for i in range(len):
        password += random.choice(char_set)

    return render(request,'pwdgen_app/password.html',{'password':password})
