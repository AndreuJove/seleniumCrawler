from selenium import webdriver
import time
from multiprocessing import Pool
import json
from webdriver_manager.chrome import ChromeDriverManager
import os

start = time.time()

#Path to input data for crawler.
path_tools_to_crawl_js = "../mastercrawlerTFG/mastercrawler/tools_for_crawling_js.json"

#Open json file and transformed to a list of dictionaries.
#Each dictionary has 2 keys: 'final_url_tool' and 'idTool'.
with open(path_tools_to_crawl_js, "r") as fp:
    tools_to_crawl = json.load(fp)

#Log for catching exceptions during crawling:
logf = open("download.log", "w")

def get_HTML_document_with_JS(tool):
    print(tool['final_url_tool'])
    #Instance class webdriver with ChromeDriverManager:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    try:
        driver.get(tool['final_url_tool'])
    except Exception as a:
        logf.write("Failed in tool {0}: {1}\n".format(str(tool), str(a)))
        html = ""
    time.sleep(5)
    try:
        html = driver.execute_script("return document.documentElement.outerHTML;")
    except Exception as e:
        logf.write("Failed in tool {0}: {1}\n".format(str(tool), str(e)))
        html= ""
    driver.close()
    list_with_dict_items = [{'final_url_tool' : tool['final_url_tool']}, {'html_js' : html}]
    unique_id = tool['idTool'].split("/")[-1]
    path_save_scraped_website = f"htmls_js/{unique_id}.json"
    with open(path_save_scraped_website, 'w') as f:
        json.dump(list_with_dict_items, f)


#Instance class Pool with 12 processes simultanously:      
pool = Pool(processes=12)
#Call the function and passs the data to crawl:
pool.map(get_HTML_document_with_JS, tools_to_crawl)


#print Time of execution of the crawler:
end = time.time()
print("\n\nTime of execution:")
print(end - start)


