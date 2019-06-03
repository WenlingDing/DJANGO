from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Issue,Feature
from datetime import datetime

#login , register page form
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, widget=forms.PasswordInput)

class RegisterUserForm(UserCreationForm):
    
    # username = forms.CharField(label="User Name", help_text="No longer than 255 characters")
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    #clean_xxxx : where xxxx is the name of the field
    def clean_email(self):
        # get the username from the form
        username = self.cleaned_data.get('username')
        
        # get the email from the form as requesed_email
        requested_email = self.cleaned_data.get('email')
        
        # see if any current users is using that email
        if User.objects.filter(email=requested_email).count() > 0:
            raise forms.ValidationError("The email is already in use!")
            
        return requested_email
            
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
    
        if (password1 != password2):
            raise forms.ValidationError("Confirm password again!")
            
        return password2
        

class IssueForm(forms.ModelForm):
    # #   TYPE = (
    # #         ('1','bugs'),
    # #         ('2','feature requests'),
    #   type = forms.ChoiceField(widget=forms.Select(), choices=(
    #         ('1','bugs'),
    #         ('2','feature requests')),required=True)
      class Meta:
        model = Issue
        fields = ('subject', 'description')
      
       
    #   subject = forms.CharField(max_length=255, required=True)
    #   description = forms.CharField(max_length=255, required=True)
    #   date = forms.DateTimeField(initial=datetime.now(), required=False)
      def clean_description(self):
            description = self.cleaned_data.get('description')
            if len(description) <= 10:
                raise forms.ValidationError("Not enough content")
            return description
            
      def clean_subject(self):
            subject = self.cleaned_data.get('subject')
            subject = subject[0:50]
            return subject
               
class FeatureForm(forms.ModelForm):
      class Meta:
        model = Feature
        fields = ('subject', 'description')
        
      def clean_description(self):
            description = self.cleaned_data.get('description')
            if len(description) <= 10:
                raise forms.ValidationError("Not enough content")
            return description
            
      def clean_subject(self):
            subject = self.cleaned_data.get('subject')
            subject = subject[0:50]
            return subject
      
