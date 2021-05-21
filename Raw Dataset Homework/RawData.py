import numpy as np
import pandas as pd
import pprint
import itertools

description = ('Country', ['2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ', '2019 '])

raw_data = [
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('AS', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 '])
]

"""{'AT': [{'year': '2019','coverage': 84}, {'year': '2018','coverage': 67},
get_year_data(dataset, "2019")"""
# description , raw_data
dataset2 = dict(raw_data)
dataset1 = ['2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ', '2019 ']

keys = dataset1
value = [raw_data]

year_key_u = { key : value[:2:2] for key in keys }
# you can also use { key : value[:] for key in keys }
pprint.pprint(year_key_u)


def get_year_data():
    list_of_lists = list(itertools.chain(*raw_data))
    return list_of_lists
    # print(get_year_data()[1::2])


data = np.array(get_year_data()[1::2])
dataFrame = pd.DataFrame(data, columns=['2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ', '2019'])
print(np.array)

json_records = dataFrame.to_json(orient='records')
print(json_records, "\n")

