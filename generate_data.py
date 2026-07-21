import os
import random
from datetime import datetime, timedelta

import numpy as np
import pandas as pd
from faker import Faker

fake = Faker()
Faker.seed(42)
random.seed(42)
np.random.seed(42)

DATA_DIR = "data"
OUTPUT_FILE = os.path.join(DATA_DIR, "customer_data.csv")

NUM_CUSTOMERS = 5000

SEGMENTS = [
    "VIP",
    "Premium",
    "Regular",
    "At Risk",
    "New"
]

REGIONS = [
    "North",
    "South",
    "East",
    "West",
    "Central"
]

PAYMENT_METHODS = [
    "Credit Card",
    "Debit Card",
    "UPI",
    "Net Banking",
    "Cash",
    "Wallet"
]

CHANNELS = [
    "Website",
    "Mobile App",
    "Instagram",
    "Facebook",
    "Google Ads",
    "Referral",
    "Email Campaign"
]

PRODUCTS = [
    "Electronics",
    "Fashion",
    "Home",
    "Sports",
    "Beauty",
    "Books",
    "Groceries"
]

LOYALTY_LEVELS = [
    "Bronze",
    "Silver",
    "Gold",
    "Platinum"
]


def random_join_date():
    start = datetime.now() - timedelta(days=1800)
    end = datetime.now()

    delta = end - start

    random_days = random.randint(0, delta.days)

    return start + timedelta(days=random_days)


def calculate_age():
    return random.randint(18, 70)


def customer_segment(total_spent):

    if total_spent >= 250000:
        return "VIP"

    if total_spent >= 120000:
        return "Premium"

    if total_spent >= 40000:
        return "Regular"

    if total_spent >= 15000:
        return "New"

    return "At Risk"


def loyalty_level(total_spent):

    if total_spent >= 250000:
        return "Platinum"

    if total_spent >= 120000:
        return "Gold"

    if total_spent >= 60000:
        return "Silver"

    return "Bronze"


def customer_score(total_spent,
                   orders,
                   satisfaction):

    score = (
        total_spent / 5000
        + orders * 2
        + satisfaction * 10
    )

    score = min(score, 100)

    return round(score, 2)


def churn_probability(days_since_last_purchase,
                      satisfaction,
                      orders):

    risk = 0

    risk += min(days_since_last_purchase / 2, 50)

    risk += (5 - satisfaction) * 10

    risk -= min(orders, 20)

    risk = max(0, min(risk, 100))

    return round(risk, 2)


def yearly_income():

    return random.randint(
        250000,
        3000000
    )


def monthly_income():

    return yearly_income() // 12


def total_orders():

    return random.randint(
        1,
        120
    )


def average_order_value():

    return random.randint(
        500,
        8000
    )


def total_spent(
        orders,
        avg):

    return orders * avg


def customer_lifetime_value(total):

    multiplier = random.uniform(
        1.2,
        3.8
    )

    return round(
        total * multiplier,
        2
    )
