# Changelog
## 1.1.1 (05-11-2020)
`lazada.py` has also been created to store the code for searching in Lazada. This is to prepare to the near future when Shopee is also rolled out. Each store will have its own python file.

<b>Bugfix:</b> Turns out that during update 1.1, `scraper.py` was not updated and hence the new features were not implemented. It has been updated to reflect it in update 1.1.1.

## 1.1 (24-10-2020)
### Release Highlights
Version 1.1 includes certain changes which added many features listed below. You can now easily access the exact listing you want as links are also exported. 

Easily filter, sort and search through your listings with Excel functionality! You can sort them by prices, by names, and more. When you find the one you like, just click on the link printed beside it!

### Features
- Input prompt to ask for search item instead of needing to change in code
- Export results to an excel sheet stored in the `Exports` folder
- Imported datetime and openpyxl
- Exported links to the specific listings as well

## 1.0 (18-10-2020)
### Release Highlights
Version 1.0 is the first release of my web scraper. At this stage, it is just a simple web scraper that takes in a search item and return the first 40 results, with their names and prices, and outputs them into the console. Printing to console was done so that it is optimized to be used on Linux machines or CLIs with no GUIs.

### Features
- Web scraper for Lazada
- Returns the first 40 results
- Returns price and full item name
- Customizable with filters to improve search results
- Uses Google Chrome browser
- Runs in the background
- Results are printed in the console