/**
 * @param {string} s
 * @return {number}
 */
var scoreOfString = function(s) {
    if (s.length === 0)
        return 0;
    if (s.length === 1)
        return s.charCodeAt(0);
    let result = 0;
    for (let i = 0; i < s.length - 1; i++) {
        result += Math.abs(s.charCodeAt(i) - s.charCodeAt(i + 1));
    }
    return result;
};


console.log(scoreOfString("hello"))