from django.shortcuts import render
from .forms import ContactForm
from django.views.generic.edit import FormView

class ContactFormView(FormView):
    template_name = "contact.html"
    form_class = ContactForm
    success_url = 'index.html'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    




# Create your views here.

def contact_view(request):
    return render(request=request,template_name='contact.html')

def home_view(request):
    return render(request=request, template_name='index.html')

def portfolio_view(request):
    return render(request=request, template_name='portfolio.html')

def about_view(request):
    return render(request=request,template_name='about.html')
    
def books_view(request):
    return render(request=request, template_name='books.html')

def gallery_view(request):
    return render(request=request,template_name='gallery.html')

def blog_single_view(request):
    return render(request=request,template_name='blog-single.html')