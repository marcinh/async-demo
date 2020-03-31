DemoClient simulates real client behaviour connected to backend server.
It provides make_business() method which mocks sending post request to the server and is equivalent of creating business transaction - 
returns Response with 200 code if transaction was taken to process or 400 if provided business id is duplicated.<br/>
DemoClient asynchronously accepts and confirms transactions with JSONs using event on_message:<br/>
{'messageType': 'ACCEPT', 'businessId': 'alphanumeric', 'id': number}<br/>
{'messageType': 'CONFIRM', 'id': number}<br/>
Those messages can arrive in random order and time

Client &emsp;&emsp;&emsp;&emsp;&emsp;&emsp; Server

POST(businessId)<br/>
------------------------------------------------->
<br/>OK<br/>
<------------------------------------------------
<br/><br/>ACCEPTED(businessId, id)<br/>
<------------------------------------------------
<br/>CONFIRMED(id)<br/>
<------------------------------------------------


<b>Task:</b><br/>
Provide exact timings of arrival of accept and confirm message per business id (starting count after making business transaction)