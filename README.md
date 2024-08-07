# Top-Pick-Recommender-system

![Screenshot 2024-05-27 at 3 09 50 PM](https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/11509257-cf39-4349-8b7e-0f377ca96c16)
![Screenshot 2024-05-27 at 3 10 00 PM](https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/0759830b-8a7c-4ebb-bb6a-7848869e9553)
![Screenshot 2024-05-27 at 3 10 10 PM](https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/5b76c619-e880-4b9b-9754-a8fb2e580ab1)

### Building Blocks and Step-by-Step Installation Guide

This repository contains the implementation of a Top Picks movie recommendation system using various technologies. Below are the building blocks and step-by-step installation instructions for setting up the system:

[![Unsupervised Machine Learning](https://img.shields.io/badge/Unsupervised%20Machine%20Learning-blue?style=flat-square&label=K-Means%20Clustering)](#unsupervised-machine-learning)

[![SQL DB](https://img.shields.io/badge/SQL%20DB%20Installation-green?style=flat-square&label=PostgreSQL)](#sql-db-installation)

[![Backend API](https://img.shields.io/badge/Backend%20API%20Installation-orange?style=flat-square&label=Flask%20API)](#backend-api-installation)

[![Frontend App](https://img.shields.io/badge/Frontend%20Installation-red?style=flat-square&label=React%20App)](#frontend-installation)


Please follow the step-by-step instructions provided in each section to set up the movie recommendation system on your local machine.

### 1. Applying K-Means Clustering 
### 1a. Steps to install
```bash  K-Means Clustering
  # Change directory to 
  cd Top-Pick-Recommender-system/flask-backend
  # 1. Install python ,if not already.
  # 2. Setup Virtual environment by running:
  python3 -m venv venv
  source venv/bin/activate
  # 3. Install all libs:
  pip3 install -r requirements.txt
  # 4. Taking "global_users.csv" and "local_users.csv" and creating "relevancy-toppicks.csv"
  python3 k_means_clustering.py
  ```
### 1b. K-Means Clustering of Users

<img width="1435" alt="Screenshot 2024-05-27 at 3 22 08 PM" src="https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/54578925-f5c9-4e50-a634-0c186f057761">

The K-means clustering algorithm is applied to local and global user data obtained from the 'local_users.csv' and 'global_users.csv' datasets. This algorithm partitions users into clusters based on their movie preferences. After clustering, recommendations are generated for each user within their respective cluster, and the results are saved to 'relevancy-toppicks.csv'.

### 1c. Usage:
  - Navigate to the project directory.
  - Set up a virtual environment and install dependencies as described above.
  - Run the 'k_means_clustering.py' script to perform clustering and generate recommendations.
  - The generated recommendations will be stored in the 'relevancy-toppicks.csv' file.
  - This process helps identify user clusters and provides personalized movie recommendations for better user engagement and satisfaction.

### 2. PostgreSQL Installation

2a. MacOS:
   - Install PostgreSQL using Homebrew:
     ```
     brew install postgresql
     ```
2b. Create Database:
   - Connect to PostgreSQL:
     ```
     psql
     ```
   - Create a database named `recommendations_db`:
     ```sql
     -- Drop the DATABASE if it already exists
     -- DROP DATABASE IF EXISTS recommendations_db;
     
     CREATE DATABASE recommendations_db;
     ```
   - Connect to the newly created database:
     ```
     \c recommendations_db
     ```

2c. Create Table:
   - Execute the following SQL command to create the `recommendations` table:
     ```sql
     -- Drop the table if it already exists
      -- DROP TABLE IF EXISTS toppicks_recommendations;
      
      -- Create the table
      CREATE TABLE toppicks_recommendations (
          user_id TEXT,
          title TEXT
      );

     ```

### 3. Flask API Installation 

3a. Loading the data in DB and Running the Flask API 
  ```bash flask-backend
  # Change directory to 
  cd Top-Pick-Recommender-system/flask-backend
  # 1. Install python ,if not already.
  # 2. Setup Virtual environment by running:
  python3 -m venv venv
  source venv/bin/activate
  # 3. Install all libs:
  pip3 install -r requirements.txt
  # 4. Change Postgre credentials
  Change at Top-Pick-Recommender-system/flask-backend/app.py and Top-Pick-Recommender-system/flask-backend/load_data.py
db_params = {
    'dbname': "recommendations_db",
    'user': "HERE",
    'password': "HERE",
    'host': "127.0.0.1",
    'port': "5432"
}
  # 4. Loading the data into DB
  python3 load_data.py
  # 5. Start the app
  python3 app.py
  ```
  Check the Flask API on http://127.0.0.1:5000/api/recommend?user_id=Manoj

  ![Screenshot 2024-05-27 at 3 44 28 PM](https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/39e1b64e-b66e-4eae-8b41-cd430e690fe1)

 

  

### 4. React App Installation

4a. Running the React App (for User Interface)

  ```
  ```bash
   # In a new terminal, go to this git parent directory
   cd Top-picks-recommenders-system
   # Create "react-frontend" react app
   npx create-react-app react-frontend
   # Copy the required files for running the react app
   cd react-frontend
   cp ../react/index.html public/
   cp ../react/index.js src/
   cp ../react/Recommendations.js src/
   cp -r ../images public/

   # Install node if not already, by running: brew install node
   # Start the APP
   npm start
  ```
  Check the User interface on http://localhost:3000/

  
## Overall Folder structure:
  ```bash
Top-picks-recommenders-system/
│
├── flask-backend/
│   ├── venv/  # Virtual environment directory
│   ├── app.py  # Flask application
│   ├── load_data.py  # Flask application
│   ├── relevancy-toppicks.csv  # Flask application
│   └── global_users.csv
│   └── local_users.csv
│   └── k_means_clustering.py
│   
│
└── react-frontend/
      ├── node_modules/  # Node.js modules
      ├── public/
      │   ├── index.html  # html page
      ├── ├── images/
      ├   ├      ├──Manoj.png
      ├   ├      ├──Vijaysri.png
      ├   ├      ├──Professor.png
      ├── src/
      │   ├── index.js  # Entry point for React
      │   ├── Recommendations.js  # Your component
      │   └── ...  # Other React files
      ├── package.json  # Node.js dependencies
      └── ...  # Other React files
  ```



