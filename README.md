## 📊 Metadata EDA for viewership Data

- This respository contains a Python script for performing Exploratory Data Analysis (EDA) on Viewership data using pandas. It focuses on analyzing metadatab attributes of a dataset containing (DateID, CustomerID, TotalTimeWatched, Platform, PlayEventType,and VideoTitle)

## 🗂️ Dataset

- 🚀 The dataset ('Viewership Analysis .xlsx') includes:
  
• DateID: A unique identifier for a specific date or timestamp, this represents a date in a numerical format. Stored as a 64-bit (integer).

• CustomerID: A unique identifier for a customer (IS a string and alphanumeric value). stored as an (object).

• TotalTimeWatched: The total amount of time (is in seconds, minutes and hours) a customer spent watching a video, stored as a 64-bit integer (float).

• Platform: is a where the video was watched (string).

• .PlayEventType: The type of play event associated with the video, stored as an object (string). This could indicate the nature of the interaction, such as 'Start', 'Pause', 'Resume', and 'Complete'.

• VideoTitle): The title or name of the video watched (String).

## 🧪 EDA script
## 💾 Output

• The script outputs metadata, unique values, summary statistics, and the cleaned Data Frame after removing duplicates.

## 🛠️ Tools Used

+ 🧱 Databricks – Data processing, ETL
  
+ 🐼 Pandas – Data cleaning, manipulation, analysis
  
+ 🔢 NumPy – Numerical operations, arrays, calculations
    
+ 📊 Excel – Data source
