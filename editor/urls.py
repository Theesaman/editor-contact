from django.urls import path
from .views import home_view,portfolio_view,about_view,books_view,contact_view,gallery_view,blog_single_view,ContactFormView

urlpatterns =[
    path('',home_view,name='home-page'),
    path('portfolio.html',portfolio_view,name='portfolio-page'),
    path('about.html',about_view,name='about-page'),
    path('books.html',books_view,name='book-page'),
    path('contact.html',ContactFormView.as_view(),name='contact-page'),
    path('index.html',home_view,name='index-page'),
    path('gallery.html',gallery_view,name='gallery-page'),
    path('blog-single.html',blog_single_view,name='blog_single_view-page'),



]