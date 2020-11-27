import os
import time
import json
import random
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options



#Declared variable for avoiding innecessary log from ChromeDriverManager.


USER_AGENT_LIST = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:77.0) Gecko/20100101 Firefox/77.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
]

def write_json(data, path):
    # Write on a json file. Input: data and path of the file.
    with open(path, 'w') as file:
        json.dump(data, file)

def load_json(path_file):
    # Load json file return the data. Input: and path of the file.
    with open(path_file) as output:
        return json.load(output)

def get_html_document_with_js(args, logger, tool):

    os.environ['WDM_LOG_LEVEL'] = '0'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.set_page_load_timeout(30)
    driver.execute_cdp_cmd('Network.setUserAgentOverride', {"userAgent": random.choice(USER_AGENT_LIST)})

    try:
        driver.get(tool['final_url'])
        html = driver.execute_script("return document.documentElement.outerHTML;")
    except Exception as exception:
        logger.error(f"Exception {str(exception)}\t\t Website: {tool['final_url']}")
    else:
        html_item = {
                "first_url" : tool['first_url'],
                "final_url" : tool['final_url'],
                "html_js" : html,
            }
        write_json(html_item, f"{args.o_directory_htmls_js}/{tool['path_file']}")
    # Seconds to wait for the renderitzation of JavaScript of the website
    time.sleep(10)
    # Extract all the HTML from the website if it's possible
    
    #Close the driver
    driver.close()

    