const jsonfile =require('jsonfile');
const moment = require('moment');
const simpleGit = require('simple-git');
const FILE_PATH='./data.json';
const random = require('random');
const makeCommit  = n =>{
    if(n===0) return simpleGit.push();
 
    for (let i = 0; i < 54; i++) {
        for (let j = 0; j < 6; j++) {
            const DATE = moment().subtract(2,'y').add(1,'d').add(i,'w').add(j,'d').format();
            const date={
                date:DATE
            }
            console.log(DATE);
            
            jsonfile.writeFile(FILE_PATH,date,()=>{
                simpleGit().add([FILE_PATH]).commit(DATE,{'--date': DATE},makeCommit.bind(this,--n)).push();
            });
          }
      }
    


    
}

makeCommit(1)




