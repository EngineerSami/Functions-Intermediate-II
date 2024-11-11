from django.shortcuts import  render, redirect


def gng(request):
    if 'visit_count' in request.session:
        request.session['visit_count'] += 1
    else:
        request.session['visit_count'] = 1
    return render(request, 'index.html')

def destroy_session(request):
    request.session.clear()
    return redirect('/')