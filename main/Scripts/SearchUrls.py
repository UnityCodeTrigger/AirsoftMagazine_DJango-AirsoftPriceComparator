"""

# OBSOLETO

import requests
from bs4 import BeautifulSoup
from ..WebConfig import SEARCH_SETTINGS

# Crear una sesión persistente para todas las solicitudes HTTP
session = requests.Session()
max_results = SEARCH_SETTINGS.get("MAX_RESULTS_PER_ENGINE")
def Weapon762(searchValue):
    url = f"https://www.weapon762.com/search?controller=search&orderby=position&orderway=desc&search_query={searchValue}&tm_submit_search="
    
    # Utilizar la sesión persistente para la solicitud HTTP
    response = session.get(url)
    html = response.text
    
    htmlSoup = BeautifulSoup(html, "html.parser")
    productContainer_ul = htmlSoup.find(class_="product_list grid row")
    
    if not productContainer_ul:
        return { "Weapon762": [] }

    productContainer_li = productContainer_ul.find_all("li")  # Remove slicing to find all results
    productContainer_li = productContainer_li[:max_results]
    productNames = []
    productPrices = []
    productImages = []
    productLinks = []
    
    for li in productContainer_li:
        grid_names = li.find_all(class_="list-name")
        productNames.extend([element.text for element in grid_names])
        
        grid_prices = li.find_all(class_="price product-price")
        productPrices.extend([element.text[:-1] for element in grid_prices])

        grid_images = li.find_all("img", class_="replace-2x img-responsive lazy")
        productImages.extend([element.get("data-original") for element in grid_images])
        
        grid_links = li.find_all(class_="product_img_link")
        productLinks.extend([element.get("href") for element in grid_links])
    
    productData = list(zip(productNames, productPrices, productImages, productLinks))
    productDict = {
        "Weapon762": productData
    }
    
    return productDict


def Quimera(searchValue):
    url = f"https://www.airsoftquimera.com/lp/?idsite=4&idioma=50&criterio=buscador&criterio_id={searchValue}&filtros=&url_action_0=%2Fbuscador%2F&url_action_1=%2Flp%2F&url_action_2=%2Frcms%2F&url_action_3=%2Frcom%2F&tipo_busqueda=1&filtro_texto={searchValue}"
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    
    # Utilizar la sesión persistente para la solicitud HTTP
    response = session.get(url, headers=headers)
    html = response.text
    
    htmlSoup = BeautifulSoup(html, "html.parser")

    # Find the parent div with class "baseTablaMini"
    parentDiv = htmlSoup.find("div", class_="baseTablaMini")
    
    if not parentDiv:
        print("Parent div not found")
        return { "Quimera": [] }

    # Find all <ul> elements within the parent div, limiting to max_results
    productContainer_ul = parentDiv.find_all("ul", class_="mini animacion")[:max_results]

    if not productContainer_ul:
        print("No products found")

    productNames = []
    productPrices = []
    productImages = []
    productLinks = []

    for ul in productContainer_ul:
        # Extract product names
        grid_names = ul.find_all("span", class_="nombreProducto")
        productNames.extend([element.text.strip() for element in grid_names])
        
        # Extract product prices
        grid_prices = ul.find_all("span", class_="precio_final")
        productPrices.extend([element.text.strip() for element in grid_prices])
        
        # Extract product images
        grid_images = ul.find_all("img", class_="lazy")
        productImages.extend(["https://www.airsoftquimera.com" + element.get("data-src") for element in grid_images])
        
        # Extract product links
        grid_links = ul.find_all("a", class_="fotoProducto")
        productLinks.extend(["https://www.airsoftquimera.com" + element.get("href") for element in grid_links])

    # Combine the extracted data into a list of tuples
    productData = list(zip(productNames, productPrices, productImages, productLinks))
    productDict = {
        "Quimera": productData
    }

    return productDict

"""