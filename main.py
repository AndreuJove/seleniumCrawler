import argparse
import json
import time
from multiprocessing import Pool
from crawler_selenium import get_HTML_document_with_JS
import os
from functools import partial


if __name__ == "__main__":

    start = time.time()
    # Instance of the class ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Crawler for dynamic websites (use of JavaScript) of a set of bioinformatics tools with")

    # Input file for crawling this package: Each tool has: ['name'], ['id'] and ['first_url_tool'] URL of the api to extract the data:
    parser.add_argument('-i_path_file', '--input_path_list_tools', type=str, 
                    default="input_data/tools_for_crawling_js.json",
                    help="File of tools for crawling. Each tool has: ['id'] and ['final_url_tool']")

    # Add the argument of the ouput directory for htmls_js:
    parser.add_argument('-o_directory_htmls_js', '--output_directory_htmls', type=str,
                    default="htmls_js", help="Name of the output stats file from crawler")
    
    args = args = parser.parse_args()

    #Open json file and transformed to a list of dictionaries.
    #Each dictionary has 2 keys: 'final_url_tool' and 'idTool'.
    with open(args.input_path_list_tools, "r") as fp:
        tools_to_crawl = json.load(fp)

    # Check if the directory exists and if not exists create it:
    if not os.path.isdir(args.output_directory_htmls):
        os.mkdir(args.output_directory_htmls)

    # Pass args as arguments to pool:
    func = partial(get_HTML_document_with_JS, args)

    #Instance class Pool with 12 processes simultanously:      
    pool = Pool(processes=12)
    #Call the function and passs the data to crawl:
    pool.map(func, tools_to_crawl[:14])


    #print Time of execution of the crawler:
    end = time.time()
    print("\n\nTime of execution:")
    print(end - start)
