# Hackathons Dataset!

   ![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen) ![enter image description here](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=Selenium&logoColor=white) ![enter image description here](https://img.shields.io/badge/Colab-F9AB00?style=for-the-badge&logo=googlecolab&color=525252)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/revanth-reddy/tamudatathon/)

> This [Dataset](https://github.com/revanth-reddy/tamudatathon/blob/master/hackathons_data.csv) is built as a part of TAMU Datathon 2021. It contains the
> details of hackathon which include Title, Location, Start Date, End
> Date, Prize Money, Number of Participants, Host of Hackathon, Themes
> in the Hackathon

> As a part of [Tamu Datathon 2021](https://tamudatathon.com/) challenges, we approached the problem of  synthesis of Hackathons Dataset throughtout the world.

## Construction of Dataset

The data for this dataset is obtained by Web Scraping using Python and Selenium.

## Problems

 - While scraping the website, the content inside website is not rendered as static content. 
 - As the content is dynamic one, it is hard to scrape.
 - The website has a pagination effect based on page scrolling. So, initially `x` items are loaded in the website and on scrolling another `x` items are loaded and so on.
 - Unless we scroll we can't scrape the entire dataset.
## Team's Approach

- We have used Selenium to scrape the website.
- We used a Chrome Web Driver to create the automation of scrolling and scraping the data.
- After Scraping, we got the raw data which is processed further and cleaned.
- The clean data is stored as a dataset in a CSV file.
- Unique datapoints like Number of participants, Start Date, End Date, Location(Online/Offline location), Prize Money, Themes

## Uses

- To Observe the trends:
	- Number of Hackathons per year.
	- Hackathons Prize Money Trend over years.
	- Rise of Themes through the years.
	- Participation in the Hackathon across years/themes.
	-  And many more ...
- To Build ML models in order :
	-  to predict Prize Money based on other features like participation, themes, location.
	- to estimate user participation based on location, prize money, themes, etc.
	- to analyze relationship between the above features.


## Visualization
- Insights: https://datastudio.google.com/reporting/269afbc3-e982-4fef-aee5-08010b427070

![Visualization Image](https://raw.githubusercontent.com/revanth-reddy/tamudatathon/master/visualization.png)

## Team
[![Site https://github.com/pcarribean/](https://img.shields.io/badge/MANISHA-DEV-lightgray)](https://github.com/pcarribean/) [![Site https://github.com/msharsha/](https://img.shields.io/badge/MSHARSHA-DEV-brightgreen)](https://github.com/msharsha) [![Site https://github.com/revanth-reddy/](https://img.shields.io/badge/REVANTH-DEV-skyblue)](https://github.com/revanth-reddy/)