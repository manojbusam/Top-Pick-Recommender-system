// src/index.js
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Recommendations from './Recommendations';
import reportWebVitals from './reportWebVitals';

ReactDOM.render(
    <React.StrictMode>
        <Recommendations />
    </React.StrictMode>,
    document.getElementById('root')
);

reportWebVitals();
