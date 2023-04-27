function wordTracker(inputArr) {
    let wordsToTrack = inputArr.shift().split(" ");
// Shift - takes out the first element of array
  
    let words = {};
  
// filter all words same as the given word
    for (const word of wordsToTrack) {
      let count = inputArr.filter((w) => w === word).length;
      words[word] = count;
    }
  
    // Object to array + Sorting by value (can't sort objects)
     let sortedWords = Object.entries(words).sort((aWord, bWord) => {
      let [_aName, aCount] = aWord;
      let [_bName, bCount] = bWord;
  
      return bCount - aCount;
    });
  
    for (const [word, count] of sortedWords) {
      console.log(`${word} - ${count}`);
    }
  }  
  
  wordTracker([
    "this sentence",
    "In",
    "this",
    "sentence",
    "you",
    "have",
    "to",
    "count",
    "the",
    "occurrences",
    "of",
    "the",
    "words",
    "this",
    "and",
    "sentence",
    "because",
    "this",
    "is",
    "your",
    "task",
  ]);
  wordTracker([
    "is the",
    "first",
    "sentence",
    "Here",
    "is",
    "another",
    "the",
    "And",
    "finally",
    "the",
    "the",
    "sentence",
  ]);