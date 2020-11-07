import os
import time
import json
import logging
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

os.environ['WDM_LOG_LEVEL'] = '0'

"""
Functions of crawler and managing data files
"""

#Save the item in manifest, for a posterior searching
def save_item_in_manifest(item, path):
    data = load_json(path)
    data['tools_ok_js'].append(item)
    write_json(data, path)

#This function is called ones to create the template of the output file of the crawler
def create_file_manifest(path):
    list_tools = []
    final_dict = {"tools_ok_js" : list_tools}
    write_json(final_dict, path)
    
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
        tool['exception_selenium'] = "Fail return HTML in {tool['final_url']}. Exception: {str(exception)}"
        html= ""
    #Close the driver
    driver.close()

    #Get the last part of the id to name the file of the HTML
    html_item = {
                    "id" : tool['id'],
                    "html_js" : html
                }

    #Create the new path for acces the HTML with JS of the URL.
    tool['path_html_js'] = tool['path_file'].replace("no_", "")

    #Write the item with the id and the html:
    write_json(html_item, f"{args.o_directory_htmls_js}/{tool['path_html_js']}")

    #Create the path for the manifest of the output of the program
    path_file_manifest = f"{args.o_directory_data}/{args.output_file}.json"

    #Try to load the the manifest file
    if not os.path.isfile(path_file_manifest):
        create_file_manifest(path_file_manifest)

    #Save the new item of the crawler to the manifest json
    save_item_in_manifest(tool, path_file_manifest)





