# Cloud Computing Project: A Music Recommender Chatbot
## Information:
BotID: t.me/LbBo_bot
BotName: LBBo
Members: Liu Bo 23450274
Job division: I did this project on my own. I’m in Group P. Please note that the other student in Group P took a year off from school, and he didn’t contribute to this project at all.
## Introduction: 	
The objective of this bot is to offer high-quality, personalized music recommendations, enabling users to discover new artists, songs, and genres. 
This project is a Telegram bot that is hosted on the AWS cloud Linux infrastructure, using docker and git techniques to accomplish version control and deployment, and connected to a remote db4free database. Leveraging the power of the ChatGPT API, this bot is capable of offering music recommendations based on user queries in natural language and context.
Integrated with Telegram, the bot engages in conversations with users to understand their music preferences and tastes. It is very easy to use, just type ‘/hello’ to see what it can do, and talk to the bot like talking to a friend to get music recommendations.
## Implementations:
Technologies Used:
### Python Programming: 
The application is developed using the Python programming language. Libraries used in this project include mysql-connector-python to link to databases, configparser to read from config.ini, telegram-python-bot to implement bot behaviors, requests to receive messages from telegram.
### db4free Remote Database: 
The db4free remote database was chosen to store song information and their occurrence count according to user queries and ChatGPT replies. It provides a reliable and accessible storage solution for the application's data.
### ChatGPT API: 
The ChatGPT API is utilized to leverage natural language processing capabilities for the chatbot. It enables the bot to understand and generate responses based on user input and context.
GitHub for Version Control: GitHub is employed for version control and code synchronization. It allows me to manage code changes, and maintain a history of revisions.
### Docker for Consistent Deployment Environment: 
Docker technology is used to ensure consistent deployment environments across different systems. Docker allows the packaging of the application and its dependencies into a container that can be deployed on various platforms.
### AWS Free Ubuntu Server: 
The application is deployed on a free Ubuntu server hosted on AWS. This server provides the necessary infrastructure for hosting and accessing the application at any time.
Implementation Steps:
### a. Database Integration:
1.	Sign up and get free usage from db4free.
2.	Establish a connection to the db4free remote database.
3.	Design and create tables to store song information and occurrence count.
4.	Implement SQL queries to insert, retrieve, and update data in the database in chatbot handlers.
5.	Inspect data from website and monitor database performance when necessary
### b. ChatGPT Integration:
1.	Get GPT API token from HKBU ChatGPT 3.5.
2.	Implement code to send user queries to the API and receive intelligent responses.
### c. Python Development:
1.	Use telegram API Updater, CommandHandler, MessageHandler, Filters, CallbackContext to send, receive, dispatch and handle requests.
2.	Write ChatGPT handler to deal with requests and context, make sure it returns the music list recommended.
### d. Version Control with GitHub:
1.	Create a GitHub repository to manage the project's source code.
2.	Create a local repository and link to remote repository.
3.	Regularly commit changes and push, marking all the changes and comments.
### e. Docker Containerization:
1.	Make sure the project is ok on local machine to ensure functionality, performance, and reliability.
2.	Write dockerfile and requirements.txt to define a container.
3.	Package the application and its dependencies into a Docker container.
4.	Use docker build and docker run to test functions in local machine.
5.	Publish this docker image and pull the image from cloud server.
### f. Testing and Deployment on AWS:
1.	Sign up and get free usage, then create an AWS free Ubuntu server instance.
2.	Install docker from command line on AWS server.
3.	Deploy the Docker container on the server, use docker run to start it.
4.	Access the bot through telegram at any time. Have fun! 

The Music Recommendation Telegram Bot has been successfully implemented using a combination of technologies. The db4free remote database stores user queries and song information, while the ChatGPT API enables natural language processing capabilities. Python programming, GitHub for version control, Docker for consistent deployment environments, and the AWS free Ubuntu server for hosting complete the technical implementation. The resulting bot can provide personalized music recommendations based on user input and context, enhancing the user's music exploration experience.
