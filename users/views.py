from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile


# Create your views here.

def view_profile(request, profile_id):
    try:
        profile = Profile.objects.get(pk=profile_id, profile_id=User)
        
        if profile.is_active:
            return profile
        return None
    except Profile.DoesNotExist:
        return None
        