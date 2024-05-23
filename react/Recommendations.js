import React, { useEffect, useState } from 'react';

function Recommendations() {
    const [recommendations, setRecommendations] = useState([]);
    const [userPhoto, setUserPhoto] = useState('');

    useEffect(() => {
        const fetchUserData = async () => {
            try {
                const searchParams = new URLSearchParams(window.location.search);
                const userId = searchParams.get('user_id') || 'Manoj';
                const photoUrl = `/images/${userId}.png`; // Assuming photos are stored in public/images/
                setUserPhoto(photoUrl);
            } catch (error) {
                console.error('Error fetching user data:', error);
            }
        };

        const fetchRecommendations = async () => {
            try {
                const searchParams = new URLSearchParams(window.location.search);
                const userId = searchParams.get('user_id') || 'Manoj';
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

        fetchUserData();
        fetchRecommendations();
    }, []);

    return (
        <div className="recommendations">
            <div className="user-photo-container">
                {userPhoto && <img src={userPhoto} alt="User Photo" className="user-photo" />}
            </div>
            <div className="top-picks-container">
                <h2>Your Top Picks</h2>
                <ul>
                     {recommendations.map((item, index) => (
                        <li key={index}>
                            {item.title} - {item.relevancy} %
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
}

export default Recommendations;
