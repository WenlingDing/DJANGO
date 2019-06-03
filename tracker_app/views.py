from django.db import models
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import Issue,Feature
from .forms import LoginForm, RegisterUserForm, IssueForm,FeatureForm

# user register and login, logout 
# def index(request):
#     return render(request, 'index.html')
    
def login(request):
    if request.method == 'POST':
        # extract the user name from the form
        form_username = request.POST.get('username')
        # extract the password from the form
        password = request.POST.get('password')
        # then we check if the user name and password are correct 
        # i.e if both exists in the database
        user = auth.authenticate(username=form_username, password=password)
        # if user is not None, then redirect
        submitted_login_form = LoginForm(request.POST)
        if user is not None:
            # actually logs in the user
            auth.login(user=user, request=request)
            messages.success(request, "Welcome back")
            return redirect(home)
        else:
            messages.error(request, "Invalid Login")
            return render(request, 'login.html', {
            'form':submitted_login_form
        })
    else:
        login_form = LoginForm()
        return render(request, 'login.html', {
            'form':login_form
        })
        
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You have logged out")
    return redirect(home) 
 
def register(request):
    if request.method == "POST":
        # process the creation
        # recreate the form with whatever data the user has keyed in
        register_form = RegisterUserForm(request.POST)
         # check if the form is valid
        if register_form.is_valid():
            # save the user
            register_form.save()
            # will show the message after the redirect
            messages.success(request, "Your account has been created!")
            return redirect(home)
        else:
            messages.error(request, "Unable to register your account")
            return render(request, 'register.html', {
              'form':register_form
            })
    else:
        register_form = RegisterUserForm()
        return render(request, 'register.html', {
            'form':register_form
        })
        
def home(request):
    issues = Issue.objects.all()
    return render(request, 'home.html',{'all_issue':issues})
 
def feature(request):
    feature = Feature.objects.all()
    return render(request, 'feature.html',{'all_feature':feature})
    
# def issues(request,type=None):
#     if type=='bug':
#     #showing in home page all issues that are type='bug'
#       issues = Issue.objects.filter(type='bug')
#     elif type=='feature':
#       issues = Issue.objects.filter(type='feature')
#     return render(request,'home.html',{'issues':issues})



#user add issue form
@login_required
def add_bug(request):
    if  request.method=="POST":
        add_form=IssueForm(request.POST)
        if add_form.is_valid():
            new_issue=Issue(
                user=request.user
                )
            new_issue=add_form.save()
            # new_issue.user = request.user  # The logged-in user
            add_form.save()
            return redirect('home')
        else:
            return render(request, 'add_bug.html',{
               'form' : add_form
            })
    else:
        add_form=IssueForm()
        return render(request, 'add_bug.html',{
               'form': add_form
            })

@login_required
def add_feature(request):
    if  request.method=="POST":
        add_feature_form=FeatureForm(request.POST)
        if add_feature_form.is_valid():
            new_issue=Feature(user=request.user
                            )
            new_issue = add_feature_form.save(commit=False)
            return redirect('feature')
        else:
            return render(request, 'add_feature.html',{
               'form' : add_feature_form
            })
    else:
        add_feature_form=FeatureForm()
        return render(request, 'add_feature.html',{
               'form': add_feature_form
            })
            
@login_required
def edit_bug(request,id):
    issue = get_object_or_404(Issue,pk=id)
    if request.method=="POST":
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            return render(request,'edit_bug.html',{
                'form':form
            }) 
    else:
        form = IssueForm(instance=issue)
        return render(request,'edit_bug.html',{
            'form':form
        })
        
@login_required
def edit_feature(request,id):
    issue = get_object_or_404(Feature,pk=id)
    if request.method=="POST":
        form = FeatureForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('feature')
        else:
            return render(request,'edit_feature.html',{
                'form':form
            }) 
    else:
        form = FeatureForm(instance=issue)
        return render(request,'edit_feature.html',{
            'form':form
        })
        
@login_required           
def delete_bug(request,id):
    issue = get_object_or_404(Issue,pk=id)
    if request.method=="POST":
        issue.delete()
        return redirect(home)
    else:
        return render(request,'delete_bug.html',{
            'delete_item':issue
        })






