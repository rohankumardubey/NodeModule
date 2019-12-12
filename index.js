const jsonfile =require('jsonfile');
const moment = require('moment');
const simpleGit = require('simple-git');
const FILE_PATH='./data.json';
const random = require('random');
const makeCommit  = n =>{
    if(n===0) return simpleGit.push();

    const DATE = moment().subtract(3,'y').add(x,'w').add(y,'d').format();

    // const date={
    //     date:DATE
    // }
    console.log(DATE);
    // jsonfile.writeFile(FILE_PATH,date,()=>{
    //     simpleGit().add([FILE_PATH]).commit(DATE,{'--date': DATE},makeCommit.bind(this,--n));
    // });
    
}

makeCommit(1000)




