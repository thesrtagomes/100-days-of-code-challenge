const main = document.querySelector('main')
const player1Container = document.querySelector('#player_1')
const player2Container = document.querySelector('#player_2')

let player1;
let player2;

function playRock(){
    const gamePhase = main.getAttribute('data-game-phase')

    if (gamePhase === 'player_1_turn') {
        player1 = 'R'
        main.setAttribute('data-game-phase', 'player_2_turn')
    } else if (gamePhase === 'player_2_turn') {
        player2 = 'R'
        main.setAttribute('data-game-phase', 'compare_result')
    }

    evaluatePhase()
}
function playPaper(){
    const gamePhase = main.getAttribute('data-game-phase')

    if (gamePhase === 'player_1_turn') {
        player1 = 'P'
        main.setAttribute('data-game-phase', 'player_2_turn')
    } else if (gamePhase === 'player_2_turn') {
        player2 = 'P'
        main.setAttribute('data-game-phase', 'compare_result')
    }
 
    evaluatePhase()
}
function playScissors(){
    const gamePhase = main.getAttribute('data-game-phase')

    if (gamePhase === 'player_1_turn') {
        player1 = 'S'
        main.setAttribute('data-game-phase', 'player_2_turn')
    } else if (gamePhase === 'player_2_turn') {
        player2 = 'S'
        main.setAttribute('data-game-phase', 'compare_result')
    }

    evaluatePhase()
}

function whatWinsAgainst(thing) {
    if (thing === 'R') {
        return 'P'
    } else if (thing === 'P') {
        return 'S'
    } else if (thing === 'S') {
        return 'R'
    }
}

function showPlayer1Thing() {
    player1Container.style.opacity = 1;
    if (player1 === 'R') {
        document.querySelector('#player_1_rock').style.opacity = 1;
        document.querySelector('#player_1_paper').style.opacity = 0;
        document.querySelector('#player_1_scissors').style.opacity = 0;
    } else if (player1 === 'P') {
        document.querySelector('#player_1_rock').style.opacity = 0;
        document.querySelector('#player_1_paper').style.opacity = 1;
        document.querySelector('#player_1_scissors').style.opacity = 0;
    } else if (player1 === 'S') {
        document.querySelector('#player_1_rock').style.opacity = 0;
        document.querySelector('#player_1_paper').style.opacity = 0;
        document.querySelector('#player_1_scissors').style.opacity = 1;
    }
}

function showPlayer2Thing() {
    player2Container.style.opacity = 1;
    if (player2 === 'R') {
        document.querySelector('#player_2_rock').style.opacity = 1;
        document.querySelector('#player_2_paper').style.opacity = 0;
        document.querySelector('#player_2_scissors').style.opacity = 0;
    } else if (player2 === 'P') {
        document.querySelector('#player_2_rock').style.opacity = 0;
        document.querySelector('#player_2_paper').style.opacity = 1;
        document.querySelector('#player_2_scissors').style.opacity = 0;
    } else if (player2 === 'S') {
        document.querySelector('#player_2_rock').style.opacity = 0;
        document.querySelector('#player_2_paper').style.opacity = 0;
        document.querySelector('#player_2_scissors').style.opacity = 1;
    }
}

function evaluatePhase() {
    const gamePhase = main.getAttribute('data-game-phase')

    if (gamePhase === 'player_1_turn') {
        player2Container.style.opacity = 0;
        player1Container.style.opacity = 1;
    } else if (gamePhase === 'player_2_turn') {
        player1Container.style.opacity = 0;
        player2Container.style.opacity = 1;
    } else if (gamePhase === 'compare_result') {
        showPlayer1Thing();
        showPlayer2Thing();

        if (player1 === whatWinsAgainst(player2)) {
            document.querySelector('#winner_message').textContent = 'Player 1 WINS 🚀!'
        }
        else if (player2 === whatWinsAgainst(player1)) {
            document.querySelector('#winner_message').textContent = 'Player 2 WINS 🚀!'
        }
        else {
            document.querySelector('#winner_message').textContent = 'Draw 😢'
        }
    }
}

evaluatePhase()

//eu te amo