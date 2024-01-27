# Shopping Web Scraper 
Web Scraper for online shops coded using Python. Can be used to scrap platforms for the best prices and for analysis or any uses you have. Uses Google Chrome.

<b>Current Version:</b> 2.0 <br>
<b>Status:</b> No Longer Updated

## Most Recent Release
### 2.0 (07-11-2020)
Shopee has been added to the scraper!

This uses Shopee's built in API by sending a request to the API with a URL that contains the query search item the user inputs and return the name, price and link of items found. The Shopee results are then thrown into another dataframe and combined with the Lazada dataframe to give the output in an Excel file. Shopee's scraping is done in `shopee.py`. This allows you to have options from Lazada and Shopee to choose from!

## How It Works
1. You input the search string you want to use into the program and run it.
2. The program searches online stores for results of your search and returns you the best results from each platform.
3. The program prints out the results of the search in the console, neatly formatted into a table format.

## Installation & Usage Configuration
### Prerequisites
- Make sure you have python3 and pip installed
- Make sure you have Google Chrome installed
- Make sure you have Git installed

### Steps to Install
1. Clone this repo onto your machine of choice, Windows or Linux is fine. Use `git clone` or `git pull` if you are updating
2. Run `pip install -r requirements.txt` to install all required packages. If this step fails, make sure pip is updated to the most recent version.
3. Run the application using `py scraper.py` and input your search. Wait for the output.
4. Go into `Exports` and find the excel file which contains the results of your search.

Note: If you run the program too many times in a short amount of time, the program may fail due to a platform flagging your IP as suspicious. If this happens, you can wait a while before trying again or use a VPN or different machine if possible.

### Usage Configuration
- Uncomment the two filter lines and fill in any filters you want to use to help you obtain better search results (Optional) 

## Future Plans
- Enable searching all results instead of just first 40 on Lazada
- Add the function of graphs for a separate application, specially for people who want to do long term analysis and comparison between the platforms
- Make an automated system to track price trends for comparison of an item
- Create a GUI so it is easier to use
- Add more platforms like Amazon and Alibaba

## Credits
Technologies and packages used in this project:
- Python   
    - selenium
    - pandas
- Google Chrome Driver
- Shopee Public API

## Support
I am open to contributes and suggestions that can help improve this project. I hope to learn from any ideas you guys can provide and would be glad to have someone want to make changes to help better the project. 

Kindly report any bugs by creating a new issue in the repo and stating clearly what was the error, how was the error caused and what did you search for. 

Thank you!

## License
MIT
