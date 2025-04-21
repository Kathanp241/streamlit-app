# streamlit-app

# 🚗 Used Car Price Explorer

This is a Streamlit app that allows users to explore a dataset of used cars, filter by car brands and fuel types, and view dynamic visualizations such as price distribution, average price by brand, and fuel type distribution.

# Features:

Filter car data by brand and fuel type

# Visualize data with interactive charts:

Average price per brand

Price distribution over the years

Price distribution by fuel type

Fuel type share (Pie chart)

Kilometers driven distribution (Histogram)

Dynamic and interactive graphs using Plotly

Prerequisites:
Before running the app, ensure you have the following installed:

Python 3.x (Recommended: Python 3.7 or higher)

Streamlit for app rendering

Pandas for data manipulation

Plotly for interactive plots

Setup & Installation:
Follow the steps below to run the app locally:

Clone the repository or download the app files.

bash
Copy
Edit
git clone <repo-url>
Install required dependencies: Ensure you have pip installed. Run the following to install the required libraries:

bash
Copy
Edit
pip install -r requirements.txt
Place the dataset cars.csv: Ensure you have a file named cars.csv containing your car data in the same folder as the app.py.

Run the Streamlit app: From the terminal, navigate to the directory containing the app files and run:

bash
Copy
Edit
streamlit run app.py
Example cars.csv:
Here’s a sample cars.csv file you can use to get started:

csv
Copy
Edit
name,year,km_driven,fuel,seller_type,transmission,owner,mileage,engine,max_power,price
Maruti Swift,2014,70000,Petrol,Individual,Manual,First Owner,22.0 kmpl,1197 CC,82 bhp,4.2
Hyundai i20,2016,50000,Diesel,Dealer,Manual,Second Owner,18.0 kmpl,1396 CC,90 bhp,5.5
Honda City,2015,40000,Petrol,Individual,Manual,First Owner,17.4 kmpl,1497 CC,117 bhp,6.0
Toyota Innova,2012,90000,Diesel,Individual,Manual,Second Owner,12.8 kmpl,2494 CC,102 bhp,7.8
Ford Ecosport,2018,30000,Diesel,Dealer,Manual,First Owner,23.0 kmpl,1498 CC,99 bhp,8.2
Tata Tiago,2019,15000,Petrol,Individual,Manual,First Owner,23.8 kmpl,1199 CC,84 bhp,4.9
Features Overview:
Sidebar Filters:
Users can filter the dataset based on car brands and fuel types from the sidebar options.

Price by Brand:
A bar chart showing the average price of cars by their brand.

Price vs Year:
A scatter plot displaying the relationship between the car's price and the year of manufacture.

Fuel Type Distribution:
A pie chart visualizing the distribution of car types based on fuel.

Price Distribution by Fuel Type:
A box plot to show how car prices vary based on fuel type.

Kilometers Driven Histogram:
A histogram showing the distribution of cars based on kilometers driven.

Example Screenshots:
Here you can include some screenshots of your app. These images will help potential users see what the app looks like.

Running in the Cloud (Streamlit Sharing):
You can also deploy the app on Streamlit Cloud for sharing with others:

Push your code to GitHub.

Go to Streamlit Cloud and sign in.

Deploy directly from your GitHub repository.

Acknowledgements:
This app uses the Iris Dataset (or any used car dataset you choose) and showcases how to combine Streamlit with Plotly for dynamic visualizations.

License:
This project is open source and available under the MIT License.

Contact:
For questions, feature requests, or bug reports, contact [Your Name] at [Your Email].
