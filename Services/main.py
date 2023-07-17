from datetime import date  # core python module
import pandas as pd  # pip install pandas
from send_email import send_email  # local python module


# Public GoogleSheets url!
SHEET_ID = "1_MLxn3d55EMGB-WcHPrBKNqdAnE7p3Hq"
SHEET_NAME = "<Sheet1>"
URL = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"


def load_df(url):
    df = pd.read_csv(url, dtype={"Email address": str, "Bike Make & Model": str})
    return df

#print(load_df(URL))
def query_data_and_send_emails(df):
    present = date.today()
    bike_make_model = "Trek 520"
    email_counter = 0
    for _, row in df.iterrows():
        if (bike_make_model == row["Bike Make & Model"]) and (row["Bike(s) wheel size"] == "25\""):
            send_email(
                subject=f'[Bworks Org.] Thank you Mail {row["Bike Make & Model"]}',
                receiver_email=row["Email address"],
                name=row["Full name(s) of donor"],
                bike_make_model = row["Bike Make & Model"],
            )
            email_counter += 1
    return f"Total Emails Sent: {email_counter}"

df = (load_df(URL))
result = query_data_and_send_emails(df)
print(result)
