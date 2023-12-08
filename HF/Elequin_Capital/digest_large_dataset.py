"""
You are analyzing the high-end fine art market, as represented by a dataset showing all publicly
reported sales for over $100K of individual pieces throughout 2022.
The data you have is not in an ideal format. It is stored in a file containing only a single JSON array,
elements of which are JSON objects with the following keys: work_uid, purchaser_name,
purchase_timestamp, purchase_price_usd, appearance_at_purchase. The values paired with
these keys are, respectively, of types String, String, Number, Number, String.
For example, the JSON array could start as follows:
[{"work_uid": "LDMonaLisa", "purchaser_name": "Jeff Bezos", "purchase_timestamp":
1641416652, "purchase_price_usd": 1202000000, "appearance_at_purchase":
"Rml4ZWQgSW5jb21lIGlzIFJlYWxseS ...
A difficulty is the appearance_at_purchase values: they are Base64 encodings of extremely high
definition JPEGs of photographs of the works - the high definition is needed to protect against
fraud. Without the appearance_at_purchase values, the file would be less than 100 MB in size, but
as it is the file containing the JSON array is 1 TB in size, and you only have 16 GB of memory.
You wish to find:
- the sale with median price (or, if there are an even number of sales, the two middle sales)
- the Z-score of each purchase price
- the slope of the OLS regression of price on timestamp of sale
- the R2 of the OLS regression of price on timestamp of sale
- the total spends per purchaser in the market, represented as a CSV
- the work which changed hands the most times in the year
Write a class to find the desired values.
"""

# Use this logic:
# 1) use file.read(1) to read one character at a time
# 2) when you reach the substring "appearance_at_purchase:" you should skip everything that comes next until the closing brace } (potentially add an empty string), in this way you will have a well formed JSON
# 3) use json.loads to digest into a dataframe


import json
import pandas as pd
from scipy.stats import zscore
from sklearn.linear_model import LinearRegression

class FineArtMarketAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.load_and_clean_data()

    def load_and_clean_data(self):
        """Read file and skip large strings."""
        cleaned_data = ''
        skip = False
        with open(self.file_path, 'r') as file:
            while True:
                char = file.read(1)
                if not char:
                    break
                if char == '{':
                    skip = False
                elif char == '}':
                    skip = False
                    cleaned_data += char
                elif skip:
                    continue
                else:
                    cleaned_data += char
                    if cleaned_data.endswith('"appearance_at_purchase":'):
                        skip = True
                        cleaned_data = cleaned_data[:-len('"appearance_at_purchase":')]
        return pd.DataFrame(json.loads(cleaned_data))

    def median_sale_price(self):
        """Calculate the median sale price."""
        return self.data['purchase_price_usd'].median()

    def calculate_z_scores(self):
        """Calculate Z-scores for purchase prices."""
        self.data['z_score'] = zscore(self.data['purchase_price_usd'])

    def ols_regression_analysis(self):
        """Perform OLS regression and calculate slope and R^2."""
        model = LinearRegression()
        X = self.data[['purchase_timestamp']]
        y = self.data['purchase_price_usd']
        model.fit(X, y)
        slope = model.coef_[0]
        r_squared = model.score(X, y)
        return slope, r_squared

    def total_spends_per_purchaser(self):
        """Calculate total spends per purchaser."""
        return self.data.groupby('purchaser_name')['purchase_price_usd'].sum().to_csv('total_spends.csv')

    def most_frequently_traded_work(self):
        """Find the work which changed hands the most times."""
        return self.data['work_uid'].value_counts().idxmax()

# Usage
analyzer = FineArtMarketAnalyzer('path_to_file.json')
median_price = analyzer.median_sale_price()
analyzer.calculate_z_scores()
slope, r_squared = analyzer.ols_regression_analysis()
analyzer.total_spends_per_purchaser()
most_traded_work = analyzer.most_frequently_traded_work()
