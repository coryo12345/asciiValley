
function WorldDisplay(props) {
    if (!props.ready) {
        return (
            <div></div>
        );
    }

    const width = props.map[0].length;
    const height = props.map.length;
    const cellSize = Math.min(window.innerWidth / width, window.innerHeight / height);
    var tiles = [];
    var count = 0;
    for (let r = 0; r < props.map.length; r++) {
        var row = [];
        for (let c = 0; c < props.map[r].length; c++) {
            row.push(
                <div key={count++} style={{ ...styles.cell, width: cellSize, height: cellSize, fontSize: `${cellSize * .8}px` }}>{props.map[r][c]}</div>
            )
        }
        var fullRow = <div key={count++} style={styles.worldrow}>{row}</div>
        tiles.push(fullRow);
    }

    return (
        <div style={styles.worldcontainer}>
            {tiles}
        </div>
    );
}

const styles = {
    worldcontainer: {

    },
    worldrow: {
        display: 'flex',
        flexDirection: 'row',
    },
    cell: {
        textAlign: 'center',
        textAlignVertical: 'center',
    }
}

export default WorldDisplay;