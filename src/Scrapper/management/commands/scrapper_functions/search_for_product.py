import os
import random
import json
from lxml import html
import requests
from Levenshtein import distance, ratio
import re
import time
from multiprocessing import Process, Manager
def searchForItem(items: list):
    output_urls = []
    output_titles = []
    index_counter = -1

    for item in items:
        index_counter += 1
        time.sleep(random.uniform(0.5, 1))
        input_title = f"{item}"
        input_title = input_title.strip().replace(' ', '-').lower()
        country_code = "nl"
        language_code = "nl"
        URL = f"https://www.bol.com/{country_code}/{language_code}/s/?searchtext={input_title}"

        # remove trailing white spaces, and normal ones changed to '-' since url will be using it like that
        if country_code != "nl" and country_code != "be":
            raise Exception('Country not supported by Bol.com')

        if language_code != "fr" and language_code != "nl":
            raise Exception('Language not supported')

        # Define the URL of the web page you want to scrape

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/119.0.0.0'
                          'Safari/537.36'
        }

        while True:
            # Check if item is valid EAN
            if item.isdigit() is True and len(item) < 13:
                output_titles.append(f"Item at index: {index_counter} is invalid")
                output_urls.append(f"Item at index: {index_counter} is invalid")
                break

            # Make a request
            response = requests.get(URL, headers=headers)

            # Check the status code
            if response.status_code == 200:
                # print(URL)
                # print(response.status_code)
                page_content = response.content
                parsed_content = html.fromstring(page_content)

                # Xpath for the url of the product
                elements = parsed_content.xpath(
                    "//li[contains(@class, 'product-item--row') and contains(@class, 'js_item_root') and not("
                    "contains(@class, 'js_sponsored_product'))]//a[@role='heading']/@href")

                # error check
                if elements is None:
                    break

                urls_list = []
                titles_list = []
                max_ratio = 0
                best_ratio_match_title = ''
                min_lev_distance = 99999

                for element in elements:
                    try:
                        # Try to access text content of the element
                        element_text = element.text_content().strip()
                        urls_list.append(element_text)
                    except AttributeError:
                        # If it's not an element, it's likely an attribute value, so print it directly
                        urls_list.append(element)

                # Check if item was found or not
                if len(urls_list) == 0:
                    # RETURN STATEMENTS HERE
                    output_titles.append(f"Item at index: {index_counter} is invalid")
                    output_urls.append(f"Item at index: {index_counter} is invalid")
                    break

                # USe regex to separate title from url
                max_match_ratio = 0
                best_match_url = ''
                best_match_title = ''

                for url in urls_list:
                    current_title = re.findall('p\/[a-z,\-,0-9]+', url)[0].replace('p/', '')
                    titles_list.append(current_title)
                    current_ratio = ratio(input_title, current_title)

                    # check if it's an EAN or not
                    if input_title.isdigit():
                        # maybe append these to the output lists
                        best_match_url = url
                        best_match_title = current_title

                    # check for the best match based on normalized indel similarity
                    if current_ratio > max_match_ratio and not input_title.isdigit():
                        max_match_ratio = current_ratio
                        best_match_url = url
                        best_match_title = current_title

                # Print the item with the highest match ratio
                output_urls.append(f"https://bol.com{best_match_url}")
                output_titles.append(best_match_title)
                break
            else:
                print(f"Request failed with status code: {response.status_code}")
                break
    return output_urls




