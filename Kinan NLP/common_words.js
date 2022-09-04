const fs = require("fs");

let rawdata = fs.readFileSync("NLP.json");
let nlpRepos = JSON.parse(rawdata);

console.log(nlpRepos);
