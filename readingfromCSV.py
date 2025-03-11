# Using the files to create dataframe in pandas using read_csv function
import pandas as pd

movies=pd.read_csv('sample-data/movies.csv')
# print(movies)
print(movies.shape)  # to get rows and column

print(movies.dtypes)
print(movies.index)
print(movies.columns)
# print(movies.values)

# functions for dataframes
# head, tail, sample, info( very important), describe, isnull, duplicated

# print(movies.head(6))
#
# print(movies.tail(2))
print("------------------------------------------------------------------------------------------")
print(movies.sample(5)) # random 5 matches

print(movies.info()) # missing values in a column. data type summary  ram memory usage

print(movies.describe())

print(movies.isnull())
print(movies.isnull().sum())
print("------------------------------------------------------------------------------------------")
print(movies.duplicated().sum())


# output


# (1629, 18)
# title_x              object
# imdb_id              object
# poster_path          object
# wiki_link            object
# title_y              object
# original_title       object
# is_adult              int64
# year_of_release       int64
# runtime              object
# genres               object
# imdb_rating         float64
# imdb_votes            int64
# story                object
# summary              object
# tagline              object
# actors               object
# wins_nominations     object
# release_date         object
# dtype: object
# RangeIndex(start=0, stop=1629, step=1)
# Index(['title_x', 'imdb_id', 'poster_path', 'wiki_link', 'title_y',
#        'original_title', 'is_adult', 'year_of_release', 'runtime', 'genres',
#        'imdb_rating', 'imdb_votes', 'story', 'summary', 'tagline', 'actors',
#        'wins_nominations', 'release_date'],
#       dtype='object')
# ------------------------------------------------------------------------------------------
#                        title_x  ...               release_date
# 881   Life Express (2010 film)  ...  17 September 2010 (India)
# 555                  Titoo MBA  ...   21 November 2014 (India)
# 349             Moh Maya Money  ...   25 November 2016 (India)
# 958               Acid Factory  ...     9 October 2009 (India)
# 1079  Eklavya: The Royal Guard  ...   16 February 2007 (India)

# [5 rows x 18 columns]
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 1629 entries, 0 to 1628
# Data columns (total 18 columns):
#  #   Column            Non-Null Count  Dtype  
# ---  ------            --------------  -----  
#  0   title_x           1629 non-null   object 
#  1   imdb_id           1629 non-null   object 
#  2   poster_path       1526 non-null   object 
#  3   wiki_link         1629 non-null   object 
#  4   title_y           1629 non-null   object 
#  5   original_title    1629 non-null   object 
#  6   is_adult          1629 non-null   int64  
#  7   year_of_release   1629 non-null   int64  
#  8   runtime           1629 non-null   object 
#  9   genres            1629 non-null   object 
#  10  imdb_rating       1629 non-null   float64
#  11  imdb_votes        1629 non-null   int64  
#  12  story             1609 non-null   object 
#  13  summary           1629 non-null   object 
#  14  tagline           557 non-null    object 
#  15  actors            1624 non-null   object 
#  16  wins_nominations  707 non-null    object 
#  17  release_date      1522 non-null   object 
# dtypes: float64(1), int64(3), object(14)
# memory usage: 229.2+ KB
# None
#        is_adult  year_of_release  imdb_rating     imdb_votes
# count    1629.0      1629.000000  1629.000000    1629.000000
# mean        0.0      2010.263966     5.557459    5384.263352
# std         0.0         5.381542     1.567609   14552.103231
# min         0.0      2001.000000     0.000000       0.000000
# 25%         0.0      2005.000000     4.400000     233.000000
# 50%         0.0      2011.000000     5.600000    1000.000000
# 75%         0.0      2015.000000     6.800000    4287.000000
# max         0.0      2019.000000     9.400000  310481.000000
#       title_x  imdb_id  poster_path  ...  actors  wins_nominations  release_date
# 0       False    False        False  ...   False             False         False
# 1       False    False         True  ...   False              True         False
# 2       False    False        False  ...   False              True         False
# 3       False    False        False  ...   False              True         False
# 4       False    False         True  ...   False             False         False
# ...       ...      ...          ...  ...     ...               ...           ...
# 1624    False    False        False  ...   False              True         False
# 1625    False    False        False  ...   False              True         False
# 1626    False    False         True  ...   False              True          True
# 1627    False    False        False  ...   False              True         False
# 1628    False    False        False  ...   False              True         False

# [1629 rows x 18 columns]
# title_x                0
# imdb_id                0
# poster_path          103
# wiki_link              0
# title_y                0
# original_title         0
# is_adult               0
# year_of_release        0
# runtime                0
# genres                 0
# imdb_rating            0
# imdb_votes             0
# story                 20
# summary                0
# tagline             1072
# actors                 5
# wins_nominations     922
# release_date         107
# dtype: int64
# ------------------------------------------------------------------------------------------
# 0




