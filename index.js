import { useEffect, useState } from 'react';

const TABS = ['Crypto', 'Stocks', 'Memecoins'];

export default function Home() {
  const [tab, setTab] = useState('Crypto');
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = () => {
      fetch(`/api/${tab.toLowerCase()}`)
        .then(res => res.json())
        .then(setData)
        .catch(() => setData([]));
    };

    fetchData();
    const interval = setInterval(fetchData, 2 * 60 * 1000); // refresh every 2 minutes
    return () => clearInterval(interval);
  }, [tab]);

  return (
    <div style={{ fontFamily: 'Arial', padding: '2rem' }}>
      <h1>Joe's Breakout Calls</h1>
      <div style={{ marginBottom: '1rem' }}>
        {TABS.map(t => (
          <button key={t} onClick={() => setTab(t)} style={{ marginRight: '1rem' }}>
            {t}
          </button>
        ))}
      </div>
      <h2>{tab} - Top Picks</h2>
      <ul>
        {data.map((d, i) => (
          <li key={i}>
            <strong>{d.name}</strong> — Score: {d.score?.toFixed(2)}<br />
            Price: ${d.price || '—'}<br />
            Reason: {d.reason}
          </li>
        ))}
      </ul>
    </div>
  );
}