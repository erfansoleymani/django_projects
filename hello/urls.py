from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='hello'
urlpatterns = [
    # path('', TemplateView.as_view(template_name='hello/main.html')),
    # path('cookie', views.cookie),
    path('', views.sessfun),
]

