# The Wildfire Network

![Scrolling through The Wildfire Network website](demo.gif)
_Homepage: Includes the most recent wildfire news scraped from the internet and a map of wildfire hotspots._

![Demo of Wildfire Risk Predictor](https://res.cloudinary.com/devpost/image/fetch/s--u03Kv-Oc--/c_limit,f_auto,fl_lossy,q_auto:eco,w_900/https://github.com/wang-owen/TheWildfireNetwork/assets/69203168/8286a445-2d95-470e-92c4-7e7d23c49bd2)
_Prediction Page: Enter your postal code or city, and we'll fetch the weather data to calculate the wildfire risk._

Watch our video demo on [Devpost](https://devpost.com/software/the-wildfire-network)! 📽️

## Inspiration

Our web app was inspired by the increasing frequency and severity of wildfires in Canada and globally. We created this app during **Ignition Hacks 2023, a 36-hour hackathon,** to help combat this growing disaster. 🌍🔥

## What It Does & How We Built It

Our app uses **feedparser** to scrape news headlines, selects those related to wildfires, and displays them on the homepage. The wildfire prediction feature uses an algorithm with real-time data from the **WeatherAPI** to calculate fire risk worldwide.

We built the app using **Django** as the back-end framework, with **Python** handling API requests and web scraping. The front-end was developed using **HTML/CSS** with **Bootstrap** for styling.
