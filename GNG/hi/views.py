from django.shortcuts import  render, redirect
import random




def index(request):
    if 'number' not in request.session:
        request.session['number'] = random.randint(1, 100)
    
    if request.method == 'POST':
        guess = request.session['guess']
        
        if guess == request.session['number']:
            context = {'message' : "You guessed it! 🎉" }
            return render(request,'index.html', context, play_again=True)
        elif guess > request.session['number']:
            context = {'message' : "Too high! ⬆️" }
            return render(request,'index.html', context , play_again=False)
        else:
            context = {'message' : "Too low! ⬇️" }
            return render(request,'index.html', context , play_again=False)
        
    
    
    return render(request,'index.html')


def play_again(request):
    if 'guess' not in request.session:
        request.session['guess'] = request.POST['guess']
    print(request.POST['guess'])
    return redirect('/')

