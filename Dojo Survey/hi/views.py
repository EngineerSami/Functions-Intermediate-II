from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def result(request):
    if request.method == 'POST':
        print(request.POST) 
        name = request.POST['name']
        select = request.POST['select']
        return render(request, 'result.html', {'name': name, 'select': select})
    return render(request, 'index.html')
