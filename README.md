# Top-Pick-Recommender-system

<img width="835" alt="Screenshot 2024-05-22 at 4 13 01 PM" src="https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/fe112906-3444-4b67-9b1d-8e1dd6d835e0">

## Steps to Build and use:

1. Running the Flask API for recommendations
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
  Check the Flask API on http://127.0.0.1:5000/api/recommend?user_id=1
  If status is 200, You are good!
  
2. Running the React App (for User Interface)

  ```
  ```bash
   # In a new terminal, go to this git parent directory
   cd Top-picks-recommenders-system
   # Create "react-frontend" react app
   npx create-react-app react-frontend
   # Copy the files as described in the above folder structure
   cd react-frontend
   cp ../react/index.html public/
   cp ../react/index.js src/
   cp ../react/Recommendations.js src/

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
    ├── src/
    │   ├── index.js  # Entry point for React
    │   ├── Recommendations.js  # Your component
    │   └── ...  # Other React files
    ├── package.json  # Node.js dependencies
    └── ...  # Other React files

Ouputs on User Selection:

<img width="886" alt="Screenshot 2024-05-22 at 7 34 30 PM" src="https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/dbc29a4f-23f3-4a0f-9fbe-463099f850bb">

<img width="834" alt="Screenshot 2024-05-22 at 7 34 23 PM" src="https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/e92fff54-47ab-4ee7-b167-368215f7b4ec

<img width="858" alt="Screenshot 2024-05-22 at 7 33 46 PM" src="https://github.com/manojbusam/Top-Pick-Recommender-system/assets/44409170/bc3e9a05-bff9-47d9-ac79-ba1acf20df0e">




