from django.shortcuts import render,redirect
from .forms import LoginForm,BookForm
# Create your views here.
def login(request):
    if request.method == "POST":
        filledform = LoginForm(request.POST)
        if filledform.is_valid():
            if request.POST["username"] == "rohith" and request.POST["password"] == "rohith":
                return redirect("home")
            else:
                return render(request, "login.html",{
                    'message':"Invalid Crendentials"
                })
        else:
            return render(request, "login.html",{
                'message':"Invalid Crendentials"
            })
    else:
        form = LoginForm()
        return render(request, "login.html",{
            'form':form
        })

def home(request):
    return render(request, "home.html")

def addBook(request):
    if request.method == "POST":
        filledform = BookForm(request.POST)
        if filledform.is_valid():
            filledform.save()
            return render(request, "home.html",{
                "message": "Book Added Successfully"
            })
        else:
            return render(request, "home.html",{
                "message": "Book was not Added. Please Try Again."
            })
    else:
        form = BookForm()
        return render(request, "addBook.html",{
            'form':form
        })