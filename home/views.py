from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime

from rest_framework import serializers
from home.models import Contact
from django.contrib import messages

from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login


from rest_framework.views import APIView
from rest_framework.response import Response
from home.serializers import ContactSerializer
from rest_framework import status
from django.shortcuts import get_list_or_404
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.permissions import IsAuthenticatedOrReadOnly

# Create your views here.
# def index(request):
#     var = {
#         "variable1":"test 1",
#         "variable2":"test 2"
#     } 
#     return render(request, 'index.html', var)
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')
 
def contact(request):
    return render(request, 'contact.html')

def to_save(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your details has been saved successfully.')
    return render(request, 'index.html')

def index(request):
    #print(request.user)
    if request.user.is_anonymous:
        return redirect("/login") 
    return render(request, 'index.html')

def loginUser(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)

        # check if user has entered correct credentials
        user = authenticate(username=username, password=password)

        if user is not None:
            # A backend authenticated the credentials
            login(request, user)
            return redirect("/")

        else:
            # No backend authenticated the credentials
            return render(request, 'login.html')

    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect("/login")


# class ContactList(APIView):

#     def get(self,request):
#         info=Contact.objects.all()
#         serializer=ContactSerializer(info,many=True)
#         return Response(serializer.data)
    
#     def post(self):
#         pass

class ContactCRUD(viewsets.ModelViewSet):
    queryset=Contact.objects.all()
    serializer_class=ContactSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]
    throttle_classes=[AnonRateThrottle,UserRateThrottle]