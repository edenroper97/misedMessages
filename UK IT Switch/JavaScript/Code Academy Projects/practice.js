//Create a function colorMessage() that takes 2 string arguments, favoriteColor and shirtColor.

//If the value of favoriteColor is the same as the value of shirtColor return the string 'The shirt is your favorite color!'.

//If not, return the string 'That is a nice color.'

//Feel free to test your code under the function definition.

// Create function below
const colorMessage = (favouriteColor, shirtColor) => {
    if (favouriteColor === shirtColor){
      console.log('The shirt is your favourite color!')
      }else {
        console.log('That is a nice color.')
      }
    }
  
  colorMessage('blue','blue')

  //create a fucntion which tells you how many digits the number has 
  //if negative include in else 

// Create function here 
numberDigits = (x) => {
    if (x > 0 && x < 9){
      return 'One digit: ' + x
    } else if (x > 10 && x < 99){
      return 'Two digits: ' + x
    } else {
      return 'The number is: ' + x
    }
  
  };
  
  console.log(numberDigits(97))