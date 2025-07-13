from flask import Flask, render_template, request, redirect, url_for, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import requests

app = Flask(__name__)

# Spotify credentials (replace with your own)
SPOTIPY_CLIENT_ID = '85ca45797d674694a16ff219752d5ffb'
SPOTIPY_CLIENT_SECRET = 'dbe1bfd1937b435ba78e009d96d29346'

# Google Custom Search API credentials (replace with your own)
GOOGLE_API_KEY = "AIzaSyCmVTFS0NHWFc4IKrO2jEqvyCo8cligapI"
GOOGLE_CSE_ID = "e75c9c7269df64242"

# Initialize Spotify API
client_credentials_manager = SpotifyClientCredentials(client_id=SPOTIPY_CLIENT_ID,
                                                      client_secret=SPOTIPY_CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

songs = []  # Store results between pages
artist_image = None

# Sample data for dropdowns
moods = ['Happy', 'Sad', 'Energetic', 'Relaxed', 'Romantic', 'Motivated', 'Nostalgic']
language_seed_genres = {
    'Hindi': 'indian',
    'Tamil': 'tamil',
    'Telugu': 'telugu',
    'Kannada': 'kannada',
    'Malayalam': 'malayalam',
    'Gujarati': 'gujarati',
    'Punjabi': 'punjabi',
    'Bengali': 'bengali',
    'Marathi': 'marathi',
    'Urdu': 'desi',
    'Konkani': 'indian',
    'Assamese': 'indian',
    'Sanskrit': 'indian',
    'Nepali': 'nepali',
    'Oriya': 'indian'
}

def get_google_artist_image(artist_name, api_key, cse_id):
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "q": artist_name,
        "cx": cse_id,
        "key": api_key,
        "searchType": "image",
        "num": 1
    }
    try:
        response = requests.get(url, params=params)
        results = response.json().get("items", [])
        return results[0]["link"] if results else None
    except Exception as e:
        print("Google Image Search error:", e)
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/mood', methods=['GET', 'POST'])
def mood():
    return render_template('mood.html', moods=moods, languages=list(language_seed_genres.keys()))

@app.route('/get_artists', methods=['POST'])
def get_artists():
    selected_language = request.form.get('language')

    top_telugu_artists = [
        "Sid Sriram", "Armaan Malik", "Anirudh Ravichander", "S. P. Balasubrahmanyam",
        "Chinmayi", "Shreya Ghoshal", "Sunitha", "Devi Sri Prasad", "Ramya Behara",
        "Karthik", "Harris Jayaraj", "Yazin Nizar", "Shankar Mahadevan", "Geetha Madhuri",
        "Naresh Iyer", "Kaala Bhairava", "Suchitra", "Mangli", "Udit Narayan", "Arijit Singh",
        "Ranjith", "Swaraveenapani", "Aditya Iyengar", "Vijay Prakash", "Nithya Menen",
        "Chinmayi Sripaada", "Sravana Bhargavi", "Revanth", "Jonita Gandhi", "Haricharan",
        "SP Charan", "Anjana Sowmya", "Vijay Yesudas", "Bhavatharini", "Vandemataram Srinivas",
        "Kousalya", "K. S. Chithra", "Mahathi", "Unni Krishnan", "Mano", "Sanket Mhatre",
        "Rahul Sipligunj", "Vedala Hemachandra", "Rita", "Malavika", "Anudeep Dev", "Sai Charan", "Surmukhi Raman", "Nikhita Gandhi", "Akhil"
    ]

    if selected_language == 'Telugu':
        return jsonify(top_telugu_artists)

    genre = language_seed_genres.get(selected_language, 'indian')
    top_artists = []
    try:
        results = sp.search(q=f"genre:{genre}", type='artist', limit=50)
        for item in results['artists']['items']:
            top_artists.append(item['name'])
    except Exception as e:
        print("Error fetching artists:", e)
        top_artists = ['Artist Not Found']
    return jsonify(top_artists)

@app.route('/get_songs', methods=['POST'])
def get_songs():
    global songs, artist_image

    mood = request.form['mood']
    language = request.form['language']
    artist = request.form['artist']

    query = f"{mood} {language} {artist}"
    results = sp.search(q=query, type='track', limit=10)

    songs = []
    for item in results['tracks']['items']:
        song = {
            'name': item['name'],
            'artist': item['artists'][0]['name'],
            'preview_url': item['preview_url'],
            'external_url': item['external_urls']['spotify']
        }
        songs.append(song)

    # Fetch one artist image from Google Custom Search
    artist_image = get_google_artist_image(artist, GOOGLE_API_KEY, GOOGLE_CSE_ID)

    return redirect(url_for('listen'))

@app.route('/listen')
def listen():
    return render_template('listen.html', songs=songs, artist_image=artist_image)

if __name__ == '__main__':
    app.run(debug=True)