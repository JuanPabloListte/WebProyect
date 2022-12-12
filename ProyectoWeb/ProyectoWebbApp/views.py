from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, 'ProyectoWebbApp/home.html')

def service(request):
    return render(request, 'ProyectoWebbApp/service.html')

def store(request):
    return render(request, 'ProyectoWebbApp/store.html')

def blog(request):
    return render(request, 'ProyectoWebbApp/blog.html')

def contact(request):
    return render(request, 'ProyectoWebbApp/contact.html')