import pandas as pd

df = pd.read_csv('US_Regional_Sales_Data(1).csv')
print(df)

from datetime import datetime

def standardized_date(date_str):
    try:
        # Parse dates, assuming the input format is either dd/mm/yy or dd/mm/yyyy
        if len(date_str.split('/')[-1]) == 2:
            date_obj = datetime.strptime(date_str, '%d/%m/%y')
            return date_obj.strftime('%d/%m/%Y')
        else:
            date_obj = datetime.strptime(date_str, '%d/%m/%Y')
            return date_obj.strftime('%d/%m/%Y')
    except ValueError:
        return None  # Handle parsing errors if necessary

# Convert order and delivery dates to dd/mm/yyyy
df['OrderDate'] = df['OrderDate'].apply(standardized_date)
df['DeliveryDate'] = df['DeliveryDate'].apply(standardized_date)

# Convert the columns to datetime format using pandas
df['OrderDate'] = pd.to_datetime(df['OrderDate'], format='%d/%m/%Y')
df['DeliveryDate'] = pd.to_datetime(df['DeliveryDate'], format='%d/%m/%Y')

# Calculate the date difference (delivery - order)
df['date_difference'] = (df['DeliveryDate'] - df['OrderDate']).dt.days

# Display the DataFrame with the date differences
print(df[['OrderDate', 'DeliveryDate', 'date_difference']])
print(df)