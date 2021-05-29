import './App.css';
import WorldDisplay from './world/WorldDisplay';
import React, { useEffect, useState } from 'react';


function App(props) {
  
  const [map, updateMap] = useState({});
  const [timeoutId, setTimeoutId] = useState(-1);

  useEffect(() => {
    fetch(`/world/`, {
      method: 'GET',
      headers: {
          'Content-Type': 'application/json'
      }
  }).then((res) => {
    if (res.ok)
      res.json().then((val) => {
        updateMap(val.map);
      })
  })
  },
    [props.first]
  );

  return (
    <div className="App">
      <WorldDisplay map={map} ready={Object.keys(map).length !== 0} />
    </div>
  );
}

export default App;
