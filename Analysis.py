import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('movies.csv')

# Clean Released_Year if it's not numeric
df['Released_Year'] = pd.to_numeric(df['Released_Year'], errors='coerce')
df.dropna(subset=['Released_Year'], inplace=True)
df['Released_Year'] = df['Released_Year'].astype(int)

# Handle any other missing data
df.dropna(inplace=True)

# Movies ranked by IMDB rating
print("\nAll Movies Rankked by IMDB Rating:\n")

# Sort movies by IMDB rating
ranked_movies = df.sort_values(by='IMDB_Rating', ascending=False)[['Series_Title', 'IMDB_Rating']]
# Reset index for better readability
ranked_movies.reset_index(drop=True, inplace=True)
ranked_movies.index += 1  # Start index at 1 for better readability
print(ranked_movies.to_string())

ranked_movies.index = ranked_movies.index + 1  # Start index at 1 for better readability
print(ranked_movies.head)
# Add decade column
df['Decade'] = (df['Released_Year'] // 10) * 10

# Plot movies per decade
df['Decade'].value_counts().sort_index().plot(kind='bar', color='skyblue')
plt.title('Number of Movies per Decade')
plt.xlabel('Decade')
plt.ylabel('Count')
plt.tight_layout()
plt.show()
