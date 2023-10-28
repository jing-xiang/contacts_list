# STEP 3: CREATE NEW FORM TO ADD BOOK TO RECORDS

from django import forms
from .models import Contacts

class ContactsForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ['name', 'number']
