/**
 * @param {string} s
 * @return {number}
 */
let s = "kewwe"
const lengthOfLongestSubstring = (s) => {
  let result = 0;
  let count = 0;
  let letterArray = []

  for(i=0; i < s.length; i++){
    
    if(letterArray.indexOf(s[i]) == -1){
      letterArray.push(s[i])
      count = letterArray.length
    }
    else{
      let index = letterArray.indexOf(s[i])
      letterArray.push(s[i])
      letterArray.splice(0, index + 1)
      count = letterArray.length
    }
    if(result < count){
      result = count;
    }

  }

  return result
};
lengthOfLongestSubstring(s);
