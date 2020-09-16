from selenium import webdriver
import time
from multiprocessing import Pool
import json
from webdriver_manager.chrome import ChromeDriverManager
import os

start = time.time()
path_tools_to_crawl_js = "../mastercrawlerTFG/mastercrawler/tools_for_crawling_js.json"

with open(path_tools_to_crawl_js, "r") as fp:
    tools_to_crawl = json.load(fp)

logf = open("download.log", "w")

def get_HTML_document_with_JS(tool):
    print(tool['final_url_tool'])
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
    item_dict_url = {'final_url_tool' : tool['final_url_tool']}
    item_dict_html_js = {'html_js' : html}
    list_with_dict_items = []
    list_with_dict_items.append(item_dict_url)
    list_with_dict_items.append(item_dict_html_js)
    unique_id = tool['idTool'].split("/")[-1]
    path_save_scraped_website = f"htmls_js/{unique_id}.json"
    with open(path_save_scraped_website, 'w') as f:
        json.dump(list_with_dict_items, f)

        
pool = Pool(processes=12)
pool.map(get_HTML_document_with_JS, tools_to_crawl)


end = time.time()
print("\n\nTime of execution:")
print(end - start)

# os.system('systemctl poweroff') 
