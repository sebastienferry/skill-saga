import React, { useEffect, useState } from 'react';
import axios from 'axios';

interface Objective {
  name: string;
  position: number;
}

const Objectives: React.FC = () => {
  const [objectives, setObjectives] = useState<Objective[]>([]);
  const apiBaseURl = process.env.NEXT_PUBLIC_API_BASE_URL;

  useEffect(() => {
    const fetchObjectives = async () => {
      try {
        const response = await axios.get<Objective[]>(apiBaseURl + '/objectives');
        setObjectives(response.data);
      } catch (error) {
        console.error('Error fetching objectives:', error);
      }
    };

    fetchObjectives();
  }, []);

  return (
    <div>
      <h1>Liste des Objectifs</h1>
      <ul>
        {objectives.map((objective) => (
          <li key={objective.name}>
            <h2>{objective.name}</h2>            
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Objectives;