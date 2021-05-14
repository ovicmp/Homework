males_2017 = [('Belgium', 2017, 'M', 21.8), ('Czechia', 2017, 'M', 13.6), ('Denmark', 2017, 'M', 36.5),
              ('Germany', 2017, 'M', 15.4), ('Ireland', 2017, 'M', 45.9), ('Greece', 2017, 'M', 44.1),
              ('Spain', 2017, 'M', 26.7), ('France', 2017, 'M', 14.4), ('Croatia', 2017, 'M', 27.5),
              ('Italy', 2017, 'M', 13.2), ('Cyprus', 2017, 'M', 54.9), ('Latvia', 2017, 'M', 5.1),
              ('Luxembourg', 2017, 'M', 22.1), ('Hungary', 2017, 'M', 5.9), ('Malta', 2017, 'M', 68),
              ('Netherlands', 2017, 'M', 21.3), ('Austria', 2017, 'M', 31.9), ('Poland', 2017, 'M', 0),
              ('Portugal', 2017, 'M', 17.8), ('Slovenia', 2017, 'M', 14.7), ('Slovakia', 2017, 'M', 2.9),
              ('Finland', 2017, 'M', 27.3), ('Sweden', 2017, 'M', 24.8), ('Iceland', 2017, 'M', 32.2),
              ('Norway', 2017, 'M', 37.4), ('Switzerland', 2017, 'M', 29), ('United Kingdom', 2017, 'M', 39),
              ('Montenegro', 2017, 'M', 24.3), ('North Macedonia', 2017, 'M', 10.9), ('Serbia', 2017, 'M', 11.2)]

males_2018 = [('Belgium', 2018, 'M', 22.6), ('Czechia', 2018, 'M', 17.8), ('Denmark', 2018, 'M', 25.3),
              ('Germany', 2018, 'M', 17), ('Ireland', 2018, 'M', 51.5), ('Greece', 2018, 'M', 53.1),
              ('Spain', 2018, 'M', 26.2), ('France', 2018, 'M', 14.8), ('Croatia', 2018, 'M', 24.5),
              ('Italy', 2018, 'M', 18.7), ('Cyprus', 2018, 'M', 51.6), ('Latvia', 2018, 'M', 2.9),
              ('Luxembourg', 2018, 'M', 22.3), ('Hungary', 2018, 'M', 4.8), ('Malta', 2018, 'M', 49.2),
              ('Netherlands', 2018, 'M', 23.3), ('Austria', 2018, 'M', 32.1), ('Poland', 2018, 'M', 16.5),
              ('Portugal', 2018, 'M', 16), ('Slovenia', 2018, 'M', 15.7), ('Slovakia', 2018, 'M', 6),
              ('Finland', 2018, 'M', 21.7), ('Sweden', 2018, 'M', 17.7), ('Iceland', 2018, 'M', 35.5),
              ('Norway', 2018, 'M', 26), ('Switzerland', 2018, 'M', 29.9), ('United Kingdom', 2018, 'M', 36.8),
              ('Montenegro', 2018, 'M', 18.4), ('North Macedonia', 2018, 'M', 12.1), ('Serbia', 2018, 'M', 15)]

females_2017 = [('Belgium', 2017, 'F', 29), ('Czechia', 2017, 'F', 18.6), ('Denmark', 2017, 'F', 24.1),
                ('Germany', 2017, 'F', 17.3), ('Ireland', 2017, 'F', 45.1), ('Greece', 2017, 'F', 42.1),
                ('Spain', 2017, 'F', 17.3), ('France', 2017, 'F', 23.1), ('Croatia', 2017, 'F', 27.1),
                ('Italy', 2017, 'F', 11.4), ('Cyprus', 2017, 'F', 47.3), ('Latvia', 2017, 'F', 6.6),
                ('Luxembourg', 2017, 'F', 22.2), ('Hungary', 2017, 'F', 14.3), ('Malta', 2017, 'F', 25.9),
                ('Netherlands', 2017, 'F', 20.7), ('Austria', 2017, 'F', 32.9), ('Poland', 2017, 'F', 14.6),
                ('Portugal', 2017, 'F', 8.6), ('Slovenia', 2017, 'F', 19.2), ('Slovakia', 2017, 'F', 21.2),
                ('Finland', 2017, 'F', 19), ('Sweden', 2017, 'F', 27.9), ('Iceland', 2017, 'F', 36.6),
                ('Norway', 2017, 'F', 28.6), ('Switzerland', 2017, 'F', 33.9), ('United Kingdom', 2017, 'F', 34),
                ('Montenegro', 2017, 'F', 36.8), ('North Macedonia', 2017, 'F', 25.4), ('Serbia', 2017, 'F', 17.2)]

