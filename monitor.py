import os, sys, django

sys.path.append("/Users/zhou/Documents/Git/IST303-G4-GroupProject") #Set it to the root of your project
os.environ["DJANGO_SETTINGS_MODULE"] = "quest.settings"
django.setup()

import requests
from monitor_log import log as log
import time
from threading import Thread
from datetime import datetime
import random
import json
import sqlite3
from bs4 import BeautifulSoup as soup
from discord_hooks import Webhook
from multiprocessing import Process
from django.shortcuts import get_object_or_404
from products_monitor.models import Product, ProductKeyWord

def send_embed(link, fields, site, image, product, webhook):
    '''
    (str, str, list, str, str, str) -> None
    Sends a discord alert based on info provided.
    '''

    embed = Webhook(webhook, color=123123)

    #if(alert_type == "NEW_SHOPIFY"):
    desc = product
    #elif(alert_type == "RESTOCK_SHOPIFY"):
        #desc = "RESTOCK: " + product

    embed.set_author(name='coplitshoes', icon='')
    embed.set_desc(desc)

    for field in fields:
        #if(alert_type == "NEW_SHOPIFY" or alert_type == "RESTOCK_SHOPIFY"):
            cart_link = site + "/cart/" + str(field[1]) + ":1"
            embed.add_field(name=str(field[0]), value=cart_link)

    if(image is not None):
        embed.set_thumbnail(image)
        embed.set_image(image)

    embed.set_footer(text='coplitshoes', icon='', ts=True)

    embed.post()

# def get_product_keyword(product):
#     keywords = ProductKeyWord.objects.filter(product=product)
#     return keywords
#     #keywords = [(product,keyword), (product,keyword),...]
#     #k=keywords[0]
#     #k.keyword
    
# def get_product_webhook(product):
#     product = get_object_or_404()
#     webhook = Product.objects.filter()

def monitor_shopify(keywords, site, pro):
    log('i', "Monitoring site <" + site + ">.")

    # Create link to monitor (Kith is a special case)
    if("kith.com" in site):
        link = "https://kith.com/collections/footwear.atom"
    else:
        link = site + "/collections/all/products.atom"

    working = False

    # Get the products on the site
    try:
        r = requests.get(link, timeout=3, verify=False)
    except:
        try:
            r = requests.get(link, timeout=5, verify=False)
        except:
            log('e', "Connection to URL <" + link + "> failed.")
            #continue

    xml = soup(r.text, "xml")
    products_raw = xml.findAll('entry')

    # Get products with the specified keywords
    for product in products_raw:
        product_found = False
        for keyword in keywords:
            if(not product_found):
                # Get the product info
                title = product.find("title").text
                link = product.find("link")["href"]
                tags_raw = product.findAll("s:tag")

                tags = []
                for tag in tags_raw:
                    tags.append(tag.text.upper())

                # Check if the keywords are in the product's name or tags
                if(keyword.upper() in title.upper() or keyword.upper() in tags):
                    # Get the variants from the product
                    try:
                        r = requests.get(link + ".xml", timeout=3, verify=False)
                        working = True
                    except:
                        try:
                            r = requests.get(link + ".xml", timeout=5, verify=False)
                            working = True
                        except:
                            working = False

                    # If the site/proxy is working
                    if(working):
                        # Break down the product page
                        xml = soup(r.text, "xml")

                        # Get the variants for the product
                        variants = []
                        raw_variants = xml.findAll("variant")
                        for raw_variant in raw_variants:
                            variants.append((raw_variant.find("title").text, raw_variant.find("id").text))

                        # Get the product's image if it's available
                        try:
                            image = xml.find("image").find("src").text
                        except:
                            image = None

                        product_found = True

                        # Send a Discord alert if the product is new
                        if(product_found and not pro.restock):
                            send_embed(link, variants, site, image, title, webhook)
                            pro.restock = True
                            pro.save()

                        elif(product_found and pro.restock):
                            if(site in site_list):
                                break
                            else:
                                site_list.append(site)
                                send_embed(link, variants, site, image, title, webhook)

                        #elif(product_found and p.restock):
                        #    send_embed("RESTOCK_SHOPIFY", link, variants, site, image, title)

    # Wait the specified timeframe before checking the site again
    time.sleep(5)

if(__name__ == "__main__"):
    # Ignore insecure messages
    requests.packages.urllib3.disable_warnings()

    site = "https://coplitshoes.myshopify.com"
    site_list=[]
    
    #Process(target=monitor_new).start()
    #Thread(target=monitor_restock).start()

    while True:
        p_list = Product.objects.filter(restock=False)
        for p in p_list:
            p_keywords = ProductKeyWord.objects.filter(product=p)
            keywords = []
            for pk in p_keywords:
                print(pk.product.name)
                keywords.append(pk.keyword)
            webhook = p.channelWebhook
            monitor_shopify(keywords, site, p)
        

        r_list = Product.objects.filter(restock=True)
        for r in r_list:
            r_keywords = ProductKeyWord.objects.filter(product=r)
            keywords = []
            for pk in r_keywords:
                print(pk.product.name)
                keywords.append(pk.keyword)
            webhook = "https://discordapp.com/api/webhooks/575850046038212618/nUCvjX7Q4rOFarecc1lli5Jw3rGngTGsGlmx9vcF-G3opNsF_WeH7-b1YNWfeNF_5gl3"
            monitor_shopify(keywords, site, r)