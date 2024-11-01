from app_store_scraper import AppStore
import pandas as pd
import numpy as np

# Initialize the AppStore scraper with UK country code 'gb'
app = AppStore(country='us', app_name='fitness-ai-gym-workout-planner', app_id='1446224156')

# Fetch reviews, request 100
app.review(how_many=500)

# Convert the fetched reviews into a DataFrame
df = pd.DataFrame(np.array(app.reviews), columns=['review'])

# Extract the review details into a structured format
df2 = df.join(pd.DataFrame(df.pop('review').tolist()))

# Display the first few rows of the DataFrame
df2.head()

# Save the reviews to a CSV file
df2.to_csv('G:/My Drive/Uni 2024-25/Random/GetReviews/fitness-ai-gym-workout-planner-App-Store-UK.csv')
