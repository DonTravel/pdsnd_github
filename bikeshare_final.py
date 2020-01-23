import time
import pandas as pd
import numpy as np


# define global variables
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

month_DATA = {'january' : 1, 'february' : 2, 'march' : 3, 'april' : 4, 'may' : 5, 'june' : 6, 'all' : 0 }
day_DATA = {'monday' : 0, 'tuesday' : 1, 'wednesday' : 2, 'thursday' : 3, 'friday' : 4, 'saturday' : 5, 'sunday' : 6, 'all' : 7 }


# functions
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    # input: city   
    print('\nHello! Let\'s explore some US bikeshare data!')
    print('\n\nWould you like to see data for "Chicago", "New York City" or "Washington?"')
    print('Please type in full name as displayed.')
        
    city_input = input().lower()
    while city_input not in CITY_DATA.keys():
        print('Invalid input, please type in Chicago, New York or Washington! Please enter City Name')
        city_input = input().lower()
        
    city = city_input
    print('-'*40)
    print('User-input: ', city.title())
    print('-'*40)
    
    # input: month
    print('\nWould you like to filter the data by month?')
    print('Please type in "January", "February", "March", "April", "May", "June" or "All" for no filter.')
    month_input = input().lower()
    
    
    while month_input not in month_DATA:
        print('Invalid input for month, please fill in correct input!')
        month_input = input().lower()
        
    month = month_input
    print('-'*40)
    print('User-input: ', month.title())
    print('-'*40)

    
    
    # input day
    print('\nWould you like to filter the data by day?')
    print('Please type in "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday" or "All" for no filter.')
    day_input = input().lower()
        
    while day_input not in day_DATA:
        print('Invalid input for day, please fill in correct input!')
        day_input = input().lower()
        
    day = day_input
    print('-'*40)
    print('User-input: ', day.title())
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
        df - pandas DataFrame containing city data filtered by month and day
    """
        
    # check: show variables
    cityname = CITY_DATA[city]
    # to check correct variable - uncomment next line
    # print('open file:', cityname)
    monthnumber = month_DATA[month]
    # to check correct variable - uncomment next line
    # print('show monthnumber:', monthnumber)
    daynumber = day_DATA[day]
    # to check correct variable - uncomment next line
    # print('show daynumer:', daynumber)
    
    
    # load data into dataframe
    df = pd.read_csv(cityname)
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
   
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month 
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    
    
    # filter by month if applicable
    if monthnumber != 0:
       
    # filter by month to create the new dataframe
        df = df[df['month'] == monthnumber]
    
    
    
    # filter by day of week if applicable
    if daynumber != 7:
    
    # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == daynumber]
    
    # return dataframe df
                
    return df


# time statistics
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('-'*40)
    
    print('\nCalculating The Most Frequent Times of Travel...')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('\nThe most common month for travel:', [key for key in month_DATA.keys()][common_month-1].title())
        
    
    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('\nThe most common day for travel:', [key for key in day_DATA.keys()][common_day].title())

    # TO DO: display the most common start hour
    common_hour = df['Start Time'].dt.hour.mode()[0]
    print('\nThe most common start hour:', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


# station statistics    
def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('\nThe most common start station:', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('\nThe most common end station:', common_end_station)

    # display most frequent combination of start station and end station trip
    common_combi_station = (df['Start Station'] + ' / ' + df['End Station']).mode()[0]
    print('\nThe most frequent trip:', common_combi_station)
    
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
    
# trip duration statistics    
def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...')
    start_time = time.time()
        
    # display total travel time
    sum_travel_time = df['Trip Duration'].sum()
    print('\nThe total time of travel:  {} sec.' .format(sum_travel_time))
    
    # display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('\nThe mean time of travel:  {} sec.' .format(mean_travel_time))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The counts for the different user types are:\n')
    print(user_type)
    
        
    # TO DO: Display counts of gender
    try:
        user_gender = df['Gender'].value_counts()
        print('\nThe counts for the different user genders are:\n')
        print(user_gender)
    except:
        print('\nData for gender not available!')
        
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_user_byear = int(df['Birth Year'].min())
        print('\n\nThe earliest user birthday is: ', earliest_user_byear)
    
        recent_user_byear = int(df['Birth Year'].max())
        print('\nThe most recent user birthdayis: ', recent_user_byear)
    
        common_user_byear = int(df['Birth Year'].mode()[0])
        print('\nThe common user birthday is: ',common_user_byear)
    except:
        print('\nData for birth year not available!')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


    # TO DO: Display individual data
    
    individual = input('\nWould you like to view individual trip data? (5 rows) \nEnter yes or any key for no.\n')
    if individual.lower() == 'yes':
        i = 0
        print(df.iloc[i:i+5])
        
        while individual.lower() == 'yes':
                 
            individual = input('\nWould you like to view MORE individual trip data? (next 5 rows) \nEnter yes or any key for no.\n')
            if individual.lower() == 'yes':
                i = i+5
                print(df.iloc[i:i+5])
            else:
                print('No further individual data requested!')
          
    else:
        print('No individual data requested!')
    
    
    
    
    

# main function

def main():

           
    while True:
        # call user-input function to get variables
        city, month, day = get_filters()
        # to check correct variable - uncomment next lines
        # city = 'chicago'
        # month = 'all'
        # day = 'all'
        
        
        
        # call load-data function to create dataframe
        df = load_data(city, month, day)
        # to check correct variable - uncomment next lines
        # print(df.head())

        print('\n\nPlease wait, statistics are calculated ..\n\n')
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\n\n\nWould you like to restart? Enter yes or any key for no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()