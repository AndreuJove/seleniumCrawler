import os
import time
import json
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#Declared variable for avoiding innecessary log from ChromeDriverManager.
os.environ['WDM_LOG_LEVEL'] = '0'

"""
Functions of crawler and managing data files.
"""
#Extract a name for tools:
def extract_id_tool(iterable):
    for tool in iterable:
        if isinstance(tool['id'], list):
            tool['id'] = tool['id'][0]
        tool['id_for_filename'] = tool['id'].split("/")[-1]
    return iterable

#Write on a json file. Input: data and path of the file.
def write_json(data, path):
    with open(path, 'w') as file:
        json.dump(data, file)

#Load json file return the data. Input: and path of the file.
def load_json(path_file):
    with open(path_file) as output:
        return json.load(output)

def get_html_document_with_js(args, tool):
    print(f"INFO: Scraping {tool['final_url']}")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_page_load_timeout(30)
    #Create a empty key value to catch the exception of the website
    tool['exception_selenium'] = ""
    #Request the website if it's available
    try:
        driver.get(tool['final_url'])
    #Catch the exception and write on the log file:
    except Exception as exception:
        tool['exception_selenium'] = f"Get fail in {tool['final_url']}. Exception: {str(exception)}"
        html = ""
    #Seconds to wait for the renderitzation of JavaScript of the website
    time.sleep(5)
    #Extract all the HTML from the website if it's possible
    try:
        html = driver.execute_script("return document.documentElement.outerHTML;")
    #Catch the exception and write on the key exception_selenium of the tool:
    except Exception as exception:
        tool['exception_selenium'] = f"Fail return HTML in {tool['final_url']}. Exception: {str(exception)}"
        html= ""
    #Close the driver
    driver.close()

    #Get the last part of the id to name the file of the HTML
    html_item = {
                    "id" : tool['id'],
                    "html_js" : html
                }

    #Write the item with the id and the html:
    write_json(html_item, f"{args.o_directory_htmls_js}/{tool['id_for_filename']}.json")