# music_nlp
Python NLP application for music discovery. Aim is to discover music through text descriptions of the desired music.

The data folder contains ~14,000 reviews scraped from Resident Advisor. This will be supplemented by other data in the futures.

The code folder contains a single script which searches the review data for specific search terms and genres.
It then returns a list of albums that meet the input criteria in order of review rating.

Rough To Do:
- Sentiment analysis.
- Topic modelling.
- Word frequency analysis.
- Bring in BBC music reviews, Pitchfork reviews, Anthony Fantano reviews from Google Dataset Search.
- Named entity recognition with entities acquired from review data, as well as Spotify API (Soundcloud and Bandcamp too if possible).
