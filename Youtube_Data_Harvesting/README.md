**NAME**: KAVIPRIYA DEVARAJ

**BATCH**: DTM7

**DOMAIN**: DATA SCIENCE

**PROJECT NAME**: YouTube-Data-Harvesting-and-Warehousing-using-SQL-MongoDB-and-Streamlit.

**PROBLEM STATEMENT**: The problem statement is to create a Streamlit application that allows users to access and analyze data from multiple YouTube channels. The application should have the following features:
   Ability to input a YouTube channel ID and retrieve all the relevant data (Channel name, subscribers, total video count, playlist ID, video ID, likes, dislikes, comments of each video) using Google API.
   Option to store the data in a MongoDB database as a data lake.
   Ability to collect data for up to 10 different YouTube channels and store them in the data lake by clicking a button.
   Option to select a channel name and migrate its data from the data lake to a SQL database as tables.
   Ability to search and retrieve data from the SQL database using different search options, including joining tables to get channel details.

**SET UP A STREAMLIT APP**: Streamlit is a great choice for building data visualization and analysis tools quickly and easily. 
   We can use Streamlit to create a simple UI where users can enter a YouTube channel ID, view the channel details, and select channels to migrate to the data warehouse.

**CONNECT TO THE YOUTUBE API**: We'll need to use the YouTube API to retrieve channel and video data. 
   We can use the Google API client library for Python to make requests to the API.

**STORE DATA IN A MONGODB DATA LAKE**: Once we retrieve the data from the YouTube API, we can store it in a MongoDB data lake. 
   MongoDB is a great choice for a data lake because it can handle unstructured and semi-structured data easily.

**MIGRATE DATA TO A SQL DATA WAREHOUSE**: After we've collected data from multiple channels, we can migrate it to a SQL data warehouse. 
   We can use a SQL database such as MySQL or PostgreSQL for this.

**QUERY THE SQL DATA WAREHOUSE**: We can use SQL queries to join the tables in the SQL data warehouse and retrieve data for specific channels based on user input. 
   We can use a Python SQL library such as SQLAlchemy to interact with the SQL database.
   
**DISPLAY DATA IN THE STREAMLIT APP**: Finally, we can display the retrieved data in the Streamlit app. 
   We can use Streamlit's data visualization features to create charts and graphs to help users analyze the data.

**Overall, this approach involves building a simple UI with Streamlit, retrieving data from the YouTube API, storing it in a MongoDB data lake, migrating it to a SQL data warehouse, querying the data warehouse with SQL, and displaying the data in the Streamlit app.**
   
**DEMO VIDEO URL**: 
 






