import itertools
import collections
import pprint

description = ('Country', ['2011 ', '2012 ', '2013 ', '2014 ', '2015 ', '2016 ', '2017 ', '2018 ', '2019 '])

raw_data = [
    ('AT', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 ']),
    ('BA', [': ', ': ', ': ', ': ', ': ', ': ', ': ', '69 ', '72 ']),
    ('AS', ['75 ', '79 ', '81 ', '81 ', '82 ', '85 ', '89 ', '89 ', '90 '])
]
# description , raw_data
dataset = list(raw_data)
dataset2 = dict(dataset)
print(dataset2)

def get_year_data():
    for p_id, p_info in dataset2.items():
        return p_id, p_info


print(get_year_data())

# print(get_year_data(raw_data))
