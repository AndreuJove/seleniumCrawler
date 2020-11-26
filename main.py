
"""

Python Package from crawling websites and saving his HTML with rendered JavaScript.

"""

import argparse
import json
import time
import os
from functools import partial
from multiprocessing import Pool
from crawler_selenium import get_html_document_with_js


def load_json(path_file):
    # Load json file return the data. Input: and path of the file.
    with open(path_file) as output:
        return json.load(output)

def main(args):

    websites = load_json(args.input_path_file)
    
    # Pass args as arguments to pool:
    func = partial(get_html_document_with_js, args)

    print(f"INFO: Starting the crawler of {len(websites[args.key_access])}, this can take aproach 2h30minutes of execution.")
    
    # Instance class Pool with 12 processes simultanously:
    pool = Pool(processes=12)

    # Call the function and passs the data to crawl:
    pool.map(func, websites[args.key_access])

    list_files = os.listdir(args.o_directory_htmls_js)

    print(f"INFO: Websites INPUT: {len(websites[args.key_access])}")
    print(f"HTMLs saved: {len(list_files)}")

if __name__ == "__main__":

    # Instance of the class ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Crawler for dynamic websites (use of JavaScript) of a set of bioinformatics tools with")

    # Input file for crawling this package: array of websites.
    parser.add_argument(
                        '-input_path_file',
                        type=str,
                        default="../mastercrawlerTFG/output_data/manifest_tools_scrapy.json",
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

    args = parser.parse_args()

    # Check if the directory for HTMLs exists and if not exists create it:
    if not os.path.isdir(args.o_directory_htmls_js):
        os.mkdir(args.o_directory_htmls_js)

    main(args)

