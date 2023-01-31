# New approach to get around issue with ad banner intercepting click
# Scrape initial page using Beautiful Soup
# Make note of the highest page number
# Create new URL that will make soup of pages 2-highest page number

# Imports
from bs4 import BeautifulSoup
import requests
search_query = "peas"

# Initial scrape of search term
def scrapeRecipes(query):
    data = []
    # Request of initial page
    page_to_scrape = requests.get(f"https://theproteinchef.co/recipes/?fwp_search={search_query}")
    # Making soup of first page
    remote_soup = BeautifulSoup(page_to_scrape.text, "html.parser")

    # Scrape initial page
    recipes = remote_soup.find_all("div", attrs={"class":"fl-post-column"})
    # Error handling - no recipes found:
    if recipes:
        for recipe in recipes:
            img = recipe.find("img")["src"]
            name = recipe.find("a")["title"]
            href = recipe.find("a")["href"]
            data.append({"img":img,"name":name,"href":href,"type":search_query})

        # Grab second to last (-2) li element 
        # This will be the LAST pagination button, which will have a text value of the last page # we can search    
        pagination = remote_soup.find("ul", attrs={"class":"page-numbers"})
        pagination_number = None
        if pagination:
            pagination_number = pagination.findChildren("a")[-2].text

        # Iterate from 2 to pagination (highest page number), converted to int
        # Fetch each of these pages, and scrape as above
        if pagination_number:
            try:
                for x in range(2, int(pagination) +1):
                # https://theproteinchef.co/recipes/?fwp_search=breakfast&fwp_paged=2
                    page_to_scrape = requests.get(f"https://theproteinchef.co/recipes/?fwp_search=breakfast&fwp_paged={x}")
                    remote_soup = BeautifulSoup(page_to_scrape.text, "html.parser")
                    recipes = remote_soup.find_all("div", attrs={"class":"fl-post-column"})
                    for recipe in recipes:
                        img = recipe.find("img")["src"]
                        name = recipe.find("a")["title"]
                        href = recipe.find("a")["href"]
                        data.append({"img":img,"name":name,"href":href,"type":search_query})
            except TypeError:
                pass

    return data

data = scrapeRecipes(search_query)
for entry in data:
    print(entry)