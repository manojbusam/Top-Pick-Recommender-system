# Top-Pick-Recommender-system

<img width="835" alt="Screenshot 2024-05-22 at 4 13 01 PM" src="https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/fe112906-3444-4b67-9b1d-8e1dd6d835e0">

## Steps to Build and use:

### 1. PostgreSQL Installation

1a. MacOS:
   - Install PostgreSQL using Homebrew:
     ```
     brew install postgresql
     ```
1b. Create Database:
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

1c. Create Table:
   - Execute the following SQL command to create the `recommendations` table:
     ```sql
     -- Drop the table if it already exists
      -- DROP TABLE IF EXISTS toppicks_recommendations;
      
      -- Create the table
      CREATE TABLE toppicks_recommendations (
          user_id TEXT,
          relevancy INTEGER,
          title TEXT
      );

     ```

1d. Insert Records:
   - Execute the following SQL commands to insert records for "Manoj", "Vijju", and "Kids":
     ```sql
     INSERT INTO toppicks_recommendations (user_id, relevancy, title) VALUES
     ('Manoj', 97, 'Salaar'),
     ('Manoj', 65, 'Animal'),
     ('Manoj', 75, 'Oppenheimer'),
     ('Vijju', 85, 'Hi Nanna'),
     ('Vijju', 95, 'Nani''s Majnu'),
     ('Kids', 100, 'Shinchan'),
     ('Kids', 100, 'Doremon');
     ```

1e. Checking records:

   ```sql
   SELECT * FROM toppicks_recommendations;
   ```
   ![Screenshot 2024-05-23 at 9 56 25 AM](https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/309d6c52-8352-4192-a324-c3225b7a4680)

### 2. Flask API Installation

2a. Running the Flask API for recommendations
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
  
  ![Screenshot 2024-05-23 at 10 05 33 AM](https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/cd003075-4bf0-4ab0-ac4e-04944228bad3)

  

### 3. React App Installation

3a. Running the React App (for User Interface)

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

  
## 4. Overall Folder structure:
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
## 5. Ouputs on User Selection:

![Screenshot 2024-05-23 at 9 34 45 AM](https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/c3a0a6b6-61c5-4ac1-abb2-f0d9c4b81647)

<img width="834" alt="Screenshot 2024-05-22 at 7 34 23 PM" src="https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/858261d5-a599-4393-9f8d-ddc94191e404">

<img width="886" alt="Screenshot 2024-05-22 at 7 34 30 PM" src="https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/be21446a-ac6f-4a3d-9f5b-b0fd34d7318e">



