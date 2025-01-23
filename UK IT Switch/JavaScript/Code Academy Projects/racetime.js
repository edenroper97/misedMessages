let raceNumber = Math.floor(Math.random() * 1000);

const registeredEarly = false;

const age = 27;

if (age > 18 && registeredEarly === true)
{
 raceNumber += 1000;
 }

 if (age > 18 && registeredEarly) {
  console.log(`Your race number is ${raceNumber} and you start at 9:30am!`);
 } else if (age > 18 && !registeredEarly) {
  console.log(`Your race number is ${raceNumber += 1000} and your race will start at 11:00am!`);
 } else if (age < 18){
  console.log(`Your race number is ${raceNumber} and your race will start at 12:30pm!`)
  } else {
    console.log('Consult the registration desk.');
  }