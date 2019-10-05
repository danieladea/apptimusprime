import requests
from bs4 import BeautifulSoup
import time
    
def main():
    s = raw_input("Enter product name: ")
    amazon(s)
    

def spider(url):
    source = requests.get(url)
    ptext = source.text
    soup = BeautifulSoup(ptext, "html.parser")
    print ("\n")
    return soup


def amazon(s):
    s = s.replace(" ", "+")
    url = "http://www.amazon.com/s/ref=nb_sb_noss?url=search-alias%3Daps&field-keywords=" + str(s)
   # soup = spider("https://www.amazon.com/gp/product/B000QSTBNS?pf_rd_p=183f5289-9dc0-416f-942e-e8f213ef368b&pf_rd_r=DYCE5XJW3FXH4K5EK9P5")
   # soup = spider("https://www.amazon.com/s?k=optimum+nutrition+whey+protein&crid=3LUZ24YRM6NGT&sprefix=optimum%2Caps%2C361&ref=nb_sb_ss_i_1_7")
    soup = spider(url)
    time.sleep(5)
    result = soup.prettify().splitlines()
#    print('\n'.join(result[:1600] + result[-1600:]))
    for link in soup.findAll('a', {'class': 'a-link-normal', 'class': 's-access-detail-page',
                                   'class': 'a-text-normal'}):
        print(link)
        if(link.get('href')):
            print("afterif")
#            print(link)
            href = link.get('href')
            time.sleep(3)
            price_checker('https://www.amazon.com' +href)
            break
       
        

def price_checker(url):   
   soup = spider(url)
   p_name = soup.find(attrs={'id':'productTitle'})
   print ("Name: " +str(p_name.string.strip()))
   p_our_price = soup.find(attrs={'id':'priceblock_ourprice'})
   p_deal_price = soup.find(attrs={'id':'priceblock_dealprice'})
   p_sale_price = soup.find(attrs={'id':'priceblock_saleprice'})
   if p_deal_price:
        new_price=p_deal_price.text.replace(',','').strip()
   elif p_our_price:
        new_price=p_our_price.text.replace(',','').strip()
   elif p_sale_price:
        new_price=p_sale_price.text.replace(',','').strip()
   print ("Price: "+new_price)
 
    

main()
