from django.shortcuts import render,redirect,get_object_or_404
from .forms import UsuarioForm
from .forms import ComentarioForm,NoticiaForm
from django.contrib import messages
from .models import Comentario,Noticia


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

def registro_html(request):
    return render(request,'registro.html')

#vistas  CRUD
def registro_usuario(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado correctamente.")
            return redirect('index')   
    else:
        form = UsuarioForm()
    return render(request, 'registro.html', {'form': form})


def streaming_html(request):
    comentarios = Comentario.objects.order_by('-fecha')  # lista de comentarios

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('streaming')  # debe coincidir con el nombre del path en urls.py
    else:
        form = ComentarioForm()

    return render(request, 'streaming.html', {
        'form': form,
        'comentarios': comentarios
    })

#Vistas de Noticias 
# Listar todas las noticias
def noticias_html(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias.html', {'noticias': noticias})

# Ver una noticia en detalle
def noticia_detalle(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, 'noticia_detalle.html', {'noticia': noticia})

# Crear nueva noticia
def noticia_crear(request):
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Noticia creada exitosamente.")
            return redirect('noticias')
    else:
        form = NoticiaForm()
    return render(request, 'noticia_form.html', {'form': form, 'accion': 'Crear'})

# Editar una noticia existente
def noticia_editar(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        form = NoticiaForm(request.POST, request.FILES, instance=noticia)
        if form.is_valid():
            form.save()
            messages.success(request, "Noticia actualizada correctamente.")
            return redirect('noticias')
    else:
        form = NoticiaForm(instance=noticia)
    return render(request, 'noticia_form.html', {'form': form, 'accion': 'Editar'})

# Eliminar una noticia
def noticia_eliminar(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    if request.method == 'POST':
        noticia.delete()
        messages.success(request, "Noticia eliminada correctamente.")
        return redirect('noticias')
    return render(request, 'noticia_eliminar.html', {'noticia': noticia})
