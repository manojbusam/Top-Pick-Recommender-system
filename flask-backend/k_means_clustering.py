import pandas as pd
from sklearn.cluster import KMeans

# Load data
local_data = pd.read_csv('local_users.csv')
global_data = pd.read_csv('global_users.csv')

# Merge datasets to get user and movie information
merged_data = pd.merge(local_data, global_data, on='movie_id')

# Create user-item matrix
user_item_matrix = merged_data.pivot_table(index='user_id_x', columns='movie_id', values='rating_y')

# Fill missing values with 0
user_item_matrix.fillna(0, inplace=True)

# Perform k-means clustering
kmeans = KMeans(n_clusters=3, random_state=42)
clusters = kmeans.fit_predict(user_item_matrix)

# Get cluster centroids
cluster_centers = kmeans.cluster_centers_

# Recommend top picks for each local user based on cluster centroids
recommendations = []
for user_id, user_ratings in user_item_matrix.iterrows():
    user_ratings = user_ratings.sort_values(ascending=False)
    user_watched_movies = local_data[local_data['user_id'] == user_id]['movie_id'].tolist()
    user_cluster = clusters[user_id - 31]  # Adjusted index to match 0-based indexing
    centroid_ratings = cluster_centers[user_cluster]
    centroid_ratings_series = pd.Series(centroid_ratings, index=user_item_matrix.columns)
    recommended_movies = centroid_ratings_series.sort_values(ascending=False).index
    for movie_id in recommended_movies:
        if movie_id not in user_watched_movies:
            movie_title = global_data[global_data['movie_id'] == movie_id]['movie'].iloc[0]
            recommendations.append((user_id, round(user_ratings[movie_id] * 100, 3), movie_title))

# Create DataFrame for recommendations
df_recommendations = pd.DataFrame(recommendations, columns=['user_id','ratings','title'])

# Merge DataFrames on 'user_id' column
merged_df = pd.merge(df_recommendations, local_data, on='user_id', how='inner')

# Select desired columns
combined_df = merged_df[['user','title']]

# Save to CSV file
combined_df.to_csv('relevancy-toppicks.csv', index=False)
