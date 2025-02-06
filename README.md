# Home_Decour_Market_Research
Using amazon best seller web pages scrape data related to home decour and infer valueable insights

Market Research:
1) After Going through various websites like Peperfry, Myntra, Home centre, Ikea got to know what the data is and what are the selling products from each website.
2) Used Amazon Best Seller page as sample data through Web Scraping
3) scraped all the required Home Decour data through Beautiful Soup and converted the data into csv and stored it
4) Transformed the csv file by cleaning missing values, strip strings with whitespaces and converting data type
5) Data ready for analysis used power bi to showcase different matrix of the available data 
6) Compared AVerage price, rating and reviews with categories to find which categories are rated high with high rating, high reviews and finding the average price for each categories. Also found the top 10 selling product.
7) Through analysis and visualizations we can infer (according to this sample data):
- Categories where average price is between 200 to 700 have a rating of greater then 4 and also good number of reviews. This refers that medium priced products are most purchased
- On the other hand expensive products or category with expensive average price have less rating and less customer review.
- According to this trend customer tend to prefer products which are cheap and also portable and usefull the categories include: Home furnishing, Clocks, furniture, Vase, Artwork, Tableware, Candels, Carpets
- Basic Analysis and visuals are created in power bi (Posted a screen shot if power bi is not present in your PC)
- data extracting and transforming done in python with the help of beautiful soup for scraping and pandas for transformation
- Other immplementations: We can also connect this code snippets with Airflow an orchestration software through which we can schedule and automate data pulls for regular fresh data (Did not perform this step since repetetive web scrapping to a particular website may lead to ip ban if you have a verified api then we can do this step)

This is the overiew of this project.
