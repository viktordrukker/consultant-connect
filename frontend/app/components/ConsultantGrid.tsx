import React from 'react';
import ConsultantCard from './ConsultantCard';

const ConsultantGrid: React.FC = () => {
  // Mock data - will be replaced with API call
  const consultants = [
    { id: 1, name: "Alex Johnson", expertise: "Business Strategy", rating: 4.8, rate: 120 },
    { id: 2, name: "Sarah Williams", expertise: "Marketing Analytics", rating: 4.9, rate: 150 },
    { id: 3, name: "Michael Chen", expertise: "Product Development", rating: 4.7, rate: 110 },
    { id: 4, name: "Emily Rodriguez", expertise: "Financial Planning", rating: 4.9, rate: 140 },
    { id: 5, name: "David Kim", expertise: "Tech Innovation", rating: 4.6, rate: 130 },
    { id: 6, name: "Priya Sharma", expertise: "Operations Management", rating: 4.8, rate: 125 },
  ];

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      {consultants.map((consultant) => (
        <ConsultantCard
          key={consultant.id}
          name={consultant.name}
          expertise={consultant.expertise}
          rating={consultant.rating}
          rate={consultant.rate}
        />
      ))}
    </div>
  );
};

export default ConsultantGrid;
