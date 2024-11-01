from google_play_scraper import reviews
import pandas as pd
import numpy as np

# App ID for RepCount Gym Workout Tracker
app_id = 'com.purplecover.anylist'

# Fetch 500 reviews for the specified app
review_data, _ = reviews(
    app_id,
    lang='en',  # Language of the reviews
    country='gb',  # Country code for the reviews
    count=500  # Number of reviews to fetch
)

# Convert the fetched reviews into a DataFrame
df = pd.DataFrame(np.array(review_data), columns=['review'])

# Extract review details into a structured format
df2 = df.join(pd.DataFrame(df.pop('review').tolist()))

# Display the first few rows of the DataFrame
print(df2.head())

# Save the reviews to a CSV file
df2.to_csv('G:/My Drive/Uni 2024-25/Random/GetReviews/AnyList-Grocery-Shopping-List-Google-Play-UK.csv')
