const getSleepHours = day => {
    if (day === 'Monday') {
      return 8;
    } else if (day === 'Tuesday') {
      return 5;
    } else if (day === 'Wednesday') {
      return 10;
    } else if (day === 'Thursday') {
      return 7;
    } else if (day === 'Friday') {
      return 3;
    } else if (day === 'Saturday') {
      return 3;
    } else if (day === 'Sunday') {
      return 16;
    }
  
  };
  const getActualSleepHours = () => 
    getSleepHours('Monday') + 
    getSleepHours('Tuesday') + 
    getSleepHours('Wednesday') + 
    getSleepHours('Thursday') + 
    getSleepHours('Friday') + 
    getSleepHours('Saturday') + 
    getSleepHours('Sunday');
  
  const getIdealSleepHours = () => {
   const idealHours = 7;
   return idealHours * 7;
  };
  
  console.log(getActualSleepHours())
  console.log(getIdealSleepHours())
  
  const calculateSleepDebt = () => {
    const actualSleepHours = getActualSleepHours();
    const idealSleepHours = getIdealSleepHours();
  
    if (actualSleepHours < idealSleepHours) {
    console.log('You got ' + (idealSleepHours - actualSleepHours) + ' hour(s) less sleep than you needed this week. Get some rest.');
  } else if (actualSleepHours > idealSleepHours) {
      console.log('You got ' + (idealSleepHours - actualSleepHours) + ' hour(s) more sleep than you needed this week. Well done champ!');
    } else {
      console.log('You got ' + (idealSleepHours - actualSleepHours) + ' hour(s) less whuch means you got the exact right amount!');
    }
  };
  
  // Call the function to execute it
  calculateSleepDebt();