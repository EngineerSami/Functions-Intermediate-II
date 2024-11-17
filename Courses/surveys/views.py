from django.shortcuts import render, redirect, get_object_or_404
from django.core.exceptions import ValidationError
from .models import Course, CourseDescription

def index(request):
    courses = Course.objects.all()
    error_message = request.session.pop('error_message', None)  # Retrieve and clear any error messages
    return render(request, 'index.html', {'courses': courses, 'error_message': error_message})


def add_course(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        description = request.POST.get('description', '').strip()

        course = Course(name=name)
        course_description = CourseDescription(content=description)

        try:
            course.full_clean()
            course.save() 

            course_description.course = course 
            course_description.full_clean()
            course_description.save()

        except ValidationError as e:
            request.session['error_message'] = e.messages
            return redirect('index')

    return redirect('index')


def destroy_course(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'destroy.html', {'course': course})


def delete_course(request, id):
    if request.method == 'POST':
        course = get_object_or_404(Course, id=id)
        course.delete()
    return redirect('index')
