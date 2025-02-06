import requests
from bs4 import BeautifulSoup
import time
import csv

# Set up Selenium WebDriver



url = [["https://www.amazon.in/gp/bestsellers/kitchen/5229870031/ref=zg_bs_pg_1_kitchen?ie=UTF8&pg=1","Artificial Flora"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/1380375031/ref=zg_bs_pg_1_kitchen?ie=UTF8&pg=1", "Artwork"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/1380378031/ref=zg_bs_pg_1_kitchen?ie=UTF8&pg=1","Ashtray"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/1380380031/ref=zg_bs_nav_kitchen_2_1380378031","Candel Holders"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/1380385031/ref=zg_bs_nav_kitchen_2_1380374031","Candels"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/5554166031/ref=zg_bs_nav_kitchen_2_1380374031","Children Decour"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/1380392031/ref=zg_bs_nav_kitchen_2_1380374031","Clocks"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/1380401031/ref=zg_bs_nav_kitchen_3_51396691031","Decorative Bowls"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/1380379031/ref=zg_bs_nav_kitchen_3_1380401031","Decorative Boxes"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/51396693031/ref=zg_bs_nav_kitchen_3_1380379031","Jars"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/1380544031/ref=zg_bs_nav_kitchen_3_51396693031","Magzine/paper Holder"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/22809165031/ref=zg_bs_nav_kitchen_2_1380374031","Decorative Accesories"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/5242296031/ref=zg_bs_nav_kitchen_2_1380374031","Pebels/Vase Fillers"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/5459540031/ref=zg_bs_nav_kitchen_2_1380374031","Fountains"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/1380542031/ref=zg_bs_nav_kitchen_2_1380374031","Magnets"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/1380408031/ref=zg_bs_nav_kitchen_2_1380374031","Mirrors"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/1380418031/ref=zg_bs_nav_kitchen_2_1380374031","Vase"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/1380098031/ref=zg_bs_nav_kitchen_2_5925789031","Tableware"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/8464342031/ref=zg_bs_nav_kitchen_2_1380510031","Home Storage"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/1380442031/ref=zg_bs_nav_kitchen_1","Home Furnishing"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/1380441031/ref=zg_bs_nav_kitchen_1","Furniture"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/1380485031/ref=zg_bs_nav_kitchen_1","Lightings"],
       ["https://www.amazon.in/gp/bestsellers/kitchen/1380462031/ref=zg_bs_nav_kitchen_2_1380442031","Carpets/Rugs"]]

ans = []
for links,name in url:
    response = requests.get(links)
    time.sleep(3)


    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")

        # Find all the products
        products = soup.find_all("div", id="gridItemRoot")

        # Loop through the products and extract the data
        
        for information in products:

            # Extract product name
            name_tag = information.find("div", class_="_cDEzb_p13n-sc-css-line-clamp-3_g3dy1")
            product_name = name_tag.text.strip() if name_tag else "N/A"

            # Extract price
            price_tag = information.find("span", class_="p13n-sc-price")
            product_price =  price_tag.text.strip() if price_tag else "0"
            product_price = product_price[1:] if product_price != "0" else "0"
            


            # Extract rating and total reviews
            rating_tag = information.find("a", title=True)  # Finding <a> tag with title attribute
            if rating_tag:
                rating_text = rating_tag["title"].strip()
                rating_parts = rating_text.split(" ")  # Splitting "4.3 out of 5 stars, 10,245 ratings"
                product_rating = rating_parts[0]
                total_reviews = rating_parts[5]  # Extract number part
            else:
                product_rating = "N/A"
                total_reviews = "N/A"

            ans.append([product_name,name,product_price,product_rating,total_reviews])
           
    else:
        print("Failed to retrieve the webpage.")
        
csv_filename = "amazon_products1.csv"

# Writing data to CSV
with open(csv_filename, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.writer(file)

    # Write the header row
    writer.writerow(["Product Name", "Category", "Price", "Rating", "Reviews"])

    # Write all product data
    writer.writerows(ans)