def generate_customer(customer_id):

    first_name = fake.first_name()
    last_name = fake.last_name()

    full_name = f"{first_name} {last_name}"

    age = calculate_age()

    gender = random.choice([
        "Male",
        "Female"
    ])

    email = fake.email()

    phone = fake.msisdn()[:10]

    city = fake.city()

    state = fake.state()

    country = "India"

    region = random.choice(REGIONS)

    join_date = random_join_date()

    orders = total_orders()

    avg_order = average_order_value()

    spent = total_spent(
        orders,
        avg_order
    )

    clv = customer_lifetime_value(
        spent
    )

    income = yearly_income()

    satisfaction = round(
        random.uniform(
            2.5,
            5.0
        ),
        1
    )

    discount_usage = random.randint(
        0,
        100
    )

    returns = random.randint(
        0,
        15
    )

    support_tickets = random.randint(
        0,
        20
    )

    website_visits = random.randint(
        5,
        300
    )

    app_sessions = random.randint(
        0,
        200
    )

    wishlist_items = random.randint(
        0,
        40
    )

    cart_abandonments = random.randint(
        0,
        30
    )

    referral_count = random.randint(
        0,
        25
    )

    days_since_purchase = random.randint(
        1,
        365
    )

    churn = churn_probability(
        days_since_purchase,
        satisfaction,
        orders
    )

    segment = customer_segment(
        spent
    )

    loyalty = loyalty_level(
        spent
    )

    score = customer_score(
        spent,
        orders,
        satisfaction
    )

    payment = random.choice(
        PAYMENT_METHODS
    )

    channel = random.choice(
        CHANNELS
    )

    favorite_category = random.choice(
        PRODUCTS
    )

    coupon_used = random.choice([
        "Yes",
        "No"
    ])

    premium_member = random.choice([
        "Yes",
        "No"
    ])

    newsletter = random.choice([
        "Subscribed",
        "Not Subscribed"
    ])

    last_purchase = (
        datetime.now()
        - timedelta(days=days_since_purchase)
    ).date()

    return {

        "Customer ID": customer_id,

        "Name": full_name,

        "Age": age,

        "Gender": gender,

        "Email": email,

        "Phone": phone,

        "City": city,

        "State": state,

        "Country": country,

        "Region": region,

        "Join Date": join_date.date(),

        "Last Purchase": last_purchase,

        "Orders": orders,

        "Average Order Value": avg_order,

        "Total Revenue": spent,

        "Customer Lifetime Value": clv,

        "Annual Income": income,

        "Monthly Income": income // 12,

        "Satisfaction Score": satisfaction,

        "Customer Score": score,

        "Churn Risk": churn,

        "Segment": segment,

        "Loyalty Level": loyalty,

        "Favorite Category": favorite_category,

        "Payment Method": payment,

        "Acquisition Channel": channel,

        "Discount Usage (%)": discount_usage,

        "Returns": returns,

        "Support Tickets": support_tickets,

        "Website Visits": website_visits,

        "App Sessions": app_sessions,

        "Wishlist Items": wishlist_items,

        "Cart Abandonments": cart_abandonments,

        "Referral Count": referral_count,

        "Coupon Used": coupon_used,

        "Premium Member": premium_member,

        "Newsletter": newsletter,

        "Days Since Last Purchase": days_since_purchase

    }


def generate_dataset():

    customers = []

    for i in range(1, NUM_CUSTOMERS + 1):

        customer = generate_customer(
            i
        )

        customers.append(customer)

    df = pd.DataFrame(
        customers
    )

    return df
def validate_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """
    Validate and clean the generated dataset.
    """

    numeric_columns = [
        "Orders",
        "Average Order Value",
        "Total Revenue",
        "Customer Lifetime Value",
        "Annual Income",
        "Monthly Income",
        "Satisfaction Score",
        "Customer Score",
        "Churn Risk",
        "Discount Usage (%)",
        "Returns",
        "Support Tickets",
        "Website Visits",
        "App Sessions",
        "Wishlist Items",
        "Cart Abandonments",
        "Referral Count",
        "Days Since Last Purchase",
    ]

    for column in numeric_columns:
        df[column] = pd.to_numeric(df[column], errors="coerce")

    df.drop_duplicates(subset="Customer ID", inplace=True)

    df.reset_index(drop=True, inplace=True)

    return df


def create_directories():
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs("reports", exist_ok=True)


def save_dataset(df: pd.DataFrame):

    csv_path = OUTPUT_FILE

    excel_path = os.path.join(
        DATA_DIR,
        "customer_data.xlsx"
    )

    df.to_csv(
        csv_path,
        index=False
    )

    df.to_excel(
        excel_path,
        index=False,
        engine="openpyxl"
    )

    print("=" * 60)
    print(" AI CUSTOMER INTELLIGENCE PLATFORM V2 PRO ")
    print("=" * 60)

    print(f"Customers Generated : {len(df):,}")
    print(f"CSV Saved           : {csv_path}")
    print(f"Excel Saved         : {excel_path}")

    print("-" * 60)

    print(
        f"Average Revenue     : ₹{df['Total Revenue'].mean():,.2f}"
    )

    print(
        f"Average CLV         : ₹{df['Customer Lifetime Value'].mean():,.2f}"
    )

    print(
        f"Average Churn Risk  : {df['Churn Risk'].mean():.2f}%"
    )

    print(
        f"Average Score       : {df['Customer Score'].mean():.2f}"
    )

    print("-" * 60)

    print("\nSegment Distribution\n")

    print(
        df["Segment"]
        .value_counts()
        .sort_index()
    )

    print("\nLoyalty Distribution\n")

    print(
        df["Loyalty Level"]
        .value_counts()
        .sort_index()
    )

    print("=" * 60)
    print("Dataset Generated Successfully!")
    print("=" * 60)


def main():

    create_directories()

    print("Generating customer dataset...\n")

    df = generate_dataset()

    df = validate_dataset(df)

    save_dataset(df)


if __name__ == "__main__":
    main()