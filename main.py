import argparse
import json
import time
import os
from functools import partial
from multiprocessing import Pool
from crawler_selenium import get_html_document_with_js

"""

Python Package from crawling websites and saving his HTML with rendered JavaScript.

"""

if __name__ == "__main__":

    start = time.time()

    # Instance of the class ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Crawler for dynamic websites (use of JavaScript) of a set of bioinformatics tools with")

    # Input file for crawling this package: Each tool has: ['name'], ['id'] and ['first_url_tool'] URL of the api to extract the data:
    parser.add_argument(
                        '-input_path_file',
                        type=str,
                        default="../mastercrawlerTFG/output_data/manifest_tools.json",
                        help="File input path")

    # Add the argument of the key acces of the input file:
    parser.add_argument(
                        '-key_access',
                        type=str,
                        default='tools_ok',
                        help="Name of the output key to access for the htmls from crawler. Default: tools_ok"
                        )
    # Add the argument of the ouput directory for htmls_js:
    parser.add_argument(
                        '-o_directory_htmls_js',
                        type=str,
                        default="htmls_js",
                        help="Name of the output directory for the htmls from crawler. Default: htmls_js"
                        )

    #Add the argument of the ouput directory for htmls_js:
    parser.add_argument(
                        '-o_directory_data',
                        type=str,
                        default="output_data_selenium",
                        help="Name of the output directory manifest ouput file, that gives the path to each tool. Default: output_data"
                        )

    #Add the argument of the output file:                 
    parser.add_argument(
                        '-output_file',
                        type=str,
                        default="manifest_tools_js",
                        help="Name of the output manifest file of the of selenium crawler. Default is: manifest_tools_js"
                        )

    args = parser.parse_args()

    #Open json file and transformed to a list of dictionaries.
    #Each dictionary has 2 keys: 'final_url_tool' and 'idTool'.
    with open(args.input_path_file, "r") as fp:
        tools_to_crawl = json.load(fp)

    # Check if the directory for output_data exists and if not exists create it:
    if not os.path.isdir(args.o_directory_data):
        os.mkdir(args.o_directory_data)
    
    #Check if the directory for HTMLs exists and if not exists create it:
    if not os.path.isdir(args.o_directory_htmls_js):
        os.mkdir(args.o_directory_htmls_js)

    # Pass args as arguments to pool:
    func = partial(get_html_document_with_js, args)

    print(f"INFO: Starting the crawler of {len(tools_to_crawl[args.key_access])}, this can take aproach 2h30minutes of execution.")
    #Instance class Pool with 12 processes simultanously:
    pool = Pool(processes=2)
    #Call the function and passs the data to crawl:
    pool.map(func, tools_to_crawl[args.key_access][:2])

    

    #print Time of execution of the crawler:
    end = time.time()
    print("\n\nTime of execution of the crawler:")
    print(end - start)
