from django.shortcuts import render

def index_html(request):
    return render(request,'index.html')

def beneficios_html(request):
    return render(request,'beneficios.html')

def blog_html(request):
    return render(request,'blog.html')

def invitaciones_html(request):
    return render(request,'invitaciones.html')

def login_html(request):
    return render(request,'login.html')

def asistente_IA_html(request):
    return render(request,'asistente_IA.html')

def noticias_html(request):
    return render(request,'noticias.html')

def reunion_html(request):
    return render(request,'reunion.html')

def enlaces_utiles_html(request):
    return render(request,'enlaces_utiles.html')

def nuevos_comercios_html(request):
    return render(request,'nuevos_comercios.html')

def redes_sociales_html(request):
    return render(request,'redes_sociales.html')

def streaming_html(request):
    return render(request,'streaming.html')

def directorio_html(request):
    return render(request,'directorio.html')







