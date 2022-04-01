"""
This file contains functions used in order to graph our data.


"""
import csv
import matplotlib.pyplot as plt
import numpy as np
from wordcloud import WordCloud, STOPWORDS
from PIL import Image



def basic_graph_data(csv_file,title,x_label, y_label):
    """

    insert data you want plotted here along with title, x label, and y label
    the csv file MUST have same number of values in columns
    csv file MUST also have only 2 columns
    all entries must be in '___' form example below
    instead of dog.csv proper form is 'dog.csv'

    Args:
        csv_file: data must have only 2 columns
        title: input the title of the graph
        x_label: input what you want your x label to be
        y_label: input what you want you y label to be


    Returns: interprets file and graphs data according to user defined
    parameters

    """

    x_axis = []
    y_axis = []
    with open(csv_file, 'r') as csv_file_:
        reader = csv.reader(csv_file_)
        for row in reader:
            x_axis.append(row[0])
            y_axis.append(float(row[1]))
    plt.bar(x_axis, y_axis)
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.show()




def draw_word(text_file, png_file):
    """
    designed to take in a text file and a png file to create a word cloud.

    Args: text_file:
        png_file is where you want the

    Returns:

    """
    with open(text_file, "r").read() as dataset:
        dataset = dataset.lower()
        create_word_cloud(dataset, png_file)


def create_word_cloud(string,pic_file):
    """
    This function creates the word cloud by taking a png and a word string
    and combining them using functions from importing wordcloud.

    Args:
        string: This is a string that contains the words given to us by the
        Yelp API when scraped for fast food in a specific location.

    Returns:
        no returns, but this function updates/creates a png in
        data_storage with the wordcloud.
    """
    maskarray = np.array(Image.open(pic_file))
    cloud = WordCloud(background_color = "white", \
    max_words = 200, mask = maskarray, stopwords = set(STOPWORDS))
    cloud.generate(string)
    cloud.to_file("visuals/words.png")



def avg_finder(csv_data):
    """
    csv_data must be obtained from the expanded_search function
    csv file MUST have 3 columns the function is specifically
    built to read files with 3 columns

    Args:
        csv_data: data obtained from expanded_search function


    Returns: returns a dictionary called city_dict
    this dictionary will return in the format of
    City: associated with a list of ratings
    example: 'Boston': ['3.0', '3.5', '3.0']
            'Brooklyn': ['3.0', '3.5', '3.0']
    also plots data on a bar graph

    """
    city_dict_ = {}
    with open(csv_data, 'r') as csv_file_:
        reader = csv.reader(csv_file_)
        for row in reader:
            city = row[0]
            if city in city_dict_.keys():
                city_dict_[city].append(row[2])
            else:
                city_dict_[city]=[row[2]]

    for i, value_ in city_dict_.items():
        new_list = []
        for item in value_:
            new_list.append(float(item))
        city_dict_[i] = np.mean(new_list)

    return city_dict_

        #return(ans)
    #return(city_dict) #sanity check to make sure it puts in proper form

city_dict = avg_finder('data_storage/expandeddata.csv')

xlabels = []
ylabels = []

for key, value in city_dict.items():
    xlabels.append(key)
    ylabels.append(value)

plt.bar(xlabels,ylabels)
plt.title('avg rating of cities')
plt.xlabel('cities')
plt.ylabel('avg ratings')
plt.show()
