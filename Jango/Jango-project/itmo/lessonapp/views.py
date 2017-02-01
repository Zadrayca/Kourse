from django.shortcuts import render, get_object_or_404

from .models import Lesson, Student, Attendance
from django.http import HttpResponse, Http404
from .forms import AttendanceForm

# Create your views here.

def index(request):
    # return HttpResponse("Hello World")
    return render(request, 'lessonapp/index.html')


def students(request):
    _students = Student.objects.all()
    return render(request, 'lessonapp/students.html', {'students': _students})


def lessons(request):
    _lessons = Lesson.objects.all()
    return render(request, 'lessonapp/lessons.html', {'lessons': _lessons})


def student(request, student_id):
    _student = get_object_or_404(Student, pk=student_id)
    return render(request, 'lessonapp/student.html', {'student': _student})


def lesson(request, lesson_id):
    # try:
    #     _lesson = Lesson.objects.get(pk=lesson_id)
    # except Lesson.DoesNotExist:
    #     raise Http404
    _lesson = get_object_or_404(Lesson, pk=lesson_id)
    return render(request, 'lessonapp/lesson.html', {'lesson': _lesson})


def attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        _student = request.POST.get('student')

    else:
        form = AttendanceForm()

    return render(request, 'lessonapp/attendance-form.html', {'form': form})