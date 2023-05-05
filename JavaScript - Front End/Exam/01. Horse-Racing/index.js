function horseRace(input) {
    let horses = input.shift().split('|');
    let finish = false;
    
    while (!finish) {
      let line = input.shift().split(' ');
      let command = line[0];
      
      if (command === 'Finish') {
        finish = true;
        break;
      }
      
        if (command === 'Retake') {
            let overtakingHorse = line[1];
            let overtakenHorse = line[2];
            let overtakingIndex = horses.indexOf(overtakingHorse);
            let overtakenIndex = horses.indexOf(overtakenHorse);
        
            if (overtakingIndex < overtakenIndex) {
                [horses[overtakingIndex], horses[overtakenIndex]] = [horses[overtakenIndex], horses[overtakingIndex]];
                console.log(`${overtakingHorse} retakes ${overtakenHorse}.`);
            }
        } 
        else if (command === 'Trouble') {
            let horse = line[1];
            let index = horses.indexOf(horse);
        
            if (index !== 0) {
                horses.splice(index, 1);
                horses.splice(index - 1, 0, horse);
                console.log(`Trouble for ${horse} - drops one position.`);
            }
        } 
        else if (command === 'Rage') {
            let horse = line[1];
            let index = horses.indexOf(horse);

            if (index === 0){
                break
            }
            else if (index + 2 > horses.length) {
                horses.splice(index, 1);
                horses.splice(horses.length, 0, horse);
            } 
            else{
                horses.splice(index, 1);
                horses.splice(index + 2, 0, horse);
            }
            console.log(`${horse} rages 2 positions ahead.`);
        }
        else if (command === 'Miracle') {
            let horse = horses[0];
            horses.shift();
            horses.push(horse);
            console.log(`What a miracle - ${horse} becomes first.`);
        }
    }

    console.log(`${horses.join('->')}\nThe winner is: ${horses[horses.length - 1]}`);
}


// horseRace([
//     'Bella|Alexia|Sugar',
//     'Retake Alexia Sugar',
//     'Rage Bella',
//     'Trouble Bella',
//     'Finish'
// ]);

// horseRace([
//     'Onyx|Domino|Sugar|Fiona',
//     'Trouble Onyx',
//     'Retake Onyx Sugar',
//     'Rage Domino',
//     'Miracle',
//     'Finish'
// ]);

// horseRace([
//     'Fancy|Lilly',
//     'Retake Lilly Fancy',
//     'Trouble Lilly',
//     'Trouble Lilly',
//     'Finish',
//     'Rage Lilly'
// ]);

horseRace([
    'Onyx|Domino|Sugar|Fiona',
    // 'Trouble Fiona',
    'Retake Fiona Onyx',
    // 'Rage Onyx',
    // 'Miracle',
    'Finish'
]);