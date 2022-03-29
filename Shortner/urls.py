from django.urls import path, include
from django.conf.urls.static import static
from django.views.generic import RedirectView
from . import views

urlpatterns = [
        path('', RedirectView.as_view(url='/shortner/')),
    path('shortner/', views.get_form, name='urlform')
]
