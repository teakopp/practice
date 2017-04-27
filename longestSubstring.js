/**
 * @param {string} s
 * @return {number}
 */
let s = "pwwkew"
const lengthOfLongestSubstring = (s) => {
  let letterDictionary = {}
  let result = 0;
  let count = 0;


  for(i=0; i < s.length; i++){
    let letter = s[i]
    let next = s[i+1]
    let previous = s[i-1]

    if(letter in letterDictionary){
      i = letterDictionary[letter] + 1
      letter = s[i]
      letterDictionary = {}
      letterDictionary[letter] = i
      count = 1

    }
    else{
      letterDictionary[letter] = i;
      count += 1
    }

    if(result < count){
      result = count;
    }
  }
  console.log(result);
    return result

};

lengthOfLongestSubstring(s);
