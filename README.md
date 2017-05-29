# Phishing Detection
![Hack Day Logo](docs/img/hack-day-logo.png) Project at <a href="http://www.ajunews.com/view/20170526135211042">Naver Campus Hack Day 2017</a>
---

## Overview
This is a phishing site detection system that accepts URL as an argument and returns a string value describing whether the website is a phishing site or not.

## Project structure
### `hackday.py`
Contains the main function for the system designed for Hack Day. `hackday.py` communicates with a temporary API designed for Hack Day, and therefore will not work past 2017/06/10.

### `phishing_detection.py`
Contains the main function for the system that removes all dependencies from Hack Day.

## Evaluation method
- Effectiveness and appropriateness of algorithms used to detect phishing sites.
- Accuracy of system
    - True positive
    - False positive
    - True negative
    - False negative

## Language
The code is written in python 2.7. Please check the [requirements](requirements.txt) for dependencies.
