from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    # return HttpResponse("Fast forward")
    return render(request, 'about.html')

def projects(request):
    excluded = ['F', 'T', 'D', 'E', 'O', 'P']
    res = [chr(x).upper() for x in range(97, 123)]
    context = {
        'data': res,
        'excluded': excluded
    }
    return render(request, 'home/projects.html', context)

