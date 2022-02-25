import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}
MONTH = {'january': 1,
         'february': 2,
         'march': 3,
         'april': 4,
         'may': 5,
         'june': 6}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    month = day = 'all'

    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    false_input = True
    while false_input:
        city = input('Would  you like to see data for Chicago, New York, or Washington?\n').lower()
        if city in ['chicago', 'new york city', 'washington']:
            false_input = False
            break
        print('Invalid Input')

    # get data filters
    false_input = True
    while false_input:
        data_filter = input('Would you like to filter data by month, day, both or not at all? Type "none" for no time filter.\n').lower()
        if data_filter in ['both', 'month', 'day', 'none']:
            false_input = False
            break
        print('Invalid Input')

    # get user input for month (all, january, february, ... , june)
    if data_filter.lower() in ['month', 'both']:
        false_input = True
        while false_input:
            month = input('Which month? January, February, March, April, May, or June\n').lower()
            if month in ['january', 'february', 'march', 'may', 'april', 'june']:
                false_input = False
                break
            print('Invalid Input')

    # get user input for day of week (all, monday, tuesday, ... sunday)
    if data_filter.lower() in ['day', 'both']:
        false_input = True
        while false_input:
            try:
                day = int(input('Which day? Please type your response as an integer (e.g., 1=sunday).\n'))
            except:
                print('Invalid Input')
                continue
            if 1 >= day or day <= 7:
                false_input = False
                break
            print('Invalid Input')

    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek + 1

    if month != 'all':
        df = df[df['Month'] == MONTH[month]]
    if day != 'all':
        df = df[df['day_of_week'] == day]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    print('The most common month is: {}'.format(df['Month'].mode()[0]))

    # display the most common day of week
    print('The most common day of week is: {}'.format(df['day_of_week'].mode()[0]))

    # display the most common start hour
    print('The most common start hour is: {}'.format(df['Start Time'].dt.hour.mode()[0]))

    print("\nThis took %s seconds." % round(time.time() - start_time, 2))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station is: {}'.format(df['Start Station'].mode()[0]))

    # display most commonly used end station
    print('The most commonly used end station is: {}'.format(df['End Station'].mode()[0]))

    # display most frequent combination of start station and end station trip
    print('The most frequent combination of start station and end station trip is: {}'.format((df['Start Station'] + '  -  ' + df['End Station']).mode()[0]))


    print("\nThis took %s seconds." % round(time.time() - start_time, 2))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print('Total travel time is: {} seconds.'.format(round(df['Trip Duration'].sum(), 2)))

    # display mean travel time
    print('Total travel time is: {} seconds.'.format(round(df['Trip Duration'].mean(), 2)))

    print("\nThis took %s seconds." % round(time.time() - start_time, 2))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('The counts of user types are:\n{}'.format(df['User Type'].value_counts().to_frame(name="count")))

    # Display counts of gender
    try:
        print('\nThe counts of gender are:\n{}'.format(df['Gender'].value_counts().to_frame(name="count")))
    except:
        pass
    # Display earliest, most recent, and most common year of birth
    try:
        print('\nThe most common year of birth is: {}'.format(int(df['Birth Year'].mode()[0])))
        print('\nThe earliest year of birth is: {}'.format(int(df['Birth Year'].min())))
        print('\nThe most recent year of birth is: {}'.format(int(df['Birth Year'].max())))
    except:
        pass

    print("\nThis took %s seconds." % round(time.time() - start_time, 2))
    print('-'*40)


def show_data(df):
    keep_showing_data = True
    start_loc = 0
    while keep_showing_data:
        wants_data = input('Do you want to see the first 5 rows of data? (enter yes or no)\n').lower()
        if wants_data == 'no':
            break
        elif wants_data == 'yes':
            print(df.iloc[start_loc:start_loc+5])
            start_loc += 5
        else:
            print('invalid input')



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    city, month, day = get_filters()
    df = load_data(city, month, day)
    show_data(df)
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)