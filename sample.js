const jsonfile =require('jsonfile');
const FILE_PATH = "./data.json";
const moment = require("moment");
const simpleGit = require("simple-git")
const random = require("random");
const makeCommit = n => {
    if(n === 0) simpleGit().push();
    const y = random.int(0,60);
    const DATE = `2022-04-19T14:01:${y}+05:30`;
    const data = {
        data:DATE
    }
    console.log(DATE);
    jsonfile.writeFile(FILE_PATH,data);
    simpleGit().add([FILE_PATH]).commit(DATE,{"--date":DATE},makeCommit.bind(this,--n));    
};
makeCommit(1)