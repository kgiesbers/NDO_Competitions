## Project description

NDO_Competitions is a project that provides a clear overview of NDO (Nederlandse Danssport Organisatie) competitions.
The current website (scrutineering.org/NDO) for insights into these competitions is not very user-friendly. For example, viewing which competitions a user has entered can be time-consuming.
This project scrapes data from the website, stores it in an SQL database, and makes the results available via an API in JSON format.

Future plans include:
  - (basic)frontend
  - user interface
  - scraping more data (competition date, judge reports etc.)


## Dependencies

Install dependencies with:
pip install fastapi uvicorn sqlalchemy beautifulsoup4


## How to run

1. Run the scraping and database creation process:
  - Run main.py

2. Start the API server:
  - Open your terminal and run: uvicorn API.main:app --reload
  
This will run the API server locally on http://localhost:8000
http://localhost:8000/docs will show you all end-points currently accessible
  
3. Go to http://localhost:8000/competition_by_competitor/{competitor_name}
  This will show you all competitions the provided competitor has competed in.
  The parameter {competitor_name} is not case-sensitive.

For example, http://localhost:8000/competition_by_competitor/kelian will contain this result in JSON format:

{
  "competition": {
    "id": 31,
    "name": "NDO Openings Cup 20250119",
    "url": "https://scrutineering.org/NDO/20250119/"
  },
  "bracket": {
    "id": 607,
    "name": "Amateurs Ballroom",
    "url": "https://scrutineering.org/NDO/20250119/3-amateursballroom/index.htm"
  },
  "listing": {
    "id": 3322,
    "place": 3,
    "number": "67",
    "competitor_names": "Kelian Giesbers / Nienke de Jonge"
  }
}
