//Creat a number to assign to the random joke message 

//User Question to the console
const tellMeAJoke = "Can you tell me a joke?"
console.log(tellMeAJoke)


let generateRandomNum = Math.floor(Math.random() * 5)

let popUpJoke = ''

switch(generateRandomNum){
  case 1: 
  popUpJoke = "How did I know my girlfriend thought I was invading her privacy? She wrote about it in her diary."
  break 
  case 2:
  popUpJoke = "Watch what you say around the egg whites. They can't take a yolk."
  break 
  case 3: 
  popUpJoke = "What do you call a sheep who can sing and dance? Lady Ba Ba."
  break
  case 4:
  popUpJoke = "Why can't dinosaurs clap their hands? Because they're extinct."
  break
  case 5:
  popUpJoke = "Dogs can't operate MRI machines. But catscan."
  break
  case 6: 
  popUpJoke = "What do you call a dog who meditates? Aware wolf."
  break
  case 7:
  popUpJoke = "Which vegetable has the best kung fu? Broc-lee."
  break
}

console.log(popUpJoke)