# -*- coding: utf-8 -*-
"""
Created on Sun Aug 26 17:00:38 2018

@author: Manikandan Gopalakrishnan
"""
import sys
import os
import pandas as pd

CITY_DATA = {'chicago':'chicago.csv',
             'new york city':'new_york_city.csv',
             'washington':'washington.csv'}

def get_user_input():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter
        (str) day - name of the day of week to filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
  
    #get user input for city (chicago, new york city, washington)
    city = input('Would you like to see data for Chicago, New York, or Washington?').lower()
    
    #get user input for month (all, january, february, ... , june)
    month = input('Which month? January, February, March, April, May, or June?').lower()
    
    #get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day? Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday?').lower()
    
    return city, month, day

def display_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter
        (str) day - name of the day of week to filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    try:
        df = pd.read_csv(CITY_DATA[city])

        df['Start Time'] = pd.to_datetime(df['Start Time'])
    
        df['month'] = df['Start Time'].dt.month
    
        df['day_of_week'] = df['Start Time'].dt.weekday_name
    
        if month != 'all':
            months = ['january', 'february', 'march', 'april', 'may', 'june']
            month = months.index(month)+1
    
        df = df[df['month'] == month]
    
        if day != all:
            df = df[df['day_of_week'] == day.title()]
            
        return df

    except:
        print('\n Please enter the correct city, month, and day name! \n')
            
def popular_times_of_travel(df, month):
    """
    Display Popular times of travel.
      Args:
        (DataFrame) df - name of the DataFrame based on user input.
    """    
    print('\n Calculating statistics...\n')
        
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['hour'] = df['Start Time'].dt.hour
    
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    #display the most common month
    print('What is the most popular month for traveling?')
    print(month)
    
    #display the most common day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('What is the most popular day for traveling?')
    print(popular_day_of_week)
           
    #display the most common start hour
    popular_hour = df['hour'].mode()[0]
    print('What is the most popular hour of the day to start your travels?')
    print(popular_hour)
         
def popular_stations_trip(df):
    """
    Display Popular stations and trips of travel.
      Args:
        (DataFrame) df - name of the DataFrame based on user input.
    """
    print('\n Calculating statistics...\n')    
    #display the most common start station
    popular_start_station = df['Start Station'].mode()[0]
    print('What was the most popular start station?')
    print(popular_start_station)
    
    #display the most common end station
    popular_end_station = df['End Station'].mode()[0]
    print('What was the most popular end station?')
    print(popular_end_station)
       
    #display the most common trip from start to end station
    trip_start_end_value = df['Start Station']+"_"+df['End Station']
    popular_trip_start_end = trip_start_end_value.mode()[0]
    print('What was the most popular trip from start to end station?')
    print(popular_trip_start_end)
     

def trip_duration(df):
    """
    Display trip duration.
      Args:
        (DataFrame) df - name of the DataFrame based on user input.
    """
    print('\n Calculating statistics...\n')
    drip_duration = df['Trip Duration']
    
    #display the Total travel time
    print('What was the total travel time in seconds?')
    print(drip_duration.sum())
    
    #display the Average travel time
    print('What was the average time spend on each trip in seconds?')
    print(drip_duration.mean())
      
def info_user(df, city):
    """
    Display user info.
      Args:
        (DataFrame) df - name of the DataFrame based on user input.
    """
    print('\n Calculating statistics. . .\n')  
    #display the count of each user type
    user_types_count = df['User Type'].value_counts()
    print('What is the breakdown of users?')
    print(user_types_count)
    
    if city != 'washington':
        #display the count of each gender
        gender_count = df['Gender'].value_counts()
        print('What is the breakdown of gender?')
        print(gender_count)
    else:
        print('\n No gender data to share.\n')
        
    if city != 'washington':
        #display the earliest year of birth
        oldest_year = df['Birth Year'].min()
        print('What is the oldest year of birth?')
        print(oldest_year)
    
        #display the recent year of birth
        youngest_year = df['Birth Year'].max()
        print('What is the youngest year of birth?')
        print(youngest_year)
    
        #display the most common year of birth
        popular_year = df['Birth Year'].mode()[0]
        print('What is the most popular year of birth?')
        print(popular_year)
    else:
        print('No birth year data to share.')
        print('-'*40)
 
def main(df_user_input,month,city):
    popular_times_of_travel(df_user_input, month)
    popular_stations_trip(df_user_input)
    trip_duration(df_user_input)
    info_user(df_user_input, city)
    print('-'*40)
            
def restart_program():
    """
    restart the oython program
    """
    python = sys.executable
    os.execl(python, python, *sys.argv)
    
if __name__ == "__main__":
    city_input, month_input, day_input = get_user_input()
    df_user_input = display_data(city_input, month_input, day_input)
    
    if df_user_input is None:
        print('\n Exception Data Frame is None \n')
        print('-'*40)
    else:    
        main(df_user_input,month_input,city_input)
        
        raw_data_input = input('Do you want to see raw data? Enter yes or no.').lower()
        index_start = 0
        index_end = 5
        while raw_data_input == 'yes':
            print(df_user_input.iloc[index_start:index_end])
            print('\n')
            raw_data_input = input('Do you want to see 5 more lines of data? Enter yes or no.').lower()
            index_start=index_end
            index_end += 5
        
        print('\n')
        restart_input = input('Would you like to restart? Enter yes or no.').lower()
        if restart_input == 'yes':
            restart_program()
            print('\n')
        elif restart_input != 'no':
            print('Please enter Yes or No!')
