from django.shortcuts import render

# Create your views here.

#Home Page
def home(request):
    return render(request,"home.html")

#signup page
def user_signup(request):
    