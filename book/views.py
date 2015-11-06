from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import Context
from book.models import Book
from book.models import Author
# Create your views here.

# GUI HTML
def index(request):
    return render_to_response("index.html")
def add_author(request):
    return render_to_response("insert_author.html")
def search_author(request):
    return render_to_response("search_by_author.html")
def add_book(request):
    return render_to_response("insert_book.html")
def view_book(request):
    book_list = Book.objects.all()
    return render_to_response("view_book.html",{'book_list':book_list})
# insert into DB
def insert_author(request):
    if request.POST:
        post = request.POST
        try:
            author_remain = Author.objects.filter(AuthorID = post["author_id"])[0]
            message="this author id exists "            
            return render_to_response("mistake.html",{'message': message})
        except IndexError:
            new_author = Author( AuthorID= post["author_id"],Name = post["author_name"] ,Age=post["age"], Country=post["country"])    
            new_author.save()
            return render_to_response("success.html")
    return render_to_response("insert_author.html")
       
def insert_book(request):
    if request.POST:
        post = request.POST
        try:
            book_remain = Book.objects.filter(ISBN = post["ISBN"])[0]
            message="this book already exists ,can not be inserted again\nbut you can update it"
            return render_to_response("mistake.html",{'message': message})
        except IndexError:   
            #if the author not exits,need to add
            try:
                author = Author.objects.filter(AuthorID = post["author_id"])[0]
                new_book = Book( ISBN= post["ISBN"],Title = post["title"] ,Publisher=post["publisher"], AuthorID=post["author_id"],Price=(float)(post["price"]),PublishDate=post["publishDate"])    
                new_book.save()
                return render_to_response("success.html")#
            except IndexError: 
                 message="we cannot find this author id ,please insert the author firstly"            
                 return render_to_response("mistake.html",{'message': message})
        
    return render_to_response("insert_book.html")
#search
def search_by_author(request):
    if 'author_name' in request.GET and request.GET['author_name']:
        author_name = request.GET['author_name']
        try:
            author = Author.objects.filter(Name =author_name)[0]
            author_id=author.AuthorID
            #find all books by this id
            books = Book.objects.filter(AuthorID = author_id)
            return render_to_response('view_by_author.html',
                {'book_list': books})
        
        except IndexError:
            message="can not find this author"
            return render_to_response("mistake.html",{'message': message})
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)
    
def search_book(request):
    if 'ISBN' in request.GET and request.GET['ISBN']:
        ISBN_num = request.GET['ISBN']
        book = Book.objects.filter(ISBN =ISBN_num)[0]
        author_id=book.AuthorID
        #find all books by this id
        books = Book.objects.filter(AuthorID = author_id)
        author = Author.objects.filter(AuthorID = author_id)
        return render_to_response('view_by_book.html',
            {'book_list': books,'author':author})
        
    else:
        message = 'bad operation'
    return HttpResponse(message)
    
#delete function
def delete_book(request):
     if 'ISBN' in request.GET and request.GET['ISBN']:
         delete_id = request.GET["ISBN"]
         Book.objects.get(ISBN = delete_id).delete()   
         return render_to_response("success.html")#
         
     message = 'operation mistake:no delete'
     return HttpResponse(message)
     
#update function
def update_book(request):
    #process the update request and return a html with information
    if 'ISBN' in request.GET and request.GET['ISBN']:
         update_id = request.GET["ISBN"]
         book = Book.objects.filter( ISBN = update_id )[0]
         return render_to_response("update_book.html", {"book":book})
         
    message = 'operation mistake:no update'
    return HttpResponse(message)
def update(request):
    if request.POST:
        post = request.POST
        book = Book.objects.get(ISBN = post["ISBN"])
        #update
        book.AuthorID = post["AuthorID"]
        book.Publisher = post["Publisher"]
        book.PublishDate = post["PublishDate"]
        book.Price = post["Price"]
        #save
        book.save()  
        return render_to_response("success.html")
    message = 'operation mistake:no update'
    return HttpResponse(message)
    