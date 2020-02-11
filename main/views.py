from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def show_color(request):
    colors = {
        'user_color' : request.session['user_color'],
        'first_name' : request.session['first_name'],
        'my_color': 'green'
    }
    return render(request, 'show_color.html', colors)

def process_color(request):
    print(request.POST['color'])
    request.session['user_color'] = request.POST['color']
    request.session['first_name'] = request.POST['first_name']
    return redirect('/show_color')
