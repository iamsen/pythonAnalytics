__author__ = 'sen.li'

import pandas


artworks = pandas.read_csv("Artworks.csv")
# print artworks.head(10)

# Number of artworks in each Date WITHOUT cleaning up
# print artworks['Date'].value_counts()


def clean_dates(row):
    initial_date = row['Date']
    final_date = initial_date

    try:
        split_date = initial_date.split('-')
        if len(split_date) > 1:
            final_date = split_date[0]
            return final_date
    except Exception as e:
        # swallow 'float' object has no attribute 'split'
        pass

    if initial_date == "n.d.":
        final_date = "Unknown"
        return final_date

    # Pattern 2
    else:
        try:
            final_date = initial_date.lstrip("c. ")
        except Exception as e:
            # 'NoneType' object has no attribute 'lstrip'
            pass
    return final_date


artworks['Date'] = artworks.apply(lambda row: clean_dates(row), axis=1)
print artworks['Date'].value_counts()

