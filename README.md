### Date created
November 12, 2023

### Project Title
Bike Share Data Analysis

### Description
In this project, Python is used to explore data related to bike share systems for three major cities in the United States—Chicago, New York City, and Washington. The code imports data, answers interesting questions about it by computing descriptive statistics, and creates an interactive experience in the terminal to present these statistics.

### Files used
- bikeshare.py
- chicago.csv
- new_york_city.csv
- washington.csv

### Credits
- [Data Wrangling](https://en.wikipedia.org/wiki/Data_wrangling)
- [GitHub Docs](https://docs.github.com/en/get-started/writing-on-github)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials/setting-up-a-repository/git-init)
- [Divvy Data](https://divvybikes.com/system-data)
- [pandas.to_datetime](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.to_datetime.html)
- [API reference](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)
- [NumPy Documentation](https://numpy.org/doc/stable/)
## Project Overview
**Overview:**
Over the past decade, bicycle-sharing systems have been growing in number and popularity in cities across the world. This project uses data provided by Motivate, a bike share system provider, to uncover bike share usage patterns in Chicago, New York City, and Washington, DC.

**Datasets:**
Randomly selected data for the first six months of 2017 are provided for all three cities. The data includes start time, end time, trip duration, start station, end station, and user type. Additional gender and birth year information is available for Chicago and New York City.

**Statistics Computed:**
The project computes various descriptive statistics, including popular times of travel, popular stations and trips, trip duration, and user information.

**Real-World Relevance:**
Understanding the dynamics of bike share systems is crucial for urban planning, transportation optimization, and sustainable city development. By delving into this dataset, you gain practical insights that can inform decisions related to the allocation of resources, improvement of infrastructure, and enhancement of the overall urban mobility experience.

**Why Bike Share Data Matters:**
Bicycle-sharing systems provide an eco-friendly and convenient mode of transportation. Analyzing bike share data not only sheds light on usage patterns but also contributes to the ongoing discourse on promoting sustainable transportation solutions. The skills developed in this project are directly applicable to real-world scenarios where data-driven decision-making is a valuable asset.

Explore the patterns and trends in bike share data to unlock the potential for a more sustainable and efficient urban transportation landscape.

### Instructions for Developers

1. **Clone the Repository:**
   - Clone or download this repository to your local machine.

2. **Install Dependencies:**
   - Make sure you have Python installed (download from [python.org](https://www.python.org/downloads/)).
   - Install necessary dependencies using the following command:
     ```bash
     pip install pandas numpy
     ```

3. **Navigate to the Script:**
   - Open a terminal or command prompt.
   - Navigate to the directory containing `bikeshare.py`.

4. **Run the Script:**
   - Execute the script by running:
     ```bash
     python bikeshare.py
     ```

5. **Input City and Filters:**
   - Follow the prompts to enter the city (Chicago, New York City, Washington), month, and day for analysis.
   - You can choose "all" for month and day to analyze all data.

6. **Explore Results:**
   - The script will display statistics on times of travel, popular stations, trip durations, and user information.
   - Optionally, view raw data in 5-row increments.

7. **Restart or Exit:**
   - Decide whether to restart the analysis or exit the script.

### Additional Notes
- The script filters data based on user input for city, month, and day.
- Explore different combinations to derive insights from the Bikeshare data.
- Feel free to customize or extend the script for your specific requirements.