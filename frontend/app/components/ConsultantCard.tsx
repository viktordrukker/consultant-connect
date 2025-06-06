import React from 'react';

interface ConsultantCardProps {
  name: string;
  expertise: string;
  rating: number;
  rate: number;
}

const ConsultantCard: React.FC<ConsultantCardProps> = ({ 
  name, 
  expertise, 
  rating,
  rate
}) => {
  return (
    <div className="bg-white rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow">
      <div className="flex items-center space-x-4 mb-4">
        <div className="bg-gray-200 border-2 border-dashed rounded-xl w-16 h-16" />
        <div>
          <h3 className="text-lg font-bold">{name}</h3>
          <p className="text-gray-600">{expertise}</p>
        </div>
      </div>
      
      <div className="flex justify-between items-center mb-4">
        <div className="flex items-center">
          <span className="text-yellow-500 mr-1">★</span>
          <span>{rating.toFixed(1)}</span>
        </div>
        <span className="font-bold">${rate}/min</span>
      </div>
      
      <button className="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition-colors">
        Request Session
      </button>
    </div>
  );
};

export default ConsultantCard;
