import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

MONTH_DATA = {'january':1,
              'february':2,
              'march':3,
              'april':4,
              'may':5,
              'june':6}

DAY_DATA = {'monday':0,
             'tuesday':1,
             'wednesday':2,
             'thursday':3,
             'friday':4,
             'saturday':5,
             'sunday':6}

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while 1:
        print ('Which city would you like to see data for?  Please enter the full city name. ')
        city = input('Chicago, New york city, Washington? ').lower()
        print()
        if city not in CITY_DATA:
            print('Please enter a valid city.')
            continue
        city = CITY_DATA[city]
        break

    # TO DO: get user input for month (all, january, february, ... , june)
    while 2:
        sort_month = input('Would you like to sort data by month? Yes/No: ').lower()
        if sort_month=='yes':
            sort_month=True
        elif sort_month=='no' :
            sort_month=False
        else:
            print('Please enter a valid choice')
            continue
        break

    while 3:
        if sort_month:
            print('Which month would you like to sort by?')
            month = input('January, February, March, April, May, June ').lower()
            print()
            if month not in MONTH_DATA:
                print('Please input a valid month')
                continue
            month = MONTH_DATA[month]
        else:
            month = 'all'
        break

    while 4:
        sort_day = input('Would you like to sort data by day? Yes/No: ').lower()
        if sort_day=='yes':
            sort_day=True
        elif sort_day=='no' :
            sort_day=False
        else:
            print('Please enter a valid choice')
            continue
        break

    while 5:
        if sort_day:
            print('Which day would you like to sort by?')
            day = input('Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday ').lower()
            print()
            if day not in DAY_DATA:
                print('Please input a valid day')
                continue
            day = DAY_DATA[day]
        else:
            day = 'all'
        break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)


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
    df = pd.read_csv(city)
    df['day_of_week'] = pd.to_datetime(df['Start Time']).dt.dayofweek
    df['month'] = pd.to_datetime(df['Start Time']).dt.month
    if day != 'all':
        df = df[df['day_of_week'] == day]
    if month != 'all':
        df = df[df['month'] == month]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    for num in MONTH_DATA:
        if MONTH_DATA[num]==most_common_month:
            most_common_month = num.title()
    print('The most common month for traveling is {}'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    for num in DAY_DATA:
        if DAY_DATA[num]==most_common_day:
            most_common_day = num.title()
    print('The most common day for traveling is {}'.format(most_common_day))

    # TO DO: display the most common start hour
    df['hour']=pd.to_datetime(df['Start Time']).dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common hour for traveling is {}'.format(most_common_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print()
    print('The most commonly used start station was {}'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print()
    print('The most commonly used end station was {}'.format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    print()
    most_common_combo = df['Start Station'] + ' to ' + df['End Station']
    print('The most commonly used combination of Start and End stations is {}'.format(most_common_combo.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()
    trip_dur = pd.to_datetime(df['End Time']) - pd.to_datetime(df['Start Time'])

    # TO DO: display total travel time
    print()
    travel_sum = df['Trip Duration'].sum()
    sum_seconds = travel_sum%60
    sum_minutes = travel_sum//60%60
    sum_hours = travel_sum//3600%60
    sum_days = travel_sum//24//3600
    print('Travelers rode for a total of {} days, {} hours, {} minutes and {} seconds.'.format(sum_days, sum_hours, sum_minutes, sum_seconds))

    # TO DO: display mean travel time
    print()
    travel_mean = df['Trip Duration'].mean()
    mean_seconds = travel_mean%60
    mean_minutes = travel_mean//60%60
    mean_hours = travel_mean//3600%60
    mean_days = travel_mean//24//3600
    print('Travelers rode for an average of {} days, {} hours, {} minutes and {} seconds.'.format(mean_days, mean_hours, mean_minutes, mean_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print()
    types_of_users = df.groupby('User Type',as_index=False).count()
    print('The number of types of users are: {}'.format(len(types_of_users)))
    for i in range(len(types_of_users)):
        print('{}s - {}.'.format(types_of_users['User Type'][i], types_of_users['Start Time'][i]))

    # TO DO: Display counts of gender
    print()
    if 'Gender' not in df:
        print("Ah man!  There's not any gender information for this city.")
    else:
        gender_of_users = df.groupby('Gender', as_index=False).count()
        print('The number of genders mentioned are: {}'.format(len(gender_of_users)))
        for i in range(len(gender_of_users)):
            print('{}s - {} '.format(gender_of_users['Gender'][i], gender_of_users['Start Time'][i]))
        print("Gender data for {} users is not available'".format(len(df)-gender_of_users['Start Time'][0]-gender_of_users['Start Time'][1]))

    # TO DO: Display earliest, most recent, and most common year of birth
    print()
    if 'Birth Year' not in df:
        print('No birth year data is available for this city.')
    else:
        birth=df.groupby('Birth Year', as_index=False).count()
        print('The oldest year of birth was: {}'.format(int(birth['Birth Year'].min())))
        print('The most recent year of birth was: {}'.format(int(birth['Birth Year'].max())))
        print('The most common year of birth was: {}'.format(int(birth.iloc[birth['Start Time'].idxmax()]['Birth Year'])))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        start0=0
        end5=5
        while True:
            raw_data = input('Do you want to see raw data?  Yes/No ').lower()
            if raw_data == 'yes':
                print(df.iloc[start0:end5])
                start0=start0+5
                end5=end5+5
            else:
                break
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
