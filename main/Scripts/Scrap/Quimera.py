from bs4 import BeautifulSoup
from ...WebConfig import SEARCH_SETTINGS
max_results = SEARCH_SETTINGS.get("MAX_RESULTS_PER_ENGINE")

def GetProducts(searchValue, session):
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
