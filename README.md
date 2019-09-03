# HeroloBe

simple message api to receive and send messages

hope you find my code worthy :)
---------------------------------------------------------------------------------
be/readall: reads all message:
GET


write new msg:
POST

parameters:

write message:

"sender":string
 
 "receiver":string
 
 "subject":string
 
 "message":string

 "been_read":boolean (default false)


exmple:
{
 
 "sender":"HeroloTeam@herolo.com",
 
 "receiver":"tomermalovani@gmail.com",
 
 "subject":"good news",
 
 "message":"you got the job!",

 "been_read":"False"

 
}

--------------------------------------------------------------------------
read all unread message:
be/readunread
GET

parameters:query string: name


http://127.0.0.1:8000/be/readunread?name=tomermalovani@gmail.com
-----------------------------------------------------------------------------
read one unread message :
/be/readmsg
parameters:
1.id(message id)

---------------------------------------------------------------------------
delete a message

e/deletemsg

parameters:
1.id
2.applyer(who is trying to delete the message)
