### Installation and Setup

##  Install Node.js and npm:
  - Download and install Node.js from the official website: https://nodejs.org/en/download/
  - npm (Node Package Manager) will be installed along with Node.js.

## Clone the Bworks App repository:
  + git clone https://github.com/vakhil-98/Bworks.git
  cd Bworks

## Set up the Flask backend:
- Navigate to the Bworks `/Services`directory:
    
    `cd Services`
    
- Install Flask and other dependencies:
    
    `pip install -r requirements.txt`
    
- Create a `.env` file in the backend directory and add any sensitive data, such as database credentials, API keys, etc.:

  `EMAIL=xxxx@gmail.com`

  `PASSWORD=xxxx`

  Required fields 

## Run the Flask development server:
`python app.py`

## [Download Microsoft SQL Server 2022 Developer](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)

## [Download SSMS and setup](https://aka.ms/ssmsfullsetup)

- Start SSMS and run these queries.
[bicycle.sql](https://github.com/vakhil-98/Bworks/blob/main/SSMS/bicycle.sql)
[users.sql](https://github.com/vakhil-98/Bworks/blob/main/SSMS/users.sql)
[Transaction.sql](https://github.com/vakhil-98/Bworks/blob/main/SSMS/Transaction.sql)

## Set up the Angular frontend:
- Navigate to the Bworks\UI\bworks\src\app:
- Install Angular CLI (if not already installed):
    
    `npm install -g @angular/cli`
    
- Install frontend dependencies:
    
    `npm install node-modules --save`

## Run the Angular app:
    
    `ng serve`

Open your browser and navigate to http://localhost:4200 to see the Bworks App in action