from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.index),
    # path('users', views.create)
    # this will bring back to same html
    # add templates/actions
]