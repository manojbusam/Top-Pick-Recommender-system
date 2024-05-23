# Top-Pick-Recommender-system

<img width="835" alt="Screenshot 2024-05-22 at 4 13 01 PM" src="https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/fe112906-3444-4b67-9b1d-8e1dd6d835e0">

## Steps to Build and use:

### PostgreSQL Installation

1. **MacOS:**
   - Install PostgreSQL using Homebrew:
     ```
     brew install postgresql
     ```

### Database Setup

1a. Create Database:
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

1b. Create Table:
   - Execute the following SQL command to create the `recommendations` table:
     ```sql
     -- Drop the table if it already exists
      -- DROP TABLE IF EXISTS recommendations;
      
      -- Create the table
      CREATE TABLE recommendations (
          user_id TEXT,
          movie_id INTEGER,
          title TEXT
      );

     ```

1c. Insert Records:
   - Execute the following SQL commands to insert records for "Manoj", "Vijju", and "Kids":
     ```sql
     INSERT INTO recommendations (user_id, movie_id, title) VALUES
     ('Manoj', 101, 'Salaar'),
     ('Manoj', 102, 'Animal'),
     ('Manoj', 107, 'Oppenheimer'),
     ('Vijju', 103, 'Hi Nanna'),
     ('Vijju', 104, 'Nani''s Majnu'),
     ('Kids', 105, 'Shinchan'),
     ('Kids', 106, 'Doremon');
     ```

1d. Checking records:

   ```sql
   SELECT * FROM recommendations;
   ```
   ![Screenshot 2024-05-23 at 9 18 36 AM](https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/b908c13f-e859-4fd1-bdcf-d868c07ba530)

### Flask API Installation

2. Running the Flask API for recommendations
  ```bash flask-backend
  # Change directory to 
  cd Top-Pick-Recommender-system/flask-backend
  # 1. Install python ,if not already.
  # 2. Setup Virtual environment by running:
  python -m venv venv
  source venv/bin/activate
  # 3. Start the app
  python app.py
  ```
  Check the Flask API on http://127.0.0.1:5000/api/recommend?user_id=Manoj
  If status is 200, You are good!

### React App Installation

3. Running the React App (for User Interface)

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
│   └── requirements.txt  # List of Python dependencies
│
└── react-frontend/
      ├── node_modules/  # Node.js modules
      ├── public/
      │   ├── index.html  # html page
      ├── ├── images/
      ├   ├      ├──Manoj.png
      ├   ├      ├──Vijju.png
      ├   ├      ├──Kids.png
      ├── src/
      │   ├── index.js  # Entry point for React
      │   ├── Recommendations.js  # Your component
      │   └── ...  # Other React files
      ├── package.json  # Node.js dependencies
      └── ...  # Other React files
  ```
Ouputs on User Selection:


<img width="858" alt="Screenshot 2024-05-22 at 7 33 46 PM" src="https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/02e63ab1-1e57-4345-9ac2-90b5b36990e8">

<img width="834" alt="Screenshot 2024-05-22 at 7 34 23 PM" src="https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/858261d5-a599-4393-9f8d-ddc94191e404">

<img width="886" alt="Screenshot 2024-05-22 at 7 34 30 PM" src="https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/be21446a-ac6f-4a3d-9f5b-b0fd34d7318e">