females_2018 = [('Belgium', 2018, 'F', 26.8), ('Czechia', 2018, 'F', 18.3), ('Denmark', 2018, 'F', 24.3),
                ('Germany', 2018, 'F', 17.3), ('Ireland', 2018, 'F', 44.8), ('Greece', 2018, 'F', 43.8),
                ('Spain', 2018, 'F', 20.5), ('France', 2018, 'F', 22.3), ('Croatia', 2018, 'F', 27.6),
                ('Italy', 2018, 'F', 12.8), ('Cyprus', 2018, 'F', 43.4), ('Latvia', 2018, 'F', 6),
                ('Luxembourg', 2018, 'F', 22.2), ('Hungary', 2018, 'F', 14.2), ('Malta', 2018, 'F', 21.8),
                ('Netherlands', 2018, 'F', 20.7), ('Austria', 2018, 'F', 32.2), ('Poland', 2018, 'F', 14.3),
                ('Portugal', 2018, 'F', 8.3), ('Slovenia', 2018, 'F', 17.7), ('Slovakia', 2018, 'F', 20.4),
                ('Finland', 2018, 'F', 16.5), ('Sweden', 2018, 'F', 27), ('Iceland', 2018, 'F', 34.6),
                ('Norway', 2018, 'F', 28.1), ('Switzerland', 2018, 'F', 34.6), ('United Kingdom', 2018, 'F', 32.6),
                ('Montenegro', 2018, 'F', 37.4), ('North Macedonia', 2018, 'F', 27.6), ('Serbia', 2018, 'F', 20.5)]


# 1. a function that generates dictionaries, and converts a tuple into dict with dict comprehensions

def dict_function(list_of_tuples):
    dict_from_list_of_tuples = {country_1: [year, sex, index_1] for country_1, year, sex, index_1 in list_of_tuples}
    return dict_from_list_of_tuples


males_2017_dict = dict_function(males_2017)
females_2017_dict = dict_function(females_2017)
males_2018_dict = dict_function(males_2018)
females_2018_dict = dict_function(females_2018)

# 2. two dicts that group all data by country for each year > health_index_2017 = {‘France’: [sex, health_index]}
dict_2017_all = males_2017_dict, females_2017_dict
dict_2018_all = males_2018_dict, females_2018_dict


# 3. one dict that groups all data by year for Germany > germany = {2017: [sex, health_index]}

def dict_function_germany(list_of_tuples):
    create_dict = {country_2: [year, sex, index_2]
                   for country_2, year, sex, index_2 in list_of_tuples if country_2 == 'Germany'}
    return create_dict


germany_males_2017 = dict_function_germany(males_2017)
germany_females_2017 = dict_function_germany(males_2017)
germany_males_2018 = dict_function_germany(males_2018)
germany_females_2018 = dict_function_germany(males_2018)

germany = germany_males_2017, germany_females_2017, germany_females_2018, germany_males_2018


# 3. Concatenate Country and year for dictionary "health_index = {‘France_2017’: [year, sex, health_index]}"

def dict_function_concat(list_of_tuples):
    create_dict = {country_3 + str("_2017"): [year, sex, index_3] for country_3, year, sex, index_3 in list_of_tuples}
    return create_dict


health_index = dict_function_concat(males_2017)
health_index_female = dict_function_concat(females_2017)


# 4. Health index > 5  starting from the previous health_index dict

health_index_5 = {}

for country, index in health_index.items():
    if int(index[2]) > 5:
        health_index_5[country] = index

health_index_5_female = {}

for country, index in health_index_female.items():
    if int(index[2]) > 5:
        health_index_5_female[country] = index

health_index_5_all = health_index_5, health_index_5_female


# 5. Health index > 5 and sex is 'F'

health_5_sex_F_female_2017 = dict()

for key, value in health_index_female.items():
    if str(value[1]):
        health_5_sex_F_female_2017[key] = value

health_5_sex_F_male_2017 = dict()

for key, value in health_index.items():
    if str(value[1]):
        health_5_sex_F_male_2017[key] = value

health_index_5_female_all = health_5_sex_F_male_2017, health_5_sex_F_female_2017


def print_results():
    print("Users from dict 2017 male and female, health_index_2017 =", dict_2017_all)
    print("Users from dict 2018 male and female, health_index_2018 =", dict_2018_all)
    print("Health Index concat Country_year: ", health_index)
    print("Dictionary for german male and female: germany =", germany)
    print("Countries with health index > 5 : ", health_index_5_all)
    print("Health index for Country > 5 and sex is F health_index =", health_index_5_female_all)


if __name__ == '__main__':
    print_results()
