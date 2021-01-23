import time
import pandas as pd
import numpy as np
import os

CITY_DATA = {'chicago': 'chicago.csv',
             'new york': 'new_york_city.csv',
             'washington': 'washington.csv'}


def chooseCity():
    # Cities Available
    Cities = ['chicago', 'washington', 'new york']
    # Choose City
    city = input("Would you like to see data for Chicago, Washington, or New York?\n")
    # Check if this is a valid city
    while city.lower() not in Cities:
        print("You have chosen an unavailable City, please choose again.")
        city = input("Please choose one of these three cities: Chicago, Washington, or New York\n")
    # City Confirmation
    confirm = input(f"You have chosen to see data for {city}, please type 'Confirm' to confirm your choice or 'Reject' to choose again.\n")
    if confirm.lower() == 'reject':
        chooseCity()
    return city
def chooseMonth():
    # Months available
    Months = ['january', 'february', 'march', 'april', 'may', 'june']
    confirm = input("You have chosen to filter by Month, please type 'Confirm' to confirm your choice or 'Reject' to choose again.\n")
    if confirm.lower() == 'reject':
        return None
    elif confirm.lower() == 'confirm':
        # CHOOSING WHICH MONTH
        Month = input("Which month would you like to choose (type the name of the month in full, months can be  January to June)\n")
        while Month.lower() not in Months:
            print("You have chosen an invalid Month, please choose again.")
            Month = input("Which month would you like to choose (type the name of the month in full)")
        return Month
    else:
        print("Please choose a valid option")
        chooseMonth()

def chooseDay():
    # Days Available
    Days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    confirm = input("You have chosen to filter by day, please type 'Confirm' to confirm your choice or 'Reject' to choose again.\n")
    if confirm.lower() == 'reject':
        return None
    elif confirm.lower() == 'confirm':
        # CHOOSING WHICH DAY
        Day = input("Which day would you like to choose (type the name of the day in full)\n")
        while Day.lower() not in Days:
            print("You have chosen an invalid Day, please choose again.")
            Day = input("Which Day would you like to choose (type the name of the day in full)\n")
        return Day
    else:
        print("Please choose a  valid option")
        chooseDay()
def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    #Choose City
    City = chooseCity()
    # Choose What to filter by
    choice = input("Would you like to filter the data by month, day, both or none?\n")
    if choice.lower() == "month":
        Month = chooseMonth()
        Day = "all"
    elif choice.lower() == "day":
       Day = chooseDay()
       Month = "all"
    elif choice.lower()=="both":
        Month = chooseMonth()
        Day = chooseDay()
    elif choice.lower() =="none":
        Month = "all"
        Day = "all"
    else:
        print("Invalid option, the program will now restart!\n")
        get_filters()
    print('-' * 40)
    return City,Month,Day


def load_data(city, month, day):

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    #Rename Start and End station to remove spaces
    df = df.rename(columns={'Start Station': 'start_station', 'End Station': 'end_station', 'Trip Duration': 'trip_duration'})
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('Most common Month:', popular_month)
    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('Most common Day of Week:', popular_day)
    # TO DO: display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('Most common Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    MCSS = df['start_station'].mode()[0]
    print('Most common Start Station:', MCSS)
    # TO DO: display most commonly used end station
    MCES = df['end_station'].mode()[0]
    print('Most common End Station:', MCES)
    # TO DO: display most frequent combination of start station and end station trip
    MCTS=(df['start_station'] + ' --> ' + df['end_station']).mode()[0]
    print('Most common Trip Stations:', MCTS)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    sum = df['trip_duration'].sum()
    print("Total travel time is: ",sum)
    average = df['trip_duration'].mean()
    # TO DO: display mean travel time
    print("Average Trip duration is : ", average)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    # print value counts for each user type
    user_types = df['User Type'].value_counts()
    print(user_types)
    # TO DO: Display counts of gender
    # print value counts for each gender
    genders = df['Gender'].value_counts()
    print(genders)
    # TO DO: Display earliest, most recent, and most common year of birth
    print(df.sort_values(by=['Birth Year']))
    Earliest = df['Birth Year'].iloc[0]
    print("Earliest year of Birth is: ",int(Earliest))
    Recent = df['Birth Year'].iloc[-1]
    print("Most recent year of Birth is: ", int(Recent))
    MCYOB = df['Birth Year'].mode()[0]
    print("Most common year of Birth is: ",int(MCYOB))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city,month,day)
        #df = load_data('chicago', 'february', 'sunday')

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()