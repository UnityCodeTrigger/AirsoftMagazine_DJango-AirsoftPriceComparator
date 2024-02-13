import pickle
from datetime import datetime, timedelta
from ..WebConfig import CACHE_SETTINGS

cache_file = "main/cache/" + CACHE_SETTINGS.get("FILE_NAME")  # Nombre del archivo de caché
global search_cache

# Carga la caché desde el archivo si existe
try:
    with open(cache_file, 'rb') as file:
        search_cache = pickle.load(file)
except FileNotFoundError:
    search_cache = {
        "context": {},
        "query": {},
    }

def GetCache(search_query):
    context = {}
    
    # Verifica si existe una entrada en caché para esta consulta y si ha caducado
    if search_query in search_cache["context"]:
        cached_data = search_cache["context"][search_query]
        cached_time = search_cache["query"][search_query]
        current_time = datetime.now()
        
        deathTimeDays = CACHE_SETTINGS.get("ITEM_DEATH_TIME_DAYS")
        deathTimeHours = CACHE_SETTINGS.get("ITEM_DEATH_TIME_HOURS")
        if current_time - cached_time <= timedelta(days=deathTimeDays,hours=deathTimeHours):
            context = cached_data  # Utiliza los datos en caché
        else:
            # Guarda la caché en el archivo
            with open(cache_file, 'wb') as file:
                pickle.dump(search_cache, file)
                
    return context

def SaveOnCache(search_query, context):  # Cambié el orden de los argumentos
    # Almacena la entrada en caché para esta consulta
    search_cache["context"][search_query] = context
    search_cache["query"][search_query] = datetime.now()

    # Guarda la caché en el archivo
    with open(cache_file, 'wb') as file:
        pickle.dump(search_cache, file)