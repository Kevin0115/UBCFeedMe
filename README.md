# UBC Feed Me
*Free Food Finder for UBC Students - Created at nwHacks 2017*

### The Team
- Alex Driedger
- Mathew MacDougall
- Kevin Choi
- Daniel Choi
- Jagjot Jhajj

### How It Works

#### Step 1: Get Pages
Using the Facebook Graph API, get the Facebook Page of every UBC club

#### Step 2: Get Events
Using the Facebook Graph API, get the events of over club

#### Step 3: Filter Events
Keyword search the description of each event for phrases indicating free food (eg. Refreshments will be provided) and remove all events with phrases indicating the event is paid (eg. Tickets cost).

#### Step 4: Process & Store
Events that pass filtering as processed and inserted into a MongoDB database

#### Step 5: Present
Present the data to users in an appropiate fashion. For this project, we created a web app.
