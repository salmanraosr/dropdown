from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from cccapp.models import Grade, Subject, Book, Chapter
def dependantfield(request):
    gradeid = request.GET.get('grade', None)
    subjectid = request.GET.get('subject', None)
    subject = None
    book = None
    if gradeid:
        getgrade = Grade.objects.get(id=gradeid)
        subject = Subject.objects.filter(grade=getgrade)
    if subjectid:
        getsubject = Subject.objects.get(id=subjectid)
        book = Book.objects.filter(subject=getsubject)
    grade = Grade.objects.all()
    return render(request, 'dependantfield.html', locals())

def home(request):
    if request.method == "POST":
        book = request.POST.get('book')
        chapter = Chapter.objects.filter(book=book)
    return render(request, "home.html",{'chapter':chapter})

def index(request):
    return render(request, 'index.html')

def result(request):
    result = request.GET['result']
    return render(request, 'result.html', {'result':result})