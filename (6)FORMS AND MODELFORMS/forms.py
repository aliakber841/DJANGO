from django import forms
from subscribe.models import Subscribe
from django.utils.translation import gettext_lazy as _

def validate_comma(value):
    if ',' in value:
        raise forms.ValidationError("Invalid Last name")
    return value

class SubscribeForm(forms.ModelForm):
    class Meta:
        model=Subscribe
        fields='__all__'
        #exclude=('first_name',)
        labels={
            'first_name':_("Enter First Name"),
             'last_name':_("Enter Last Name"),
              'email':_("Enter Email")
        }
        help_texts={
            'first_name':_("Enter characters only")
        }

        error_messages={
            'first_name':{
                'required':_('You cannnot move forward without first name')
            },
        }
        
        #fields=['first_name','last_name','email']
    # first_name=forms.CharField(max_length=100, required=False ,label="Enter first name",help_text="Enter character only")
    # last_name=forms.CharField(max_length=100, disabled=False,validators=[validate_comma])
    # email= forms.EmailField(max_length=100,validators=[validate_comma])

    # def clean_first_name(self):
    #     data=self.cleaned_data['first_name']
    #     if ',' in data:
    #         raise forms.ValidationError("Invalid First Name")
    #     return data