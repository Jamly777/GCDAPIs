from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns=[
    path('test/',views.Test.as_view()),
    path('series/',views.series.as_view()),
    path('booknames/',views.bookname.as_view()),
    path('brief/',views.brief.as_view()),
    path('chapternames/',views.chapternames.as_view()),
    path('article/',views.Article.as_view())
]