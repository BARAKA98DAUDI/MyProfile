from django.shortcuts import render
from .models import Profile

def profile_view(request):
    profile = Profile.objects.first()  # Assuming you'll have only one profile
    context = {
        'profile': profile,
    }
    return render(request, 'profile_app/profile.html', context)