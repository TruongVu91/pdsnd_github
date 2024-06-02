import time

import pandas as pd

import numpy as np

 

CITY_DATA = { 'chicago': 'chicago.csv',

              'new york': 'new_york_city.csv',

              'washington': 'washington.csv' }

 

cities = ['chicago', 'new york', 'washington']

 

months = ['january', 'february', 'march', 'april', 'may', 'june', 'all']

 

days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'all']

 

def get_filters():

    """

    Asks user to specify a city, month, and day to analyze.

 

    Returns:

        (str) city - name of the city to analyze

        (str) month - name of the month to filter by, or "all" to apply no month filter

        (str) day - name of the day of week to filter by, or "all" to apply no day filter

    """

    print('Hello! Let\'s explore some US bikeshare data!')

    #get user input for city (chicago, new york city, washington)

    while True:

        print("Please enter your city: ")

        print("\n Chicago, New York,or Washington\n")

        city =input().lower()

        if city in cities:

            break

        else:

            print('Please enter one of the three cities listed.')

 

    #get user input for month (all, january, february, ... , june)

    #get user input for day of week (all, monday, tuesday, ... sunday)

    while True:

        print("Enter the filtering you want: ")

        print("\n none, month, day\n")

        filter = input().lower()

        if filter == 'month':

            print("Enter the month you want filter on or enter all to see view all month data: ")

            print("Valid month input: All, January, February, March, April, May, June\n ")

            month = input().lower()

            day = 'all'

            if month in months:

                break

            else:

                print('Please enter a valid input month.')

        elif filter == 'day':

            print("Enter the day you want filter on or enter all to see view all day data: ")

            print("Valid day input:  All, Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday\n")

            day = input().lower()

            month = 'all'

            if day in days:

                break

            else:

                print('Please enter a valid input day')

        elif filter == 'none':

            month = 'all'

            day = 'all'

            break

 

    print('-'*100)

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

 

    df['month'] = df['Start Time'].dt.month

    df['day_of_week'] = df['Start Time'].dt.weekday_name

 

    if month != 'all':

        months = ['january', 'february', 'march', 'april', 'may', 'june']

        month = months.index(month) + 1

 

        df = df[df['month'] == month]

 

    if day != 'all':

        df = df[df['day_of_week'] == day.title()]

    return df

 

 

def time_stats(df):

    """Displays statistics on the most frequent times of travel."""

 

    print('\nCalculating The Most Frequent Times of Travel...\n')

    start_time = time.time()

 

    # display the most common month

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    df['month'] = df['Start Time'].dt.month

 

    common_month = df['month'].mode()[0]

 

    if common_month == 1:

        print("Most common month is January.")

    elif common_month == 2:

        print("Most common month is February.")

    elif common_month == 3:

        print("Most common month is March.")

    elif common_month == 4:

        print("Most common month is April.")

    elif common_month == 5:

        print("Most common month is May.")

    elif common_month == 6:

        print("Most common month is June.")

 

    #display the most common day of week

    common_day = df['day_of_week'].mode()[0]

    print('Most common day of week is ', common_day)

 

    #display the most common start hour

    df['hour'] = df['Start Time'].dt.hour

    common_hour = df['hour'].mode()[0]

    if common_hour < 12:

        print('Most common start hour is ', common_hour, ' AM')

    elif common_hour >= 12:

        if common_hour > 12:

            common_hour -= 12

        print('Most common start hour is ', common_hour, ' PM')

 

 

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*100)

 

 

def station_stats(df):

    """Displays statistics on the most popular stations and trip."""

 

    print('\nCalculating The Most Popular Stations and Trip...\n')

    start_time = time.time()

 

    #display most commonly used start station

    commmon_start_station = df['Start Station'].mode()[0]

    print("Most commonly used start station is ", commmon_start_station)

 

    #display most commonly used end station

    common_end_station = df['End Station'].mode()[0]

    print("\nMost commonly used end station is ", common_end_station)

 

    #display most frequent combination of start station and end station trip

    line_station = df['Start Station'] + " to " +  df['End Station']

    common_line_station = line_station.mode()[0]

    print("\nMost common trip from start to end: {}".format(common_line_station))

 

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*100)

 

 

def trip_duration_stats(df):

    """Displays statistics on the total and average trip duration."""

 

    print('\nCalculating Trip Duration...\n')

    start_time = time.time()

 

    #display total travel time

    total_duration = df['Trip Duration'].sum()

    minute, second = divmod(total_duration, 60)

    hour, minute = divmod(minute, 60)

    print("The total travel time is {0} hours, {1} minutes, and {2} seconds.".format(hour, minute, second))

 

    #display mean travel time

    average_duration = round(df['Trip Duration'].mean())

    minute, second = divmod(average_duration, 60)

    if minute> 60:

        hour, minute = divmod(minute, 60)

        print('The average travel time is {0} hours, {1} minutes, and {2} seconds.'.format(hour, minute, second))

    else:

        print('The average travel duration is {0} minutes and {1} seconds.'.format(minute, second))

 

 

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*100)

 

 

def user_stats(df):

    """Displays statistics on bikeshare users."""

 

    print('\nCalculating User Stats...\n')

    start_time = time.time()

 

    #Display counts of user types

    user_types = df['User Type'].value_counts()

    print("Counts of user types: ")

    print(user_types)

 

    #Display counts of gender

    try:

        gender = df['Gender'].value_counts()

        print('\nCounts of gender:')

        print(gender)

    except:

        print("There is no Gender column.")

 

    #Display earliest, most recent, and most common year of birth

    try:

        earliest_birth_year = df['Birth Year'].min()

        recent_birth_year = df['Birth Year'].max()

        common_birth_year = df['Birth Year'].mode()

        print('\nEarliest birth year: ', int(earliest_birth_year))

        print('\nRecent birth year: ', int(recent_birth_year))

        print('\nMost common birth year: ', int(common_birth_year))

    except:

        print("There is no birth year.")

 

 

    print("\nThis took %s seconds." % (time.time() - start_time))

    print('-'*100)

 

def display_raw_data(df):
    # display raw data function.
    # Ask user if they want to see individual trip data.

    start_data = 0

    end_data = 5

    df_length = len(df.index)

   

    while start_data < df_length:

        print("\nWould you like to see individual trip data? Enter 'yes' or 'no'.\n")

        raw_data = input().lower()

        if raw_data == 'yes':

           

            print("\nDisplaying only 5 rows of data.\n")

            if end_data > df_length:

                end_data = df_length

            print(df.iloc[start_data:end_data])

            start_data += 5

            end_data += 5

        else:

            break

 

 

def main():

    while True:

        city, month, day = get_filters()

        df = load_data(city, month, day)

 

        time_stats(df)

        station_stats(df)

        trip_duration_stats(df)

        user_stats(df)

        display_raw_data(df)

 

        restart = input('\nWould you like to restart? Enter yes or no.\n')

        if restart.lower() != 'yes':

            break

 

 

if _name_ == "_main_":

    main()