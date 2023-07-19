from django.db import models
from django.contrib.auth.models import User
import uuid
from datetime import datetime,timedelta
from django.urls import reverse

# Create your models here.

class ExtraUserInfo(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=10)
    choices = (('Male','Male'),('Female','Female'))
    gender = models.CharField(max_length=20,choices=choices)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    choices = (('Education','Education'),('Entertainment','Entertainment'),('Science','Science'))
    category = models.CharField(max_length=100,choices=choices)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['title']
    
    def get_absolute_url(self):
        return reverse('book_detail',kwargs={'pk':self.pk})
    
class BookInstance(models.Model):
    isbn = models.UUIDField(primary_key=True,default=uuid.uuid4)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.book.title} : {self.isbn}"
    class Meta:
        ordering = ['book']

    def get_absolute_url(self):
        return reverse('bookinstance_detail',kwargs={'pk':self.isbn})


    
def returnDate():
    return datetime.today() + timedelta(days=8)   
class IsseBook(models.Model):
    borrower = models.ForeignKey(User,on_delete=models.CASCADE)
    book_name = models.ForeignKey(BookInstance,on_delete=models.CASCADE)
    issue_date = models.DateField(auto_now=True)
    return_date = models.DateField(default=returnDate()) 

    def __str__(self):
        return f"{self.borrower} : {self.book_name.book.title} : {self.book_name.isbn}"