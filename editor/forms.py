# form lar ikki xil bo'ladi oddiy form va Modelform
from typing import Any
from django import forms
from django.forms import ModelForm
from .models import Contact

# class ContactForm(forms.Form):
#     name = forms.CharField(max_length=50)
#     email = forms.EmailField(max_length=50)
#     contect = forms.Textarea()

class ContactForm(ModelForm):
    class  Meta:
        model = Contact
        fields = ["name","email","contect"]

    def clean(self):
 
        # data from the form is fetched using super function
        super(ContactForm, self).clean()
         
        # extract the username and text field from the data
        name = self.cleaned_data.get('name')
        email = self.cleaned_data.get('email')
        content = self.cleaned_data.get('contect')

        # conditions to be met for the username length
        if name:
            if len(name) < 3:
                self._errors['name'] = self.error_class([
                    'Minimum 3 characters required'])
                
        else:
            self._errors['name'] = self.error_class([
                    'nami is required'])
            
        if email:  
           if len(email) <8:
                self._errors['email'] = self.error_class([
                    'there should be at least 8 emails'])
                
        else:
            self._errors['email'] = self.error_class([
                    'email is required'])
            
                
        if content:  
           if len(content) <10:
                self._errors['context'] = self.error_class([
                    'there should be at least 10 world'])
 
        else:
            self._errors['content'] = self.error_class([
                    'content is required'])
 
        # return any errors if found
        return self.cleaned_data
        
