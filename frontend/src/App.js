import './App.css';
import WorldDisplay from './world/WorldDisplay';
import Lobby from './Lobby';
import React, { useEffect, useState } from 'react';


function App(props) {

    const [session_code, setSession] = useState('');
    const [error_code, setError] = useState('');
    const [inGame, setInGame] = useState(false);

    const attemptJoin = () => {
        fetch(`/session/get/${session_code}/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        }).then((res) => {
            if (res.ok)
                res.json().then((data) => {
                    // {code: '', settings: {}}
                    if (data.code === '') {
                        setError("Cannot join that game.");
                        setSession("");
                        return;
                    }
                    setInGame(true);
                })
        })
    }

    const newGame = () => {
        fetch(`/session/new/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        }).then((res) => {
            if (res.ok)
                res.json().then((data) => {
                    // {code: '', settings: {}}
                    setSession(data.code);
                    setInGame(true);
                })
        })
    }

    const inputChange = (e) => {
        setSession(e.target.value);
    }

    const leaveSession = () => {
        setError('');
        setSession('');
        setInGame(false);
    }

    if (inGame) {
        return (
            <div>
                <Lobby code={session_code} leave={leaveSession} />
            </div>
        );
    }

    return (
        <div>
            <Error message={error_code} />
            <p>Enter a game code</p>
            <input type="text" value={session_code} onChange={inputChange} />
            <button onClick={attemptJoin}>Join</button>
            <p>Or create a new game</p>
            <button onClick={newGame}>New Game</button>
        </div>
    );

    // const [map, updateMap] = useState({});
    // const [timeoutId, setTimeoutId] = useState(-1);

    // useEffect(() => {
    //   fetch(`/world/`, {
    //     method: 'GET',
    //     headers: {
    //         'Content-Type': 'application/json'
    //     }
    // }).then((res) => {
    //   if (res.ok)
    //     res.json().then((val) => {
    //       updateMap(val.map);
    //     })
    // })
    // },
    //   [props.first]
    // );

    // return (
    //   <div className="App">
    //     <WorldDisplay map={map} ready={Object.keys(map).length !== 0} />
    //   </div>
    // );
}

function Error(props) {
    if (props.message.length !== 0) {
        return <div><p>{props.message}</p></div>
    }
    return <div></div>
}

export default App;
