const team = {
    _players: [
      {firstName: 'Kobbie', lastName:'Mainoo', age: 19},
      {firstName: 'Cristiano', lastName: 'Ronaldo', age: 37},
      {firstName: 'Alejandro', lastName: 'Garnacho', age: 20}
    ],
    _games: [
      {opponent: 'Manchester City', teamPoints: 3, opponentPoints: 0},
      {opponent:'Liverpool', teamPoints: 5, opponentPoints: 1},
      {opponent: 'Arsenal', teamPoints: 8, opponentPoints: 2}
    ],
    get players(){
      return this._players;
    },
    get games(){
    return this._games;
    },
    addPlayer(newFirstName, newLastName, newAge){
      let player = {
        firstName: newFirstName,
        laatName:  newLastName,
        newAge: newAge
      };
      this.players.push(player);
    },
    addGame(newOpponent, newTeamPoints, newOpponentPoins){
      let game = {
        opponent: newOpponent,
        teamPoints: newTeamPoints,
        opponentPoints: newOpponentPoins
     };
     this.games.push(game);
    }
  };
  
  team.addPlayer('Ryan','Giggs', 35);
  console.log(team.players);
  
  team.addGame("Tottenham", 10, 0)
  console.log(team.games);
  
  
  