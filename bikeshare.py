import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def chooseCity():
    # Cities Available
    Cities = ['chicago', 'washington', 'new york']
    # Choose City
    city = input("Would you like to see data for Chicago, Washington, or New York?\n")
    # Check if this is a valid city
    while city.lower() not in Cities:
        print("You have chosen an unavailable City, please choose again.")
        city = input("Please choose one of these three cities: Chicago, Washington, or New York")
    # City Confirmation
    confirm = input(
        f"You have chosen to see data for {city}, please type 'Confirm' to confirm your choice or 'Reject' to choose again.")
    if confirm.lower() == 'reject':
        chooseCity()
    return city


def chooseMonth():
    # Months available
    Months = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
              'november', 'december']
    print("You have chosen to filter by Month, if its not the case, please restart the program.")
    # CHOOSING WHICH MONTH
    Month = input("Which month would you like to choose (type the name of the month in full)")
    while Month.lower() not in Months:
        print("You have chosen an invalid Month, please choose again.")
        Month = input("Which month would you like to choose (type the name of the month in full)")

def chooseDay():
    # Days Available
    Days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    print("You have chosen to filter by day, if its not the case, please restart the program.")
    # CHOOSING WHICH MONTH
    Day = input("Which day would you like to choose (type the name of the month in full)")
    while Day.lower() not in Days:
        print("You have chosen an invalid Day, please choose again.")
        Day = input("Which month would you like to choose (type the name of the month in full)")
def get_filters():
    """
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Choose What to filter by
    choice = input("Would you like to filter the data by month, day, both or none?")
    # CHOOSING THE FILTER TYPE
    # Month
    if choice.lower() == "month":
        chooseMonth()
    elif choice.lower() == "day":
       chooseDay()
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs

    # TO DO: get user input for month (all, january, february, ... , june)

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month

    # TO DO: display the most common day of week

    # TO DO: display the most common start hour

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station

    # TO DO: display most commonly used end station

    # TO DO: display most frequent combination of start station and end station trip

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time

    # TO DO: display mean travel time

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types

    # TO DO: Display counts of gender

    # TO DO: Display earliest, most recent, and most common year of birth

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


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
getfilter()