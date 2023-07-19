from django.urls import path
from . import views

urlpatterns = [
    # path('',views.login,name="login"),
    path('home/',views.home,name="home"),
    path('register/',views.register,name="register"),
    path('addBook/',views.AddBook.as_view(),name="add"),
    path('addInstance/',views.AddInstance.as_view(),name="addInstance"),
    path('issueBook/',views.IssueBookInstance.as_view(),name="issue"),
    path('viewissued/',views.viewIssuedBooks,name='view'),
    path('book_detail/<int:pk>',views.BookDetail.as_view(),name="book_detail"),
    path('bookinstance_detail/<pk>',views.BookInstanceDetail.as_view(),name="bookinstance_detail")
]