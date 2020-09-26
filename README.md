
## Crawler description:
This crawler aims to extract the HTMLs with JavaScript render from the websites of a dataset of bioinformatic tools.

#### Input:
- Dataset of bioinformatics tools (used to get the websites of the bioinformatic tools).

#### Output:
- Each HTML with JavaScript rendered in a JSON file. The name of the file is the Id of the bioinformatic tool. 
<br />


## Package installation:

- 1) Open terminal.
- 2) Go to the current directory where you want the cloned directory to be added using 'cd'.
- 3) Run the command: 
        $ git clone https://github.com/AndreuJove/seleniumCrawler.
- 4) Install requirements.txt:
        $ pip3 install -r requirements.txt
- 5) Run the following command:
        $ python3 crawler_selenium.py
<br />


## Build with:
- [Selenium](https://selenium-python.readthedocs.io/) - Selenium is an open-source web-based automation tool. With the usage of a Webdriver it can be used to render JavaScript on websites.
- [Webdriver-manager](https://pypi.org/project/webdriver-manager/) - WebDriver-Manager is a free open source library that automatically manages our different browser drivers and saves us all the time and effort spent in manually managing the drivers. Basically what it does is, check for the latest version of the WebDriver binary, download it if it’s not present on your system and then export the required WebDriver environment variables needed by Selenium.


<br />


## Authors

Andreu Jové

<br />


## License

This project is licensed under the GNU GENERAL PUBLIC LICENSE Version 3 - see the [LICENSE.MD](https://github.com/AndreuJove/mastercrawlerTFG/blob/master/LICENSE.md) file for details.