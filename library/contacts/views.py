from django.shortcuts import render, redirect, get_object_or_404
from .models import Contacts
from .forms import ContactsForm

# Create your views here.
def contact_list(request):
    contacts = Contacts.objects.all()
    return render(request, 'contacts/contact_list.html', {'contacts': contacts})

def contact_create(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_list')
    else:
        form = ContactsForm()
    return render(request, 'contacts/contact_form.html', {'form': form})

def contact_delete(request, contact_id):
    book = get_object_or_404(Contacts, pk=contact_id)
    book.delete()
    return redirect('contacts_list')
