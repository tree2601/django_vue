from django.urls import path
from . import views

urlpatterns = [
    path('CainiaoBased/', views.CainiaoBasedOption.as_view()),
    path('Designlist/', views.DesignlistOption.as_view()),
    path('UserLike/', views.UserLikeOption.as_view()),
    path('Word/', views.WordOption.as_view()),
    path('findAllWorld/', views.findAllWorld.as_view()),
    path('gitintiitle/', views.gitintiitle.as_view()),
    path('gitinintiitle/', views.gitinintiitle.as_view()),
    path('gitcontent/', views.gitcontent.as_view()),
    path('putlike/', views.putlike.as_view()),
    path('getlikebyid/', views.getlikebyid.as_view()),
    path('getNameByname/', views.getNameByname.as_view()),
    path('getcainiao/', views.getcainiao.as_view()),
    path('getTuijianForUser/', views.getTuijianForUser.as_view()),
    path('getname/', views.getname.as_view()),
    path('TitleCount/', views.TitleCountOption.as_view()),
    path('TitleCountAll/', views.TitleCountAll.as_view()),
    path('getAllWord/', views.getAllWord.as_view()),
    path('getAllWordByc/', views.getAllWordByc.as_view()),

]
    