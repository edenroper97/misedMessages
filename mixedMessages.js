//Creat a number to assign to the random joke message 


//tell me a joke... jokes... answers
//can we get the right answer to come up?
const collectiveJokes = {
    jokeQuestion:['Can you tell me a joke?', 'Got any new jokes for me?', 'How rubish are your jokes today?'],
    dadJokes: ["How did I know my girlfriend thought I was invading her privacy?", 
        "Watch what you say around the egg whites. ",
        "What do you call a sheep who can sing and dance?", 
        "Dogs can't operate MRI machines.", 
        "Why can't dinosaurs clap their hands? Because they're extinct.",
        "Dogs can't operate MRI machines.",
        "What do you call a dog who meditates?",
        "Which vegetable has the best kung fu?"],
    punchLine: ['She wrote about it in her diary.', "They can't take a yolk.",'Lady Ba Ba.', 'But catscan.', 'Aware wolf.', 'Brocc-Lee']

}


// store jokes in an array 
let tellMeAJoke = []

let generateRandomNum = Math.floor(Math.random() * 8)

let popUpJoke = ''

//generate a random question, joke an punchline 

switch(generateRandomNum){
case 1: 
  console.log(collectiveJokes['jokeQuestion'][0])
  console.log(collectiveJokes['dadJokes'][0])
  console.log(collectiveJokes['punchLine'][0])
  break

case 2:
    console.log(collectiveJokes['jokeQuestion'][1])
    console.log(collectiveJokes['dadJokes'][1])
    console.log(collectiveJokes['punchLine'][1])
    break

case 3:
    console.log(collectiveJokes['jokeQuestion'][2])
    console.log(collectiveJokes['dadJokes'][2])
    console.log(collectiveJokes['punchLine'][2])
    break

case 4:
    console.log(collectiveJokes['jokeQuestion'][0])
    console.log(collectiveJokes['dadJokes'][3])
    console.log(collectiveJokes['punchLine'][3])
    break

case 5:
    console.log(collectiveJokes['jokeQuestion'][1])
    console.log(collectiveJokes['dadJokes'][4])
    console.log(collectiveJokes['punchLine'][4])
    break

case 6:
    console.log(collectiveJokes['jokeQuestion'][2])
    console.log(collectiveJokes['dadJokes'][5])
    console.log(collectiveJokes['punchLine'][5])
    break

case 7:
    console.log(collectiveJokes['jokeQuestion'][0])
    console.log(collectiveJokes['dadJokes'][6])
    console.log(collectiveJokes['punchLine'][6])
    break

    default:
    console.log("Sorry dude, all out of Jokes today!")
}

console.log(popUpJoke)