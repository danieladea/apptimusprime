import requests
from bs4 import BeautifulSoup
import time
    
def main():
    s = raw_input("Enter product name: ")
    amazon(s)
    

def spider(url):
   # source = requests.get(url)
    source = requests.get("https://www.amazon.com/gp/product/B000QSTBNS?pf_rd_p=183f5289-9dc0-416f-942e-e8f213ef368b&pf_rd_r=DYCE5XJW3FXH4K5EK9P5")
    ptext = source.text
    soup = BeautifulSoup(ptext, "html.parser")
    print ("soup")
    return soup


def amazon(s):
    s = s.replace(" ", "+")
    url = "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + str(s)
    soup = spider("https://www.amazon.com/gp/product/B000QSTBNS?pf_rd_p=183f5289-9dc0-416f-942e-e8f213ef368b&pf_rd_r=DYCE5XJW3FXH4K5EK9P5")
    print("yuh")
    time.sleep(5)
    print("yuh2")
    for link in soup.findAll('a', {'class': 'a-link-normal', 'class': 's-access-detail-page',
                                   'class': 'a-text-normal'}):
        print("yuh3")
        if(link.get('href')):
            href = link.get('href')
            time.sleep(5)
            print("yuh4")
            price_checker(href)
            break
       
        

def price_checker(url):   
   soup = spider(url)
   p_name = soup.find(attrs={'id':'productTitle'})
   print("Hello")
   print ("Name: " +str(p_name.string.strip()))
  # print(soup.get_text())
   p_our_price = soup.find(attrs={'id':'priceblock_ourprice'})
   p_deal_price = soup.find(attrs={'id':'priceblock_dealprice'})
   p_sale_price = soup.find(attrs={'id':'priceblock_saleprice'})
   if p_deal_price:
        new_price=p_deal_price.text.replace(',','').strip()
   elif p_our_price:
        new_price=p_our_price.text.replace(',','').strip()
   elif p_sale_price:
        new_price=p_sale_price.text.replace(',','').strip()
   print ("Price: $" + new_price)
 
    

main()
