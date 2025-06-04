import React, { useState, useEffect } from 'react'

const API_URL = import.meta.env.VITE_API_URL || '/api'

function App() {
  const [consultants, setConsultants] = useState([])
  useEffect(() => {
    fetch(`${API_URL}/consultants`)
      .then(res => res.json())
      .then(data => setConsultants(data))
      .catch(() => {})
  }, [])

  return (
    <div style={{ padding: '1rem' }}>
      <h1>Consultant Directory</h1>
      <ul>
        {consultants.map(c => (
          <li key={c.id}>{c.headline || 'No headline'} - rate: {c.hourly_rate}</li>
        ))}
      </ul>
    </div>
  )
}

export default App
