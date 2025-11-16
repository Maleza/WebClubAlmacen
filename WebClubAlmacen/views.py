from django.shortcuts import render,redirect,get_object_or_404
from .forms import *
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required,permission_required



def index_html(request):
    return render(request,'index.html')

def asistente_IA_html(request):
    return render(request,'asistente_IA.html')


#vistas de autenticacion
def login_html(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        messages.error(request, "Usuario o contraseña incorrectos")

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')







# --- Helper genérico para lista pública ---
def listar(request, modelo, titulo):
    objetos = modelo.objects.all()
    context = {
        'objects': objetos,
        'title': titulo,
    }
    return render(request, 'crud/list.html', context)

# --- Helper genérico para detalle público ---
def detalle(request, modelo, titulo, pk):
    obj = get_object_or_404(modelo, pk=pk)
    return render(request, 'crud/detail.html', {'object': obj, 'title': titulo})

# --- Helper genérico CRUD protegido ---
@login_required
def crear(request, FormClass, titulo, redirect_name):
    if request.method == 'POST':
        form = FormClass(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"{titulo} creada correctamente.")
            return redirect(redirect_name)
    else:
        form = FormClass()
    return render(request, 'crud/form.html', {'form': form, 'title': f"Crear {titulo}"})

@login_required
def editar(request, pk, modelo, FormClass, titulo, redirect_name):
    obj = get_object_or_404(modelo, pk=pk)
    if request.method == 'POST':
        form = FormClass(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, f"{titulo} actualizada correctamente.")
            return redirect(redirect_name)
    else:
        form = FormClass(instance=obj)
    return render(request, 'crud/form.html', {'form': form, 'title': f"Editar {titulo}"})

@login_required
def eliminar(request, pk, modelo, titulo, redirect_name):
    obj = get_object_or_404(modelo, pk=pk)
    if request.method == 'POST':
        obj.delete()
        messages.success(request, f"{titulo} eliminada correctamente.")
        return redirect(redirect_name)
    return render(request, 'crud/delete.html', {'object': obj, 'title': f"Eliminar {titulo}"})

# --- RUTAS CONCRETA (wrappers) ---
# Noticias
def noticias_html(request):
    noticias = Noticia.objects.all()
    
    context = {
        "title": "Noticias",
        "objects": noticias,
        "create_url": "noticia_crear",
        "detail_url": "noticia_detalle",
        "edit_url": "noticia_editar",
        "delete_url": "noticia_eliminar",

        # Permisos ya evaluados
        "can_create": request.user.has_perm("WebClubAlmacen.add_noticia"),
        "can_edit": request.user.has_perm("WebClubAlmacen.change_noticia"),
        "can_delete": request.user.has_perm("WebClubAlmacen.delete_noticia"),
    }

    return render(request, "crud/list.html", context)



def noticia_detalle(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    context = {
        'object': noticia,
        'title': noticia.titulo,
        'edit_url': 'noticia_editar',
        'detail_url': 'noticia_detalle',
        'edit_perm': 'webclubalmacen.change_noticia',
    }
    return render(request, 'crud/detail.html', context)



@permission_required('webclubalmacen.add_noticia', raise_exception=True)
def noticia_crear(request):
    return crear(request, NoticiaForm, "Noticia", 'noticias')

@permission_required('webclubalmacen.change_noticia', raise_exception=True)
def noticia_editar(request, pk):
    return editar(request, pk, Noticia, NoticiaForm, "Noticia", 'noticias')

@permission_required('webclubalmacen.delete_noticia', raise_exception=True)
def noticia_eliminar(request, pk):
    return eliminar(request, pk, Noticia, "Noticia", 'noticias')

# Blog
#def blog_html(request):
    #return listar(request, BlogPost, "Blog")

def blog_detalle(request, pk):
    return detalle(request, BlogPost, "Entrada de Blog", pk)

def blog_html(request):
    blogs = BlogPost.objects.all()

    context = {
        "title": "Blog",
        "objects": blogs,
        "create_url": "blog_crear",
        "detail_url": "blog_detalle",
        "edit_url": "blog_editar",
        "delete_url": "blog_eliminar",

        "can_create": request.user.has_perm("WebClubAlmacen.add_blog"),
        "can_edit": request.user.has_perm("WebClubAlmacen.change_blog"),
        "can_delete": request.user.has_perm("WebClubAlmacen.delete_blog"),
    }
    return render(request, "crud/list.html", context)



@permission_required('webclubalmacen.add_blogpost', raise_exception=True)
def blog_crear(request):
    return crear(request, BlogPostForm, "Entrada de Blog", 'blog')

@permission_required('webclubalmacen.change_blogpost', raise_exception=True)
def blog_editar(request, pk):
    return editar(request, pk, BlogPost, BlogPostForm, "Entrada de Blog", 'blog')

@permission_required('webclubalmacen.delete_blogpost', raise_exception=True)
def blog_eliminar(request, pk):
    return eliminar(request, pk, BlogPost, "Entrada de Blog", 'blog')

# Streaming
def streaming_html(request):
    streams = Streaming.objects.all()

    context = {
        "title": "Transmisiones",
        "objects": streams,
        "create_url": "streaming_crear",
        "detail_url": "streaming_detalle",
        "edit_url": "streaming_editar",
        "delete_url": "streaming_eliminar",

        "can_create": request.user.has_perm("WebClubAlmacen.add_streaming"),
        "can_edit": request.user.has_perm("WebClubAlmacen.change_streaming"),
        "can_delete": request.user.has_perm("WebClubAlmacen.delete_streaming"),
    }
    return render(request, "crud/list.html", context)

def streaming_detalle(request, pk):
    return detalle(request, Streaming, "Streaming", pk)

@permission_required('webclubalmacen.add_streaming', raise_exception=True)
def streaming_crear(request):
    return crear(request, StreamingForm, "Streaming", 'streaming')

@permission_required('webclubalmacen.change_streaming', raise_exception=True)
def streaming_editar(request, pk):
    return editar(request, pk, Streaming, StreamingForm, "Streaming", 'streaming')

@permission_required('webclubalmacen.delete_streaming', raise_exception=True)
def streaming_eliminar(request, pk):
    return eliminar(request, pk, Streaming, "Streaming", 'streaming')

# Beneficios
def beneficios_html(request):
    beneficios = Beneficio.objects.all()

    context = {
        "title": "Beneficios",
        "objects": beneficios,
        "create_url": "beneficio_crear",
        "detail_url": "beneficio_detalle",
        "edit_url": "beneficio_editar",
        "delete_url": "beneficio_eliminar",

        "can_create": request.user.has_perm("WebClubAlmacen.add_beneficio"),
        "can_edit": request.user.has_perm("WebClubAlmacen.change_beneficio"),
        "can_delete": request.user.has_perm("WebClubAlmacen.delete_beneficio"),
    }
    return render(request, "crud/list.html", context)

@permission_required('webclubalmacen.add_beneficio', raise_exception=True)
def beneficio_crear(request):
    return crear(request, BeneficioForm, "Beneficio", 'beneficios')

@permission_required('webclubalmacen.change_beneficio', raise_exception=True)
def beneficio_editar(request, pk):
    return editar(request, pk, Beneficio, BeneficioForm, "Beneficio", 'beneficios')

@permission_required('webclubalmacen.delete_beneficio', raise_exception=True)
def beneficio_eliminar(request, pk):
    return eliminar(request, pk, Beneficio, "Beneficio", 'beneficios')

# Enlaces útiles
def enlaces_utiles_html(request):
    enlaces = EnlaceUtil.objects.all()

    context = {
        "title": "Enlaces Útiles",
        "objects": enlaces,
        "create_url": "enlace_crear",
        "detail_url": "enlace_detalle",
        "edit_url": "enlace_editar",
        "delete_url": "enlace_eliminar",

        "can_create": request.user.has_perm("WebClubAlmacen.add_enlaceutil"),
        "can_edit": request.user.has_perm("WebClubAlmacen.change_enlaceutil"),
        "can_delete": request.user.has_perm("WebClubAlmacen.delete_enlaceutil"),
    }
    return render(request, "crud/list.html", context)

@permission_required('webclubalmacen.add_enlaceutil', raise_exception=True)
def enlace_crear(request):
    return crear(request, EnlaceUtilForm, "Enlace", 'enlaces_utiles')

@permission_required('webclubalmacen.change_enlaceutil', raise_exception=True)
def enlace_editar(request, pk):
    return editar(request, pk, EnlaceUtil, EnlaceUtilForm, "Enlace", 'enlaces_utiles')

@permission_required('webclubalmacen.delete_enlaceutil', raise_exception=True)
def enlace_eliminar(request, pk):
    return eliminar(request, pk, EnlaceUtil, "Enlace", 'enlaces_utiles')

# Invitaciones
def invitaciones_html(request):
    invitaciones = Invitacion.objects.all()

    context = {
        "title": "Invitaciones",
        "objects": invitaciones,
        "create_url": "invitacion_crear",
        "detail_url": "invitacion_detalle",
        "edit_url": "invitacion_editar",
        "delete_url": "invitacion_eliminar",

        "can_create": request.user.has_perm("WebClubAlmacen.add_invitacion"),
        "can_edit": request.user.has_perm("WebClubAlmacen.change_invitacion"),
        "can_delete": request.user.has_perm("WebClubAlmacen.delete_invitacion"),
    }
    return render(request, "crud/list.html", context)


@permission_required('webclubalmacen.add_invitacion', raise_exception=True)
def invitacion_crear(request):
    return crear(request, InvitacionForm, "Invitación", 'invitaciones')

@permission_required('webclubalmacen.change_invitacion', raise_exception=True)
def invitacion_editar(request, pk):
    return editar(request, pk, Invitacion, InvitacionForm, "Invitación", 'invitaciones')

@permission_required('webclubalmacen.delete_invitacion', raise_exception=True)
def invitacion_eliminar(request, pk):
    return eliminar(request, pk, Invitacion, "Invitación", 'invitaciones')

# Nuevos comercios
def nuevos_comercios_html(request):
    comercios = NuevoComercio.objects.all()

    context = {
        "title": "Nuevos Comercios",
        "objects": comercios,
        "create_url": "comercio_crear",
        "detail_url": "comercio_detalle",
        "edit_url": "comercio_editar",
        "delete_url": "comercio_eliminar",

        "can_create": request.user.has_perm("WebClubAlmacen.add_nuevocomercio"),
        "can_edit": request.user.has_perm("WebClubAlmacen.change_nuevocomercio"),
        "can_delete": request.user.has_perm("WebClubAlmacen.delete_nuevocomercio"),
    }
    return render(request, "crud/list.html", context)


@permission_required('webclubalmacen.add_nuevocomercio', raise_exception=True)
def comercio_crear(request):
    return crear(request, NuevoComercioForm, "Comercio", 'nuevos_comercios')

@permission_required('webclubalmacen.change_nuevocomercio', raise_exception=True)
def comercio_editar(request, pk):
    return editar(request, pk, NuevoComercio, NuevoComercioForm, "Comercio", 'nuevos_comercios')

@permission_required('webclubalmacen.delete_nuevocomercio', raise_exception=True)
def comercio_eliminar(request, pk):
    return eliminar(request, pk, NuevoComercio, "Comercio", 'nuevos_comercios')

# Redes sociales
def redes_sociales_html(request):
    redes = RedSocial.objects.all()

    context = {
        "title": "Redes Sociales",
        "objects": redes,
        "create_url": "red_crear",
        "detail_url": "red_detalle",
        "edit_url": "red_editar",
        "delete_url": "red_eliminar",

        "can_create": request.user.has_perm("WebClubAlmacen.add_redsocial"),
        "can_edit": request.user.has_perm("WebClubAlmacen.change_redsocial"),
        "can_delete": request.user.has_perm("WebClubAlmacen.delete_redsocial"),
    }
    return render(request, "crud/list.html", context)


@permission_required('webclubalmacen.add_redsocial', raise_exception=True)
def redsocial_crear(request):
    return crear(request, RedSocialForm, "Red social", 'redes_sociales')

@permission_required('webclubalmacen.change_redsocial', raise_exception=True)
def redsocial_editar(request, pk):
    return editar(request, pk, RedSocial, RedSocialForm, "Red social", 'redes_sociales')

@permission_required('webclubalmacen.delete_redsocial', raise_exception=True)
def redsocial_eliminar(request, pk):
    return eliminar(request, pk, RedSocial, "Red social", 'redes_sociales')

# Reuniones
def reunion_html(request):
    reuniones = Reunion.objects.all()

    context = {
        "title": "Reuniones",
        "objects": reuniones,
        "create_url": "reunion_crear",
        "detail_url": "reunion_detalle",
        "edit_url": "reunion_editar",
        "delete_url": "reunion_eliminar",

        "can_create": request.user.has_perm("WebClubAlmacen.add_reunion"),
        "can_edit": request.user.has_perm("WebClubAlmacen.change_reunion"),
        "can_delete": request.user.has_perm("WebClubAlmacen.delete_reunion"),
    }
    return render(request, "crud/list.html", context)

@permission_required('webclubalmacen.add_reunion', raise_exception=True)
def reunion_crear(request):
    return crear(request, ReunionForm, "Reunión", 'reuniones')

@permission_required('webclubalmacen.change_reunion', raise_exception=True)
def reunion_editar(request, pk):
    return editar(request, pk, Reunion, ReunionForm, "Reunión", 'reuniones')

@permission_required('webclubalmacen.delete_reunion', raise_exception=True)
def reunion_eliminar(request, pk):
    return eliminar(request, pk, Reunion, "Reunión", 'reuniones')

# Directorio
def directorio_html(request):
    directorio = Directorio.objects.all()

    context = {
        "title": "Directorio",
        "objects": directorio,
        "create_url": "directorio_crear",
        "detail_url": "directorio_detalle",
        "edit_url": "directorio_editar",
        "delete_url": "directorio_eliminar",

        "can_create": request.user.has_perm("WebClubAlmacen.add_directorio"),
        "can_edit": request.user.has_perm("WebClubAlmacen.change_directorio"),
        "can_delete": request.user.has_perm("WebClubAlmacen.delete_directorio"),
    }
    return render(request, "crud/list.html", context)

@permission_required('webclubalmacen.add_directorio', raise_exception=True)
def directorio_crear(request):
    return crear(request, DirectorioForm, "Registro de directorio", 'directorio')

@permission_required('webclubalmacen.change_directorio', raise_exception=True)
def directorio_editar(request, pk):
    return editar(request, pk, Directorio, DirectorioForm, "Registro de directorio", 'directorio')

@permission_required('webclubalmacen.delete_directorio', raise_exception=True)
def directorio_eliminar(request, pk):
    return eliminar(request, pk, Directorio, "Registro de directorio", 'directorio')