from django.conf.urls import url
from .views import view_profile

urlpatterns = [
    
    url(r'^user/', view_profile, name="profile")
    
    ]