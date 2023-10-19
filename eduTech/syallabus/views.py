from django.http import HttpResponse
from django.template import loader
from .models import Books

def syallabus(request):
    booksData = Books.objects.all().values()
    template = loader.get_template("mySample.html")
    context = {
        "myBooks" : booksData
    }
    
    return HttpResponse(template.render(context, request))

def bookDetails(request, id):
    books = Books.objects.get(id = id)
    template = loader.get_template("bookDetails.html")
    context = {
        "book" : books
    }
    return HttpResponse(template.render(context, request))
    
