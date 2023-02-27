from django.urls import path

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView)

from authApp import views


urlpatterns = [
    path('refresh/', TokenRefreshView.as_view()),
    path('login/', TokenObtainPairView.as_view()),

    path('user/', views.UserCreateView.as_view()),
    path('user/<int:pk>/', views.UserDetailView.as_view()),
    path('user_list/', views.UserListView.as_view()),

    path('news/', views.NewsCreateView.as_view()),
    path('news_list/', views.NewsListView.as_view()),
    path('news/<int:pk>/', views.NewsDetailView.as_view()),
    path('news/update/<int:owner>/<int:pk>/', views.NewsUpdateView.as_view()),
    path('news/delete/<int:owner>/<int:pk>/', views.NewsDeleteView.as_view()),

    path('comment/', views.CommentCreateView.as_view()),
    path('comment_list/', views.CommentListView.as_view()),
    path('comment/update/<int:owner>/<int:notica>/<int:pk>/', views.CommentUpdateView.as_view()),
    path('comment/delete/<int:owner>/<int:notica>/<int:pk>/', views.CommentDeleteView.as_view())
]