from django import forms
from authapp.models import User
class MyUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_employee', 'is_client')
        
    def __init__(self, *args, **kwargs):
        super(MyUserForm, self).__init__(*args, **kwargs)      
        self.fields['username'].required = True   
        self.fields['email'].required = True      
        self.fields['first_name'].required = True 
        self.fields['last_name'].required = True  
        self.fields['is_employee'].required = False 
        self.fields['is_client'].required = False
        self.fields['date_joined'].required=False   
        
    # def save(self, commit=True):
    #     # Get the instance but don't save it yet
    #     instance = super(MyUserForm, self).save(commit=False)

    #     # Only hash the password if it's being set
    #     if self.cleaned_data['password']:
    #         instance.password = make_password(self.cleaned_data['password'])
    #     else:
    #         # Keep the old password if none is provided
    #         instance.password = instance.password

    #     if commit:
    #         instance.save()

    #     return instance

 
class LoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
 
    
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField()   