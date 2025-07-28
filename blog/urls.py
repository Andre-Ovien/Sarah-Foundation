from django.urls import path
from . import views

urlpatterns =[
    path('blog/', views.BlogListCreateApi.as_view()),
    path('blog/<slug:slug>/', views.BlogDetailApi.as_view())
]