import requests
from .Scrap import Quimera, Weapon762, Sherman

def GetProducts(search):
    
    # Crear una sesión persistente para todas las solicitudes HTTP
    session = requests.Session()

    req = []
    req.append( Weapon762.GetProducts( searchValue=search, session=session ) )
    req.append( Quimera.GetProducts( searchValue=search, session=session ) )
    #Sherman.GetProducts( searchValue=search, session=session )

    return req