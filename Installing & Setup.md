# Installation

##  Install Node.js:
  - Download and install Node.js from the official website: https://nodejs.org/en/download/
  - npm (Node Package Manager) will be installed along with Node.js.

## Clone the Bworks App repository:

`git clone https://github.com/vakhil-98/Bworks.git`

`cd Bworks`

## Set up the Flask backend:
- Navigate to the Bworks `/Services`directory:
    
    `cd Services`
    
- Install Flask and other dependencies:
    
    `pip install -r requirements.txt`
    
- Create a `.env` file in the backend directory and add any sensitive data, such as database credentials, API keys, etc.:

  `EMAIL=xxxx@gmail.com`

  `PASSWORD=xxxx`

  Required fields 

## [Download Microsoft SQL Server 2022 Developer](https://www.microsoft.com/en-us/sql-server/sql-server-downloads)
![image](https://github.com/vakhil-98/Bworks/assets/129634823/897c9bb7-f83a-4c11-9364-e1284af92c87)

## [Download SSMS and setup](https://aka.ms/ssmsfullsetup)
![image](https://github.com/vakhil-98/Bworks/assets/129634823/b886994e-ed35-4037-8a97-9b0da0c619d6)

- Start SSMS and run these queries.

[bicycle.sql](https://github.com/vakhil-98/Bworks/blob/main/SSMS/bicycle.sql) 

![image](https://github.com/DemonXslayer47/Bworks-1/assets/129634823/3086a448-c2ec-48c6-ab43-41a5dd998ad2)

[users.sql](https://github.com/vakhil-98/Bworks/blob/main/SSMS/users.sql) 

![image](https://github.com/DemonXslayer47/Bworks-1/assets/129634823/65a7d1ca-8fdb-4499-95cd-3f3f0c476b77)

[Transaction.sql](https://github.com/vakhil-98/Bworks/blob/main/SSMS/Transaction.sql)

![image](https://github.com/DemonXslayer47/Bworks-1/assets/129634823/365198ec-7b24-4145-8784-62891e53b7cb)

# Setup

## Set up the Angular frontend:
- Navigate to the Bworks\UI\bworks\src\app:
- Install Angular CLI (if not already installed):
    
    `npm install -g @angular/cli`
    
- Install frontend dependencies:
    
    `npm install node-modules --save`

## Run the Angular app:
    
    `ng serve`

Open your browser and navigate to http://localhost:4200 to see the Bworks App in action

## Run the Python app:

`cd .\Services\`

`python app.py`

Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000/), to see the Bworks App in action
