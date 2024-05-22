import React, { useEffect, useState } from 'react';

function Recommendations() {
    const [recommendations, setRecommendations] = useState([]);

    useEffect(() => {
        const fetchRecommendations = async () => {
            try {
                const userId = 1; // Example user ID
                const response = await fetch(`http://127.0.0.1:5000/api/recommend?user_id=${userId}`);
                if (!response.ok) {
                    throw new Error('Network response was not ok');
                }
                const data = await response.json();
                setRecommendations(data);
            } catch (error) {
                console.error('Error fetching recommendations:', error);
            }
        };
        fetchRecommendations();
    }, []);

    return (
        <div className="recommendations">
            <h2>Your Top Picks</h2>
            <ul>
                {recommendations.map(item => (
                    <li key={item.id}>{item.title}</li>
                ))}
            </ul>
        </div>
    );
}

export default Recommendations;
