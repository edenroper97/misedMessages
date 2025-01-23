//Setting the var as my age number
let myAge = 8;

//this is the value of early years 
let earlyYears = 2;

earlyYears *= 10.5

//we have accounted for the 2 earlier years... so we took them off
var laterYears = myAge -= 2

//multiply the later years by 4 
laterYears *= 4 

//check work point 

console.log(earlyYears)
console.log(laterYears)

//add them together for my age in dog years
myAgeInDogYears = earlyYears += laterYears

console.log(myAgeInDogYears)

//write name in string... assign... lowercase

let myName = 'Eden Roper'.toLowerCase();
console.log(myName);

//concatenate my name and dog age with interpolation 

console.log(`My name is ${myName}. I am ${myAge} years old in human years which is ${myAgeInDogYears} years old in dog years.`);



