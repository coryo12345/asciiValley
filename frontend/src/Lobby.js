import React, { useEffect, useState } from 'react';

function Lobby(props) {

    const [settings, setSettings] = useState({});

    useEffect(() => {
        fetch(`/session/get/${props.code}/`, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        }).then((res) => {
            if (res.ok)
                res.json().then((data) => {
                    // {code: 0, settings: {}}
                    setSettings(data.settings);
                })
        })
    },
        [true]
    );

    console.log(settings.world);

    return (
        <div>
            <p>Settings:</p>
            <p>World: {settings.world}</p>
            <button onClick={props.leave} >Leave Game</button>
        </div>
    );
}

export default Lobby;
