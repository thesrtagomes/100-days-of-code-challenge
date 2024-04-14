const main = document.querySelector('main')
const player1Container = document.querySelector('#player_1')
const player2Container = document.querySelector('#player_2')

const gamePhase = main.getAttribute('data-game-phase')

if (gamePhase === 'player_1_turn') {
    player2Container.style.opacity = 0;
    player1Container.style.opacity = 1;
} else if (gamePhase === 'player_2_turn') {
    player1Container.style.opacity = 0;
    player2Container.style.opacity = 1;
}

//eu te amo