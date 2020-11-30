
## Crawler description:
This crawler aims to extract the HTMLs with JavaScript render from the websites of a dataset of bioinformatic tools.

#### Input:
- JSON file called by default "manifest_tools_scrapy.json" from [mastercrawlerTFG](https://github.com/AndreuJove/mastercrawlerTFG).

#### Output:


- JSON file called by default by the name of each tool inside the directory of htmls_no_js that follows the next JSON schema:


```

type="string" = {
  'first_url' : type="string",

  'final_url'   : type="string,
 
  'html_js' : type="string"                 
}

```

<br />


## Package installation:

1) Open terminal.
2) Go to the current directory where you want the cloned directory to be added using 'cd'.
3) Run the command: <br />
        $ git clone https://github.com/AndreuJove/seleniumCrawler.
4) Install requirements.txt:<br />
        $ pip3 install -r requirements.txt
5) Run the following command:<br />
        $ python3 main.py
6) The name of the output files and the directory to save them can be changed using the following command line (write it with the default values):<br />
        $ python3 main.py <br />
        -input_path_file "../mastercrawlerTFG/output_data/manifest_tools_scrapy.json" <br />
        -key_access "tools_ok" <br />
        -o_directory_htmls_js "htmls_js" <br />
        -log_file_name "selenium" <br />
<br />



## Build with:
- [Selenium](https://selenium-python.readthedocs.io/) - Selenium is an open-source web-based automation tool. With the usage of a Webdriver it can be used to render JavaScript on websites.
- [Webdriver-manager](https://pypi.org/project/webdriver-manager/) - WebDriver-Manager is a free open source library that automatically manages our different browser drivers and saves us all the time and effort spent in manually managing the drivers. Basically what it does is, check for the latest version of the WebDriver binary, download it if it’s not present on your system and then export the required WebDriver environment variables needed by Selenium.
- [Multiprocessing](https://docs.python.org/3/library/multiprocessing.html) - multiprocessing is a package that supports spawning processes using an API similar to the threading module. The multiprocessing package offers both local and remote concurrency, effectively side-stepping the Global Interpreter Lock by using subprocesses instead of threads. Due to this, the multiprocessing module allows the programmer to fully leverage multiple processors on a given machine.
- [Argparser](https://docs.python.org/3/library/argparse.html) - The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.
- [Logging](https://docs.python.org/3/howto/logging.html) - Logging is a means of tracking events that happen when some software runs. The software’s developer adds logging calls to their code to indicate that certain events have occurred.

<br />
<br />


## Authors

Andreu Jové

<br />
<br />


## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3 - see the [LICENSE.MD](https://github.com/AndreuJove/mastercrawlerTFG/blob/master/LICENSE.md) file for details.