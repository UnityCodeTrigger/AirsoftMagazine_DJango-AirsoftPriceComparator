from bs4 import BeautifulSoup
from ...WebConfig import SEARCH_SETTINGS
max_results = SEARCH_SETTINGS.get("MAX_RESULTS_PER_ENGINE")

def GetProducts(searchValue, session):
    url = f"https://shermansurvival.com/?mot_q={searchValue}"
    
    # Utilizar la sesión persistente para la solicitud HTTP
    response = session.get(url)
    html = response.text
    
    htmlSoup = BeautifulSoup(html, "html.parser")
    main_element = htmlSoup.find("main")

    productContainer_ul = main_element.find("ul")
    
    print(productContainer_ul)
    
    if not productContainer_ul:
        return { "Sherman": [] }

    productContainer_li = productContainer_ul.find_all("li")  # Remove slicing to find all results
    productContainer_li = productContainer_li[:max_results]
    print(productContainer_li)
    
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
