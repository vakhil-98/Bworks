The documentation will explain how to use the code, how to install it, and how to contribute to the project.

# Architecture
## BWorks Project Visualization:
Introduction:
The BWorks project is an innovative bicycle donation and buying application that aims to promote sustainable transportation options and make affordable bicycles accessible to those in need. The application allows users to log in and choose between donating or buying a bicycle, thus connecting individuals interested in making a difference in their communities. This documentation provides an overview of the project, technical details, API endpoints, and data model.

Technical Details:
BWorks is developed using Python Flask as a lightweight web framework for the backend API, SQLAlchemy as the Python SQL toolkit and ORM library for database interactions, and Angular for creating the user interface. The project's architecture allows for a seamless integration of frontend and backend components, ensuring a smooth user experience.

API Endpoints:
The project offers several API endpoints to facilitate user interactions. Users can register, view available bicycles, log in to their accounts, perform transactions, retrieve past transactions, and manage data. Each API endpoint is designed to serve specific functionalities, ensuring a well-organized and efficient user experience.

Database Model:
The project adopts a relational database model to store user information, bicycle details, and transaction history. The database consists of three main tables:
Users: This table stores user account information, including name, contact details, email, address, username, and password.
Bicycles: The Bicycles table contains bicycle details, such as bicycle ID, name, and an image representing the bicycle.
Transactions: The Transactions table records user transactions, whether they involve buying or donating a bicycle. Each transaction includes the user's ID, bicycle ID, bicycle number for donation, transaction type, address, contact details, date of donation or purchase, and status.
User Registration:
To register, users provide their personal information, including their full name, contact details, email address, address, desired username, and password. The registration process ensures that all required fields are filled and validates the input data for accuracy.

Bicycle Information:
The API endpoint /bicycle allows users to view the available bicycles for donation or purchase. When accessing this endpoint, the server queries the Bicycles table to retrieve bicycle information and returns a list of bicycle objects, each containing the bicycle ID, name, and an image URL representing the bicycle.
User Login:
Users can log in to their accounts by providing their username and password through the /login API endpoint. The server validates the input data, checks for matching credentials in the Users table, and returns the user's account information upon successful login.
User Transactions:
The /transaction API endpoint enables users to make new transactions, either to buy or donate a bicycle. Users submit transaction details such as user ID, bicycle ID, bicycle number for donation (if applicable), transaction type, address, and contact details. The server validates the input data and records the transaction in the Transactions table.
Past Transactions:
Users can retrieve their past transactions using the /gettransaction API endpoint. The server queries the Transactions table to fetch all past transactions related to the user and returns a list of transaction objects containing the transaction ID, user ID, and bicycle ID for each past transaction.

ETL Operations:
The /etl_bicycles API endpoint is used for Extract, Transform, Load (ETL) operations on bicycle data. The server reads bicycle information from a CSV file named Bicycles.csv and inserts it into the Bicycles table. This ETL process efficiently populates the database with bicycle details.
Data Management:
The /data API endpoint, while currently commented out in the code, potentially handles user data management. If implemented, this endpoint could retrieve user data, including name, email, survey responses, drop-off location, date and time of the survey, bike model, bike color, and bike wheel information.

Conclusion:
In conclusion, the BWorks project offers a user-friendly and effective platform for connecting bicycle donors and buyers. It enables users to make a positive impact in their communities by providing access to sustainable transportation options. As an open-source project, BWorks has the potential for continuous improvement and enhancement, furthering its mission to create a positive impact on society.



Step1: 
![login](https://github.com/vakhil-98/Bworks/assets/129809773/39180e28-0602-455b-8c3c-5f028d8a55d0)

Step2:
![signup](https://github.com/vakhil-98/Bworks/assets/129809773/6db1ce02-631c-4d6d-8e2f-47030b7959ed)

Step3:
![bulk_edit](https://github.com/vakhil-98/Bworks/assets/129809773/dfec7627-1e3e-4dd7-87e9-1b445aaeb53a)

Step4:
![bulk_upload](https://github.com/vakhil-98/Bworks/assets/129809773/cc20f4eb-44d1-4980-8258-31bf21d1ddb4) 




