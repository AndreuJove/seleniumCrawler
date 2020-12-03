
"""

Python Package from crawling websites and saving his HTML with rendered JavaScript.

"""

import argparse
import json
import logging
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

    start_time = time.time()
     # Create the logger:
    logging.basicConfig(
                        level=logging.DEBUG,
                        format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                        datefmt='%m-%d %y %H:%M:%S',
                        filename=f'{args.log_file_name}.log',
                        filemode='w'
                        )

    websites = load_json(args.input_path_file)

    # Define a Handler which writes INFO messages or higher to the sys.stderr
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    # Set a format which is simpler for console use
    formatter = logging.Formatter('%(levelname)-12s %(filename)-12s %(message)s')

    # Tell the handler to use this format
    console.setFormatter(formatter)

    # Add the handler to the root logger
    logging.getLogger().addHandler(console)

    logger = logging.getLogger(__name__)

    # Pass args as arguments to pool:
    func = partial(get_html_document_with_js, args, logger)

    # Instance class Pool with 12 processes simultanously:
    pool = Pool(processes=12)

    logging.info(f"Websites to crawl: {len(websites[args.key_access])}.")

    logging.info("Starting the crawler. ESTIMATION TIME: 4h.")

    # Call the function and pass the data to crawl:
    pool.map(func, websites[args.key_access])

    # Extract the websites saved in the directory.
    list_files = os.listdir(args.o_directory_htmls_js)

    # last logging info:
    logging.info(f"INFO: Websites INPUT: {len(websites[args.key_access])}")
    logging.info(f"HTMLs saved: {len(list_files)}")
    logging.info(f"Time of execution: {time.time() - start_time} seconds.")

if __name__ == "__main__":

    # Instance of the class ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Extract HTMLs with JavaScript rendered.")

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
                        help="Input key file. Default: tools_ok"
                        )

    # Add the argument of the ouput directory for htmls_js:
    parser.add_argument(
                        '-o_directory_htmls_js',
                        type=str,
                        default="htmls_js",
                        help="Name of the output directory for HTMLs. Default: htmls_js"
                        )

    # Add the argument of output's directory name of log:
    parser.add_argument(
                        '-log_file_name',
                        type=str,
                        metavar="",
                        default="selenium",
                        help="Name of the output log file of the program"
                        )

    args = parser.parse_args()

    # Check if the directory for HTMLs exists and if not exists create it:
    if not os.path.isdir(args.o_directory_htmls_js):
        os.mkdir(args.o_directory_htmls_js)

    main(args)
