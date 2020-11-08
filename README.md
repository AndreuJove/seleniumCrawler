
## Crawler description:
This crawler aims to extract the HTMLs with JavaScript render from the websites of a dataset of bioinformatic tools.

#### Input:
- Dataset of bioinformatics tools (used to get the websites of the bioinformatic tools).

#### Output:


- JSON file called by default by the name of each tool inside the directory of htmls_no_js that follows the next JSON schema:


```

type="string" = {
  'id' : type="string",
 
  'html_js' : type="string"                 
}

```

<br />


## Package installation:

- 1) Open terminal.
- 2) Go to the current directory where you want the cloned directory to be added using 'cd'.
- 3) Run the command: <br />
        $ git clone https://github.com/AndreuJove/seleniumCrawler.
- 4) Install requirements.txt:<br />
        $ pip3 install -r requirements.txt
- 5) Run the following command:<br />
        $ python3 main.py
- 6) The name of the output files and the directory to save them can be changed using the following command line (write it with the default values):<br />
        $ python3 main.py 
        -input_path_file ../mastercrawlerTFG/output_data/manifest_tools.json
        -key_access tools_ok
        -o_directory_htmls_js htmls_js
        -o_directory_data output_data_selenium
        -output_file manifest_tools_js
<br />
<br />


## Build with:
- [Selenium](https://selenium-python.readthedocs.io/) - Selenium is an open-source web-based automation tool. With the usage of a Webdriver it can be used to render JavaScript on websites.
- [Webdriver-manager](https://pypi.org/project/webdriver-manager/) - WebDriver-Manager is a free open source library that automatically manages our different browser drivers and saves us all the time and effort spent in manually managing the drivers. Basically what it does is, check for the latest version of the WebDriver binary, download it if it’s not present on your system and then export the required WebDriver environment variables needed by Selenium.


<br />
<br />


## Authors

Andreu Jové

<br />
<br />


## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3 - see the [LICENSE.MD](https://github.com/AndreuJove/mastercrawlerTFG/blob/master/LICENSE.md) file for details.