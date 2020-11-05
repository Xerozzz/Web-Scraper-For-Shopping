# Shopping Web Scraper 
Web Scraper for online shops coded using Python. Can be used to scrap platforms for the best prices and for analysis or any uses you have. Uses Google Chrome.

<b>Current Version:</b> 1.1.1 <br>
<b>Status:</b> Regularly updated

## Most Recent Release
### 1.1.1 (05-11-2020)
Version 1.1 includes certain changes which added many features listed below. You can now easily access the exact listing you want as links are also exported. 

Easily filter, sort and search through your listings with Excel functionality! You can sort them by prices, by names, and more. When you find the one you like, just click on the link printed beside it!

`lazada.py` has also been created to store the code for searching in Lazada. This is to prepare to the near future when Shopee is also rolled out. Each store will have its own python file.

<b>Bugfix:</b> Turns out that during update 1.1, `scraper.py` was not updated and hence the new features were not implemented. It has been updated to reflect it in update 1.1.1

## How It Works
1. You input the search string you want to use into the program and run it.
2. The program searches online stores for results of your search and returns you the best 40 results from each platform. You may apply filters to make the search results more accurate
3. The program prints out the results of the search in the console, neatly formatted into a table format.

## Installation & Usage Configuration
### Prerequisites
- Make sure you have python3 and pip installed
- Make sure you have Google Chrome installed
- Make sure you have Git installed

### Steps to Install
1. Clone this repo onto your machine of choice, Windows or Linux is fine. Use `git clone` or `git pull` if you are updating
2. Run `pip install -r requirements.txt` to install all required packages. If this step fails, make sure pip is updated to the most recent version.
3. Go into `scraper.py` and configure based on the options stated below in the Usage Configuration section
4. Run the application using `py scraper.py` and input your search. Wait for the output.

Note: If you run the program too many times in a short amount of time, the program may fail due to Lazada flagging your IP as suspicious. If this happens, you can wait a while before trying again or use a VPN or different machine if possible.

### Usage Configuration
- Uncomment the two filter lines and fill in any filters you want to use to help you obtain better search results (Optional) 

## Future Plans
- To add Shopee and other platforms in as well for comparison
- Enable searching all results instead of just first 40

## Credits
Technologies and packages used in this project:
- Python   
    - selenium
    - pandas
    - matplotlib
    - seaborn
- Google Chrome Driver

## Support
I am open to contributes and suggestions that can help improve this project. I hope to learn from any ideas you guys can provide and would be glad to have someone want to make changes to help better the project. 

## License
MIT
