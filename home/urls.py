from django.contrib import admin
from django.urls import path
from home import views

# urlpatterns = [
#     path("", views.index, name='home'),
#     path("about", views.about, name='about'),
#     path("services", views.services, name='services'),
#     path("contact", views.contact, name='contact'),
#     path("to_save", views.to_save, name='to_save'), 
# ]

urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("to_save", views.to_save, name='to_save'), 
    path("login", views.loginUser, name='login'),
    path('logout',views.logoutUser, name="logout"),
    #path('details',views.ContactList.as_view(),name="details"),
]