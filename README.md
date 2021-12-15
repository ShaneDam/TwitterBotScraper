# TwitterBotScraper
Built a little scraper bot that analyzes the latest 1000 tweets on a desired search term. It uses Selenium and Chrome web driver to gather the data and returns 2 word clouds (tweets’ text &amp; associated #’s; distinguishable by their white &amp; black background color) along with a pie chart of a sentiment analysis and a table with the total number of retweets, replies and likes grouped by the sentiments (named RRL_table).

# References:
1.	Selenium (Chrome driver) installment:
https://pypi.org/project/selenium/ 
https://chromedriver.chromium.org/downloads
https://chromedriver.storage.googleapis.com/index.html?path=96.0.4664.45/
2.	Selenium documentation:
https://selenium-python.readthedocs.io/
3.	XPath basics & tutorial:
https://www.w3schools.com/xml/xpath_intro.asp 
4.	SelectorsHub XPath Plugin 
https://chrome.google.com/webstore/detail/selectorshub-xpath-plugin/ndgimibanhlabgdgjcpbbndiehljcpfh 
5.	Textblob sentiment analysis:
https://towardsdatascience.com/my-absolute-go-to-for-sentiment-analysis-textblob-3ac3a11d524
6.	Word cloud:
https://www.geeksforgeeks.org/generating-word-cloud-python/ 
7.	Pie Chart:
https://matplotlib.org/3.1.1/gallery/pie_and_polar_charts/pie_features.html 
8.	Deployment of results/visualization:
https://github.com/plotly/dash/issues/71 
9.	Idea/inspiration:
https://github.com/israel-dryer/Twitter-Scraper 
