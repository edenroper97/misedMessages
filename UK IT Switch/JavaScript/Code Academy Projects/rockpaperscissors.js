console.log('hi');

//putting input from the user 
const userChoice = userInput => {
  userInput = userInput.toLowerCase();
  if(userInput === 'rock' || userInput === 'paper' || userInput === 'scissors') {
    return userInput;
  } else {
    console.log('Error!');
  }
};

// randomising number and assigning to possibility to generate random computer choice 
const computerChoice = () => {
  const randomNumber = Math.floor(Math.random() * 3);
  switch (randomNumber) {
    case 0:
      return 'rock';
    case 1:
      return 'paper';
    case 2:
      return 'scissors';
  }
};

console.log(computerChoice());
//detrmining winner with possible outcomes

function determineWinner(userChoice, computerChoice){
  if (userChoice === computerChoice) {
    return 'The game is a tie!';
  } else {
    if (userChoice === 'rock'){
      if(computerChoice === 'paper'){
        return 'The computer won!';
      } else {
        return 'You won!';
      }
    }
    if (userChoice === 'paper'){
      if (computerChoice === 'rock'){
        return 'You won!';
      } else {
        return 'The computer won!';
      }
    }
  }
}

//checking winner with posibilities inputted
console.log(determineWinner('paper', 'scissors')); // prints something like 'The computer won!'
console.log(determineWinner('paper', 'paper')); // prints something like 'The game is a tie!'
console.log(determineWinner('paper', 'rock')); // prints something like 'The user won!'


function playGame(){
const userInput = userChoice('rock');
const computerInput = computerChoice();
console.log('You threw:' + userInput);
console.log('The computer threw:' + computerInput);
console.log(determineWinner(userInput, computerInput));
};

playGame();


