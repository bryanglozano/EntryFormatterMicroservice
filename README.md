Entry Formatter Microservice


Description: This microservice formats entry data before it is stored by the data storage microservice.

It ensures:
• entry fields are formatted consistently
• titles and categories are converted to lowercase
• dates are converted to a consistent format

The microservice communicates using text files, not direct function calls.
The test file simulates a main program using the microservice.
Communication Contract

This is text-file based communication, with these files both containing JSON formatted text: 

Request file: pipe/format_request.txt
Response file: pipe/format_response.txt

How to request formatting:

1) Open: pipe/format_request.txt

2) Write a JSON object and save the file.

Request format:

{
 "action": "format",
 "entry": {
   "date": "3/11/26",
   "title": "Morning Run",
   "category": "Fitness",
   "notes": "Ran 30 minutes"
 }
}
Example request
Copy code
Json
{
 "action": "format",
 "entry": {
   "date": "3/11/26",
   "title": "Morning Run",
   "category": "Fitness",
   "notes": "Ran 30 minutes"
 }
}

How to receive formatted data:

The microservice writes a JSON response to: pipe/format_response.txt

Response format:

{
 "ok": true,
 "formatted_entry": {
   "date": "2026-03-11",
   "title": "morning run",
   "category": "fitness",
   "notes": "Ran 30 minutes"
 }
}

Example invalid request response:

{
 "ok": false,
 "error": "invalid_action"
}


How to run:

1) Clone the repository.
2) Make sure you are in the repository root folder (do not run inside /src, /tests, or /pipe).
3) Start the microservice
   
Linux / Mac: python3 src/microservice4.py
Windows: python src\microservice4.py

Output should look similar to:

Entry Formatter Microservice running...
Request file: pipe\format_request.txt
Response file: pipe\format_response.txt

4) Run the test client
5) Open a second terminal and run:
6) 
Linux / Mac:python3 tests/test_client.py
Windows: python tests\test_client.py

Output should look similar to:

FORMAT -> {'ok': True, 'formatted_entry': {'date': '2026-03-11', 'title': 'morning run', 'category': 'fitness', 'notes': 'Ran 30 minutes'}}

Important Notes for Windows:

• Use \ in file paths
• Make sure you are running commands from the project root folder
• If python does not work, try:

py src\microservice4.py
py tests\test_client.py
