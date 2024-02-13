def GetArgument(errorID):
    if( errorID == 100):
        return "ERROR 100, Error de autenticacion, los datos de sesion que se ha introducido no son coherentes o ya existen."
    elif( errorID == 101):
        return "ERROR 101, Error de autenticacion, los datos de sesion que se ha introducido no existe."
    elif( errorID == 102):
        return "ERROR 102, Error de autenticacion, pagina protegida por inicio de sesion."
    elif( errorID == 103):
        return "ERROR 103, Acceso no autorizado."