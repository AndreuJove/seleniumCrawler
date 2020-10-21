from selenium import webdriver
import time
import json
from webdriver_manager.chrome import ChromeDriverManager

#Log for catching exceptions during crawling:
logf = open("download.log", "w")

def get_HTML_document_with_JS(args, tool):
    #Instance class webdriver with ChromeDriverManager to get the latest version of the WebDriver:
    driver = webdriver.Chrome(ChromeDriverManager().install())
    #Request the website if it's available
    try:
        driver.get(tool['final_url_tool'])
    #Catch the exception and write on the log file:
    except Exception as a:
        logf.write("Failed in request of the tool {0}: {1}\n".format(str(tool), str(a)))
        html = ""
    #Seconds to wait for the renderitzation of JavaScript of the website
    time.sleep(5)
    #Extract all the HTML from the website if it's possible
    try:
        html = driver.execute_script("return document.documentElement.outerHTML;")
    #Catch the exception and write on the log file:
    except Exception as e: 
        logf.write("Failed to return the HTML in tool {0}: {1}\n".format(str(tool), str(e)))
        html= ""
    driver.close()
    #Get the last part of the id to name the file of the HTML
    unique_id = tool['idTool'].split("/")[-1]
    if html:
        with open(f"{args.output_directory_htmls}/{unique_id}.json", 'w') as f:
            json.dump([{'final_url_tool' : tool['final_url_tool']}, {'html_js' : html}], f)



