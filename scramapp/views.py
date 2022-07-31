from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import ScramForm
from .models import scram
# Create your views here.
def home_view(request):
    
    user = request.user
    if user.is_anonymous:
        form = UserCreationForm()
        return render(request, 'scramapp/register_user.html', {'form':form})
        
    form = ScramForm
    my_notes = scram.objects.filter(user=request.user).order_by('-created_at')
    #print('user : ', request.user)
    #print('data : ', my_notes)
    
    if request.method == "POST":
        form = ScramForm(request.POST)
        
        if form.is_valid():
            
            plan = form.save(commit=False)
            plan.user = request.user
            plan.save()
            return redirect('home')
    
    
    context = {'form':form,'my_notes':my_notes}
    return render(request, 'scramapp/home.html', context)
    
def deletePlan(request, field_id):
    itemDel = scram.objects.get(pk = field_id)
    
    itemDel.delete()

    return redirect('home')

def publicScram(request):
    all_notes = scram.objects.filter(private = False).order_by('-created_at')
    #print(all_notes)
    context = {'all_notes':all_notes}
    return render(request, 'scramapp/public.html', context)

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("There was an error logging in"))
            return redirect('login')
    else:
        
        return render(request, 'scramapp/login.html', {})
    
def logout_user(request):
    logout(request)
    
    messages.success(request, ("You were logged out"))
    
    return redirect('home')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            
            user = authenticate(username=username, password=password)
            login(request,user)
            
            messages.success(request,("Register SUcces"))
            
            return redirect('home')
        
    else:
        form = UserCreationForm()
    
    
    return render(request, 'scramapp/register_user.html', {
        'form':form
    })
    
    

