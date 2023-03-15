import datetime
import json
import os

DATA_FILE = "sales_data.json"


def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)


def input_sales():
    hot_dogs = int(input("How many hot dogs were sold today? "))
    arepas = int(input("How many arepas were sold today? "))
    strawberries_creme = int(input("How many strawberries with creme were sold today? "))
    drinks = int(input("How many drinks were sold today? "))

    return {
        "date": datetime.datetime.now().strftime("%Y-%m-%d"),
        "hot_dogs": hot_dogs,
        "arepas": arepas,
        "strawberries_creme": strawberries_creme,
        "drinks": drinks,
    }


def calculate_averages(data, days):
    end_date = datetime.datetime.strptime(data[-1]["date"], "%Y-%m-%d")
    start_date = end_date - datetime.timedelta(days=days - 1)
    relevant_data = [d for d in data if start_date <= datetime.datetime.strptime(d["date"], "%Y-%m-%d") <= end_date]

    averages = {}
    for key in ["hot_dogs", "arepas", "strawberries_creme", "drinks"]:
        averages[key] = sum([d[key] for d in relevant_data]) / len(relevant_data)

    return averages


# def main():
#     sales_data = load_data()
#     today_sales = input_sales()
#     sales_data.append(today_sales)
#     save_data(sales_data)
#
#     print("\nAverages:")
#     for days in [3, 7, 30]:
#         if len(sales_data) >= days:
#             averages = calculate_averages(sales_data, days)
#             print(f"{days}-day rolling averages:")
#             for key, value in averages.items():
#                 print(f"{key}: {value:.2f}")
#             print()
#
#     weekday = datetime.datetime.strptime(today_sales["date"], "%Y-%m-%d").strftime("%A")
#     weekday_data = [d for d in sales_data if
#                     datetime.datetime.strptime(d["date"], "%Y-%m-%d").strftime("%A") == weekday]
#     averages = calculate_averages(weekday_data, len(weekday_data))
#
#     print(f"Averages for {weekday}:")
#     for key, value in averages.items():
#         print(f"{key}: {value:.2f}")

def main():
    sales_data = load_data()
    today_sales = input_sales()
    sales_data.append(today_sales)
    save_data(sales_data)

    print("\nAverages:")
    for days in [3, 7, 30]:
        if len(sales_data) >= 1:
            averages = calculate_averages(sales_data, min(days, len(sales_data)))
            print(f"{days}-day rolling averages:")
            for key, value in averages.items():
                print(f"{key}: {value:.2f}")
            print()

    weekday = datetime.datetime.strptime(today_sales["date"], "%Y-%m-%d").strftime("%A")
    weekday_data = [d for d in sales_data if
                    datetime.datetime.strptime(d["date"], "%Y-%m-%d").strftime("%A") == weekday]
    averages = calculate_averages(weekday_data, len(weekday_data))

    print(f"Averages for {weekday}:")
    for key, value in averages.items():
        print(f"{key}: {value:.2f}")


if __name__ == "__main__":
    main()
