from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy    

from .forms import *
from .models import *
from WebClubAlmacen.models import DashboardItem
from WebClubAlmacen.forms import DashboardItemForm
from django.http import JsonResponse
from django.core.paginator import Paginator

# ---------------------------
# PÁGINAS PÚBLICAS
# ---------------------------

from .models import ContenidoIndex

def index_html(request):
    items = ContenidoIndex.objects.all()[:20]

    return render(request, "index.html", {
        "items": items
    })





def asistente_IA_html(request):
    return render(request, 'asistente_IA.html')


# ---------------------------
# AUTENTICACIÓN
# ---------------------------

class UsuarioLoginView(LoginView):
    template_name = "login.html"
    authentication_form = LoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
       return self.get_redirect_url() or reverse_lazy('index')
    

def login_view(request):
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")

        user = authenticate(request, username=email, password=password)

        if user:
            login(request, user)

            # Redirección según tipo de usuario
            if user.tipo_usuario == "administrador" :
                return redirect("dashboard_html") 
            else:
                return redirect("index")

        messages.error(request, "Credenciales inválidas")

    return render(request, "login.html")



def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')


# Registro de usuarios
Usuario = get_user_model()

def registro_html(request):
    if request.method == "POST":
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Usuario registrado correctamente.")
            return redirect("login")
        else:
            messages.error(request, "Corrija los errores marcados.")
    else:
        form = RegistroForm()

    return render(request, "registro.html", {"form": form})
# ---------------------------
# HELPERS CRUD COMPARTIDOS
# ---------------------------

def listar(request, modelo, titulo):
    objetos = modelo.objects.all()
    return render(request, 'crud/list.html', {
        'objects': objetos,
        'title': titulo,
    })


def detalle(request, modelo, titulo, pk):
    obj = get_object_or_404(modelo, pk=pk)
    return render(request, 'crud/detail.html', {
        'object': obj,
        'title': titulo,
    })


@login_required
def crear(request, FormClass, titulo, redirect_name):
    if request.method == 'POST':
        form = FormClass(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"{titulo} creado correctamente.")
            return redirect(redirect_name)
    else:
        form = FormClass()
    return render(request, 'crud/form.html', {
        'form': form,
        'title': f"Crear {titulo}",
    })


