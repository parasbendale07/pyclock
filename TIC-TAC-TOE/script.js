document.addEventListener("DOMContentLoaded", () => {
    const cells = document.querySelectorAll(".cell");
    const turnIndicator = document.getElementById("turn-indicator");
    const winnerMessage = document.getElementById("winner-message");
    const restartBtn = document.getElementById("restart-btn");

    let board = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ];
    let currentPlayer = "X";
    let gameOver = false;

    function updateTurnIndicator() {
        turnIndicator.textContent = `Turn: ${currentPlayer}`;
    }

    function checkWinner() {
        // Check rows & columns
        for (let i = 0; i < 3; i++) {
            if (board[i][0] && board[i][0] === board[i][1] && board[i][1] === board[i][2])
                return board[i][0];
            if (board[0][i] && board[0][i] === board[1][i] && board[1][i] === board[2][i])
                return board[0][i];
        }
        // Check diagonals
        if (board[0][0] && board[0][0] === board[1][1] && board[1][1] === board[2][2])
            return board[0][0];
        if (board[0][2] && board[0][2] === board[1][1] && board[1][1] === board[2][0])
            return board[0][2];
        // Check draw
        if (board.flat().every(cell => cell !== "")) return "Draw";
        return null;
    }

    function handleClick(e) {
        if (gameOver) return;

        const row = parseInt(e.target.dataset.row);
        const col = parseInt(e.target.dataset.col);

        if (board[row][col] !== "") return;

        board[row][col] = currentPlayer;
        e.target.textContent = currentPlayer;

        const winner = checkWinner();
        if (winner) {
            gameOver = true;
            winnerMessage.textContent = winner === "Draw" ? "It's a Draw!" : `Winner: ${winner}`;
            return;
        }

        currentPlayer = currentPlayer === "X" ? "O" : "X";
        updateTurnIndicator();
    }

    cells.forEach(cell => cell.addEventListener("click", handleClick));

    restartBtn.addEventListener("click", () => {
        board = [
            ["", "", ""],
            ["", "", ""],
            ["", "", ""]
        ];
        cells.forEach(cell => cell.textContent = "");
        currentPlayer = "X";
        gameOver = false;
        winnerMessage.textContent = "";
        updateTurnIndicator();
    });
});
