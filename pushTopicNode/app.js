const jsforce = require("jsforce");

const username = '<username>';
const password = '<password>';

const security_token  = '<security_token>';

const connection = new jsforce.Connection();

connection.login(username,password+security_token,(err,res)=>{


    connection.streaming.channel('<channel_path>').subscribe((message)=>{

        console.log(message);

    })

});