import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def validate_city_input(city):
    valid_cities = ['chicago', 'new york city', 'washington']
    return city.lower() in valid_cities

def validate_month_input(month):
    valid_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    return month.lower() in valid_months

def validate_day_input(day):
    valid_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    return day.lower() in valid_days

def get_filters():
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    city = input("Enter the name of the city (Chicago, New York City, Washington): ").lower()
    while not validate_city_input(city):
        print("Invalid input. Please choose a valid city.")
        city = input("Enter the name of the city (Chicago, New York City, Washington): ").lower()

    month = input("Enter the name of the month (all, January, February, ..., June): ").lower()
    while not validate_month_input(month):
        print("Invalid input. Please choose a valid month.")
        month = input("Enter the name of the month (all, January, February, ..., June): ").lower()

    day = input("Enter the name of the day of the week (all, Monday, Tuesday, ..., Sunday): ").lower()
    while not validate_day_input(day):
        print("Invalid input. Please choose a valid day.")
        day = input("Enter the name of the day of the week (all, Monday, Tuesday, ..., Sunday): ").lower()

    print('-'*40)
    return city, month, day

def validate_and_load_city(city):
    valid_cities = list(CITY_DATA.keys())
    city = city.lower()
    if city not in valid_cities:
        raise ValueError("Invalid city. Please choose a valid city.")
    return pd.read_csv(CITY_DATA[city])

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of the week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = validate_and_load_city(city)

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.strftime('%A')
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month_num = validate_month_input(month)
        df = df[df['month'] == month_num]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Calculate and display the most common month
    common_month = df['month'].mode()[0]
    print("The most common month for bike trips is:", common_month)

    # Calculate and display the most common day of the week
    common_day_of_week = df['day_of_week'].mode()[0]
    print("The most common day of the week for bike trips is:", common_day_of_week)

    # Calculate and display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print("The most common start hour for bike trips is:", common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def station_stats(df):
    """Displays statistics on the most popular stations and trips."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Calculate and display the most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print("The most commonly used start station is:", common_start_station)

    # Calculate and display the most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print("The most commonly used end station is:", common_end_station)

    # Calculate and display the most frequent combination of start and end stations
    common_trip = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("The most frequent combination of start and end stations for trips is:")
    print("Start Station:", common_trip[0])
    print("End Station:", common_trip[1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Calculate and display the total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time for all trips: {:.2f} hours".format(total_travel_time / 3600))

    # Calculate and display the mean (average) travel time
    mean_travel_time = df['Trip Duration'].mean()
    print("Average travel time for all trips: {:.2f} minutes".format(mean_travel_time / 60))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Calculate and display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of User Types:")
    print(user_types)

    # Check if 'Gender' column exists in the DataFrame
    if 'Gender' in df:
        # Calculate and display counts of gender
        gender_counts = df['Gender'].value_counts()
        print("\nCounts of Gender:")
        print(gender_counts)
    else:
        print("\nGender information is not available in this dataset.")

    # Check if 'Birth Year' column exists in the DataFrame
    if 'Birth Year' in df:
        # Calculate and display the earliest, most recent, and most common year of birth
        earliest_birth_year = df['Birth Year'].min()
        most_recent_birth_year = df['Birth Year'].max()
        common_birth_year = df['Birth Year'].mode()[0]
        print("\nYear of Birth Statistics:")
        print("Earliest Birth Year:", int(earliest_birth_year))
        print("Most Recent Birth Year:", int(most_recent_birth_year))
        print("Most Common Birth Year:", int(common_birth_year))
    else:
        print("\nBirth year information is not available in this dataset.")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
