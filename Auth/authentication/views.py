from django.shortcuts import render

# Create your views here.

#Home Page
def home(request):
    return render(request,"home.html")

#signup page
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})
