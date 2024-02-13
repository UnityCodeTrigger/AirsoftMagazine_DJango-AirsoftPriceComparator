# views.py

from django.shortcuts import render,redirect
from .Scripts import ProductSearch,Cache,ErrorArguments
from django.contrib.auth.decorators import login_required, user_passes_test

templateIndex = "index.html"
templateSearch = "search.html"

# ==================== INDEX ====================
def index(request):
    messages.success(request, 'Mensaje de prueba n1 :)')
    messages.success(request, 'Mensaje de prueba n2 :)')
    messages.success(request, 'Mensaje de prueba n3 :)')
    
    context = {
        "data": {},
        "error": "",
    }
    return render(request, templateIndex, context)

# ==================== SEARCH ====================
def search(request):       
    if (not request.user.is_authenticated):
        messages.success(request, ErrorArguments.GetArgument(102))
        return redirect('login')
        
    errorMessage = ""
    search_query = request.GET.get('query', '')
    context = {}

    if search_query == "":
        errorMessage += "Argumento de búsqueda vacío.\n"
    else:
        #context = Cache.GetCache(search_query)
        context = {}
        products = ProductSearch.GetProducts(search_query)
        
        if context == {}:
            context = {
                "data": {
                    "Weapon762": products[0]["Weapon762"],
                    "Quimera": products[1]["Quimera"],
                },
                "error": errorMessage,
            }
            Cache.SaveOnCache(search_query, context)

    return render(request, 'search.html', context)

 
# ==================== Authentication ====================
from .Scripts.Registration.Autentication import authCreateUser, authLogin, authLogout
from django.contrib import messages

# ==================== Register
def userRegister(request):
    if request.method == 'POST':        
        catch = authCreateUser(request)
        
        if(catch == 0):
            messages.success(request, 'La creación de la cuenta fue exitosa.')

            # Redirigir al usuario a la página de inicio o a donde desees
            return redirect('index')
        else:
            messages.success(request, catch)
            return redirect("register")
    else:
        # Si la solicitud es GET, muestra el formulario de registro
        return render(request, 'register.html')

# ==================== Login
def userLogin(request):
    if request.method == 'POST':        
        authLogin(request)
        
        messages.success(request, 'Sesion iniciada correctamente.')

        # Redirigir al usuario a la página de inicio o a donde desees
        return redirect('index')
    
    # Si la solicitud es GET, muestra el formulario de registro
    return render(request, 'login.html')

# ==================== Logout
def userLogout(request):
    authLogout(request)
    messages.success(request, "Has salido de la sesion correctamente.")
    return redirect("index")

# ==================== DEBUG ====================
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse

def ver_usuarios(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            usuarios = User.objects.all()
            return render(request, 'ver_usuarios.html', {'usuarios': usuarios, 'logUser': request.user})
        else:
            return HttpResponse("No tienes permiso para acceder a esta página.")  # Puedes personalizar este mensaje
    else:
        return redirect("index")  # Redirige al usuario a la página de inicio o la página que prefieras