@login_required
def editar(request, pk, modelo, FormClass, titulo, redirect_name):
    obj = get_object_or_404(modelo, pk=pk)

    if request.method == 'POST':
        form = FormClass(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            messages.success(request, f"{titulo} actualizado correctamente.")
            return redirect(redirect_name)
    else:
        form = FormClass(instance=obj)

    return render(request, 'crud/form.html', {
        'form': form,
        'title': f"Editar {titulo}",
    })


@login_required
def eliminar(request, pk, modelo, titulo, redirect_name):
    obj = get_object_or_404(modelo, pk=pk)

    if request.method == 'POST':
        obj.delete()
        messages.success(request, f"{titulo} eliminado correctamente.")
        return redirect(redirect_name)

    return render(request, 'crud/delete.html', {
        'object': obj,
        'title': f"Eliminar {titulo}",
    })


# ---------------------------
# SECCIÓN: NOTICIAS
# ---------------------------

def noticias_html(request):
    noticias = Noticia.objects.all()

    context = {
        "title": "Noticias",
        "objects": noticias,
        "create_url": "noticia_crear",
        "detail_url": "noticia_detalle",
        "edit_url": "noticia_editar",
        "delete_url": "noticia_eliminar",

        "can_create": request.user.has_perm("webclubalmacen.add_noticia"),
        "can_edit": request.user.has_perm("webclubalmacen.change_noticia"),
        "can_delete": request.user.has_perm("webclubalmacen.delete_noticia"),
    }
    return render(request, "crud/list.html", context)

def noticia_detalle(request, pk):
    noticia = get_object_or_404(Noticia, pk=pk)
    return render(request, "crud/detail.html", {
        'object': noticia,
        'title': noticia.titulo
    })


@permission_required('webclubalmacen.add_noticia', raise_exception=True)
def noticia_crear(request):
    return crear(request, NoticiaForm, "Noticia", 'noticias')


@permission_required('webclubalmacen.change_noticia', raise_exception=True)
def noticia_editar(request, pk):
    return editar(request, pk, Noticia, NoticiaForm, "Noticia", 'noticias')


@permission_required('webclubalmacen.delete_noticia', raise_exception=True)
def noticia_eliminar(request, pk):
    return eliminar(request, pk, Noticia, "Noticia", 'noticias')


# ---------------------------
# BLOG
# ---------------------------

def blog_html(request):
    blogs = BlogPost.objects.all()

    context = {
        "title": "Blog",
        "objects": blogs,
        "create_url": "blog_crear",
        "detail_url": "blog_detalle",
        "edit_url": "blog_editar",
        "delete_url": "blog_eliminar",

        "can_create": request.user.has_perm("webclubalmacen.add_blogpost"),
        "can_edit": request.user.has_perm("webclubalmacen.change_blogpost"),
        "can_delete": request.user.has_perm("webclubalmacen.delete_blogpost"),
    }
    return render(request, "crud/list.html", context)


def blog_detalle(request, pk):
    return detalle(request, BlogPost, "Entrada de Blog", pk)


@permission_required('webclubalmacen.add_blogpost', raise_exception=True)
def blog_crear(request):
    return crear(request, BlogPostForm, "Entrada de Blog", 'blog')


@permission_required('webclubalmacen.change_blogpost', raise_exception=True)
def blog_editar(request, pk):
    return editar(request, pk, BlogPost, BlogPostForm, "Entrada de Blog", 'blog')


@permission_required('webclubalmacen.delete_blogpost', raise_exception=True)
def blog_eliminar(request, pk):
    return eliminar(request, pk, BlogPost, "Entrada de Blog", 'blog')

# ---------------------------
# STREAMING
# ---------------------------

def streaming_html(request):
    streamings = Streaming.objects.all()

    context = {
        "title": "Streaming",
        "objects": streamings,
        "create_url": "streaming_crear",
        "detail_url": "streaming_detalle",
        "edit_url": "streaming_editar",
        "delete_url": "streaming_eliminar",

        "can_create": request.user.has_perm("webclubalmacen.add_streaming"),
        "can_edit": request.user.has_perm("webclubalmacen.change_streaming"),
        "can_delete": request.user.has_perm("webclubalmacen.delete_streaming"),
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
# ---------------------------
# BENEFICIOS
# ---------------------------
def beneficios_html(request):
    beneficios = Beneficio.objects.all()

    context = {
        "title": "Beneficios",
        "objects": beneficios,
        "create_url": "beneficio_crear",
        "detail_url": "beneficio_detalle",
        "edit_url": "beneficio_editar",
        "delete_url": "beneficio_eliminar",

        "can_create": request.user.has_perm("webclubalmacen.add_beneficio"),
        "can_edit": request.user.has_perm("webclubalmacen.change_beneficio"),
        "can_delete": request.user.has_perm("webclubalmacen.delete_beneficio"),
    }
    return render(request, "crud/list.html", context)


def beneficio_detalle(request, pk):
    return detalle(request, Beneficio, "Beneficio", pk)


@permission_required('webclubalmacen.add_beneficio', raise_exception=True)
def beneficio_crear(request):
    return crear(request, BeneficioForm, "Beneficio", 'beneficios')


@permission_required('webclubalmacen.change_beneficio', raise_exception=True)
def beneficio_editar(request, pk):
    return editar(request, pk, Beneficio, BeneficioForm, "Beneficio", 'beneficios')


@permission_required('webclubalmacen.delete_beneficio', raise_exception=True)
def beneficio_eliminar(request, pk):
    return eliminar(request, pk, Beneficio, "Beneficio", 'beneficios')

# ---------------------------
# ---------------------------
# DASHBOARD
# ---------------------------
def dashboard_html(request):
    items = DashboardItem.objects.all()

    context = {
        "title": "Dashboard",
        "objects": items,
        "create_url": "dashboard_crear",
        "detail_url": "dashboard_detalle",
        "edit_url": "dashboard_editar",
        "delete_url": "dashboard_eliminar",

        "can_create": request.user.has_perm("webclubalmacen.add_dashboarditem"),
        "can_edit": request.user.has_perm("webclubalmacen.change_dashboarditem"),
        "can_delete": request.user.has_perm("webclubalmacen.delete_dashboarditem"),
    }
    return render(request, "crud/list.html", context)


def dashboard_detalle(request, pk):
    return detalle(request, DashboardItem, "Dashboard", pk)


@permission_required('webclubalmacen.add_dashboarditem', raise_exception=True)
def dashboard_crear(request):
    return crear(request, DashboardItemForm, "Dashboard", 'dashboard')


@permission_required('webclubalmacen.change_dashboarditem', raise_exception=True)
def dashboard_editar(request, pk):
    return editar(request, pk, DashboardItem, DashboardItemForm, "Dashboard", 'dashboard')


@permission_required('webclubalmacen.delete_dashboarditem', raise_exception=True)
def dashboard_eliminar(request, pk):
    return eliminar(request, pk, DashboardItem, "Dashboard", 'dashboard')

# ---------------------------
# DIRECTORIO
# ---------------------------
def directorio_html(request):
    items = Directorio.objects.all()

    context = {
        "title": "Directorio",
        "objects": items,
        "create_url": "directorio_crear",
        "detail_url": "directorio_detalle",
        "edit_url": "directorio_editar",
        "delete_url": "directorio_eliminar",

        "can_create": request.user.has_perm("webclubalmacen.add_directorio"),
        "can_edit": request.user.has_perm("webclubalmacen.change_directorio"),
        "can_delete": request.user.has_perm("webclubalmacen.delete_directorio"),
    }
    return render(request, "crud/list.html", context)


def directorio_detalle(request, pk):
    return detalle(request, Directorio, "Directorio", pk)


@permission_required('webclubalmacen.add_directorio', raise_exception=True)
def directorio_crear(request):
    return crear(request, DirectorioForm, "Directorio", 'directorio')


@permission_required('webclubalmacen.change_directorio', raise_exception=True)
def directorio_editar(request, pk):
    return editar(request, pk, Directorio, DirectorioForm, "Directorio", 'directorio')


@permission_required('webclubalmacen.delete_directorio', raise_exception=True)
def directorio_eliminar(request, pk):
    return eliminar(request, pk, Directorio, "Directorio", 'directorio')
# ---------------------------
# ---------------------------
# ENLACES ÚTILES
# ---------------------------
def enlaces_utiles_html(request):
    enlaces = EnlaceUtil.objects.all()

    context = {
        "title": "Enlaces Útiles",
        "objects": enlaces,
        "create_url": "enlace_crear",
        "detail_url": "enlace_detalle",
        "edit_url": "enlace_editar",
        "delete_url": "enlace_eliminar",

        "can_create": request.user.has_perm("webclubalmacen.add_enlaceutil"),
        "can_edit": request.user.has_perm("webclubalmacen.change_enlaceutil"),
        "can_delete": request.user.has_perm("webclubalmacen.delete_enlaceutil"),
    }
    return render(request, "crud/list.html", context)


def enlace_detalle(request, pk):
    return detalle(request, EnlaceUtil, "Enlace Útil", pk)


@permission_required('webclubalmacen.add_enlaceutil', raise_exception=True)
def enlace_crear(request):
    return crear(request, EnlaceUtilForm, "Enlace Útil", 'enlaces')


@permission_required('webclubalmacen.change_enlaceutil', raise_exception=True)
def enlace_editar(request, pk):
    return editar(request, pk, EnlaceUtil, EnlaceUtilForm, "Enlace Útil", 'enlaces')


@permission_required('webclubalmacen.delete_enlaceutil', raise_exception=True)
def enlace_eliminar(request, pk):
    return eliminar(request, pk, EnlaceUtil, "Enlace Útil", 'enlaces')
# ---------------------------
def nuevos_comercios_html(request):
    comercios = NuevoComercio.objects.all()

    context = {
        "title": "Nuevos Comercios",
        "objects": comercios,
        "create_url": "nuevo_comercio_crear",
        "detail_url": "nuevo_comercio_detalle",
        "edit_url": "nuevo_comercio_editar",
        "delete_url": "nuevo_comercio_eliminar",

        "can_create": request.user.has_perm("webclubalmacen.add_nuevocomercio"),
        "can_edit": request.user.has_perm("webclubalmacen.change_nuevocomercio"),
        "can_delete": request.user.has_perm("webclubalmacen.delete_nuevocomercio"),
    }
    return render(request, "crud/list.html", context)


def nuevo_comercio_detalle(request, pk):
    return detalle(request, NuevoComercio, "Nuevo Comercio", pk)


@permission_required('webclubalmacen.add_nuevocomercio', raise_exception=True)
def nuevo_comercio_crear(request):
    return crear(request, NuevoComercioForm, "Nuevo Comercio", 'nuevos_comercios')


@permission_required('webclubalmacen.change_nuevocomercio', raise_exception=True)
def nuevo_comercio_editar(request, pk):
    return editar(request, pk, NuevoComercio, NuevoComercioForm, "Nuevo Comercio", 'nuevos_comercios')


@permission_required('webclubalmacen.delete_nuevocomercio', raise_exception=True)
def nuevo_comercio_eliminar(request, pk):
    return eliminar(request, pk, NuevoComercio, "Nuevo Comercio", 'nuevos_comercios')
# ---------------------------
# REDES SOCIALES
# ---------------------------
def redes_sociales_html(request):
    redes = RedSocial.objects.all()

    context = {
        "title": "Redes Sociales",
        "objects": redes,
        "create_url": "red_social_crear",
        "detail_url": "red_social_detalle",
        "edit_url": "red_social_editar",
        "delete_url": "red_social_eliminar",

        "can_create": request.user.has_perm("webclubalmacen.add_redsocial"),
        "can_edit": request.user.has_perm("webclubalmacen.change_redsocial"),
        "can_delete": request.user.has_perm("webclubalmacen.delete_redsocial"),
    }
    return render(request, "crud/list.html", context)


def red_social_detalle(request, pk):
    return detalle(request, RedSocial, "Red Social", pk)


@permission_required('webclubalmacen.add_redsocial', raise_exception=True)
def red_social_crear(request):
    return crear(request, RedSocialForm, "Red Social", 'redes')


@permission_required('webclubalmacen.change_redsocial', raise_exception=True)
def red_social_editar(request, pk):
    return editar(request, pk, RedSocial, RedSocialForm, "Red Social", 'redes')


@permission_required('webclubalmacen.delete_redsocial', raise_exception=True)
def red_social_eliminar(request, pk):
    return eliminar(request, pk, RedSocial, "Red Social", 'redes')
# ---------------------------
# REUNIONES
# ---------------------------
def reuniones_html(request):
    reuniones = Reunion.objects.all()

    context = {
        "title": "Reuniones",
        "objects": reuniones,
        "create_url": "reunion_crear",
        "detail_url": "reunion_detalle",
        "edit_url": "reunion_editar",
        "delete_url": "reunion_eliminar",

        "can_create": request.user.has_perm("webclubalmacen.add_reunion"),
        "can_edit": request.user.has_perm("webclubalmacen.change_reunion"),
        "can_delete": request.user.has_perm("webclubalmacen.delete_reunion"),
    }
    return render(request, "crud/list.html", context)


def reunion_detalle(request, pk):
    return detalle(request, Reunion, "Reunión", pk)


@permission_required('webclubalmacen.add_reunion', raise_exception=True)
def reunion_crear(request):
    return crear(request, ReunionForm, "Reunión", 'reuniones')


@permission_required('webclubalmacen.change_reunion', raise_exception=True)
def reunion_editar(request, pk):
    return editar(request, pk, Reunion, ReunionForm, "Reunión", 'reuniones')


@permission_required('webclubalmacen.delete_reunion', raise_exception=True)
def reunion_eliminar(request, pk):
    return eliminar(request, pk, Reunion, "Reunión", 'reuniones')
# ---------------------------
def asistente_ia_html(request):
    sesiones = AsistenteIA.objects.all()

    context = {
        "title": "Asistente IA",
        "objects": sesiones,
        "create_url": "asistente_ia_crear",
        "detail_url": "asistente_ia_detalle",
        "edit_url": "asistente_ia_editar",
        "delete_url": "asistente_ia_eliminar",

        "can_create": request.user.has_perm("webclubalmacen.add_asistenteia"),
        "can_edit": request.user.has_perm("webclubalmacen.change_asistenteia"),
        "can_delete": request.user.has_perm("webclubalmacen.delete_asistenteia"),
    }
    return render(request, "crud/list.html", context)


def asistente_ia_detalle(request, pk):
    return detalle(request, AsistenteIA, "Asistente IA", pk)


@permission_required('webclubalmacen.add_asistenteia', raise_exception=True)
def asistente_ia_crear(request):
    return crear(request, AsistenteIAForm, "Asistente IA", 'asistente_ia')


@permission_required('webclubalmacen.change_asistenteia', raise_exception=True)
def asistente_ia_editar(request, pk):
    return editar(request, pk, AsistenteIA, AsistenteIAForm, "Asistente IA", 'asistente_ia')


@permission_required('webclubalmacen.delete_asistenteia', raise_exception=True)
def asistente_ia_eliminar(request, pk):
    return eliminar(request, pk, AsistenteIA, "Asistente IA", 'asistente_ia')
# ---------------------------
def invitaciones_html(request):
    invitaciones = Invitacion.objects.all()

    context = {
        "title": "Invitaciones",
        "objects": invitaciones,
        "create_url": "invitacion_crear",
        "detail_url": "invitacion_detalle",
        "edit_url": "invitacion_editar",
        "delete_url": "invitacion_eliminar",

        "can_create": request.user.has_perm("webclubalmacen.add_invitacion"),
        "can_edit": request.user.has_perm("webclubalmacen.change_invitacion"),
        "can_delete": request.user.has_perm("webclubalmacen.delete_invitacion"),
    }
    return render(request, "crud/list.html", context)


def invitacion_detalle(request, pk):
    return detalle(request, Invitacion, "Invitación", pk)


@permission_required('webclubalmacen.add_invitacion', raise_exception=True)
def invitacion_crear(request):
    return crear(request, InvitacionForm, "Invitación", 'invitaciones')


@permission_required('webclubalmacen.change_invitacion', raise_exception=True)
def invitacion_editar(request, pk):
    return editar(request, pk, Invitacion, InvitacionForm, "Invitación", 'invitaciones')


@permission_required('webclubalmacen.delete_invitacion', raise_exception=True)
def invitacion_eliminar(request, pk):
    return eliminar(request, pk, Invitacion, "Invitación", 'invitaciones')





#-----------------------API JSON SCROLL Infinito------------------------

def api_index_items(request):
    page = int(request.GET.get("page", 1))
    paginator = Paginator(ContenidoIndex.objects.all(), 20)

    items_page = paginator.get_page(page)

    data = [{
        "titulo": item.titulo,
        "descripcion": item.descripcion,
        "categoria": item.categoria,
        "imagen": item.imagen.url if item.imagen else None,
        "link": item.link,
    } for item in items_page]

    return JsonResponse({
        "items": data,
        "has_next": items_page.has_next(),
    })