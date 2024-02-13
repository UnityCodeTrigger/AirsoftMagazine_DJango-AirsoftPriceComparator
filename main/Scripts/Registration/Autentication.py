from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

def authCreateUser(request):
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']
    birth_year = request.POST.get('birth_year')  # Utiliza get para manejar casos donde el campo puede estar ausente

    error = 0

    if authExist(email):
        error = 100
        messages.error(request, 'Ya existe una cuenta con este correo electrónico.')
    else:
        try:
            # Intenta convertir el año de nacimiento a un entero
            birth_year = int(birth_year)        
        except (TypeError, ValueError):
            error = 101
            messages.error(request, 'Ingrese un año de nacimiento válido.')

    if error == 0:
        # Crear un nuevo usuario
        user = User.objects.create_user(username=username, email=email, password=password)
        user.birth_year = birth_year  # Agregar el año de nacimiento
        user.save()

        # Iniciar sesión al usuario recién registrado
        login(request, user)
        messages.success(request, 'La creación de la cuenta fue exitosa.')

    return error

def authExist(email):
        if(User.objects.filter(email=email).exists()):
                return True
        else:
                return False

def authLogin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Autenticar al usuario usando email y password
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return 0
        else:
            return 103

    return 100

def authLogout(request):
        logout(request)