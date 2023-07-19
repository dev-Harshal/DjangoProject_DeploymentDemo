from django.shortcuts import render,redirect
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from . models import ExtraUserInfo,Book,BookInstance,IsseBook
from django.views.generic import CreateView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

def login(request):
    return redirect('login')
    
def home(request):
    return render(request,'library/home.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        mobile = request.POST.get('mobile')
        gender = request.POST.get('gender')
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        try:
            user = User.objects.get(username=username)
            return render(request,'library/register.html',{'error':"User Exists"})
        except:
            if password1 != password2:
                return render(request,'library/register.html',{'error':"Password Not Matching"})
            else:
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password1)
                ExtraUserInfo.objects.create(user=user,mobile=mobile,gender=gender)
                return redirect('login')
    else:
        return render(request,'library/register.html',{'error':""})
    
class AddBook(LoginRequiredMixin,CreateView):
    model = Book
    fields = '__all__'
    # success_url = reverse_lazy('home')

class AddInstance(CreateView):
    model = BookInstance
    fields = '__all__'
    # success_url = reverse_lazy('view')


class IssueBookInstance(CreateView):
    model = IsseBook
    fields = ['borrower','book_name']
    success_url = reverse_lazy('view')
    


@login_required
def viewIssuedBooks(request):
    books =IsseBook.objects.all()
    return render(request,'library/viewissuedbooks.html',{'books':books})

class BookDetail(DetailView):
    model = Book

class BookInstanceDetail(DetailView):
    model = BookInstance



