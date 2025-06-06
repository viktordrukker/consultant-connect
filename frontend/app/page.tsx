"use client";
import ConsultantGrid from '@/components/ConsultantGrid';

export default function Home() {
  return (
    <div className="container mx-auto py-8">
      <div className="mb-10 text-center">
        <h1 className="text-4xl font-bold mb-4">Find Expert Consultants</h1>
        <p className="text-lg text-gray-600 max-w-2xl mx-auto">
          Connect instantly with industry experts for real-time video consultations. 
          First 10 minutes free, then only pay for the time you use.
        </p>
      </div>
      
      <div className="mb-8">
        <div className="flex items-center justify-between mb-6">
          <h2 className="text-2xl font-bold">Available Consultants</h2>
          <div className="flex space-x-4">
            <select className="border border-gray-300 rounded-md px-3 py-2">
              <option>All Specializations</option>
              <option>Business Strategy</option>
              <option>Marketing</option>
              <option>Technology</option>
              <option>Finance</option>
            </select>
            <select className="border border-gray-300 rounded-md px-3 py-2">
              <option>Sort by: Rating</option>
              <option>Sort by: Price (Low to High)</option>
              <option>Sort by: Price (High to Low)</option>
            </select>
          </div>
        </div>
        <ConsultantGrid />
      </div>
    </div>
  );
}
