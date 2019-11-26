from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "home.html")
    
    
def view_bid(request):
    # A view that render bid page for user
    if request.user.is_authenticated:
        return render(request, "bid.html")
    else:
        return "Please SignIn or Register to bid"
    