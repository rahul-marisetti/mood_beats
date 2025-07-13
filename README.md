# MoodBeats App

A mood-based music recommendation web app built using **Flask**, **Spotify API**, and **Google Custom Search API**. The user selects their mood, preferred language, and favorite artist — and the app returns a curated list of songs along with the artist's image.

---

## 🚀 Features

* 🎵 Select **mood**, **language**, and **artist** using dropdowns
* 🔍 Artist list dynamically loads based on selected language
* ▶️ Listen to song previews fetched from Spotify
* 🖼️ Display top image of the selected artist using Google Custom Search
* 🎨 Clean, responsive UI with music-themed design

---

## 🛠️ Technologies Used

* **Flask** – Web framework
* **Spotify API** – To fetch tracks and artist details
* **Google Custom Search API** – To fetch artist images
* **HTML + CSS** – Frontend templates
* **Render** – For deployment

---

## 🧪 Setup Instructions

### 🔐 1. Get API Keys

* [Spotify Developer Portal](https://developer.spotify.com/dashboard)

  * Create an app and get `SPOTIPY_CLIENT_ID` and `SPOTIPY_CLIENT_SECRET`
* [Google Programmable Search](https://programmablesearchengine.google.com/)

  * Create a search engine and get `GOOGLE_API_KEY` and `GOOGLE_CSE_ID`
  * Make sure **Image Search** is enabled

---

### 📆 2. Installation

```bash
cd MoodBeats-app
pip install -r requirements.txt
```

---

### ⚙️ 3. Environment Variables

Create a `.env` file (if using `python-dotenv`) or set the following manually:

```env
SPOTIPY_CLIENT_ID=your_spotify_client_id
SPOTIPY_CLIENT_SECRET=your_spotify_client_secret
GOOGLE_API_KEY=your_google_api_key
GOOGLE_CSE_ID=your_google_cse_id
```

---

### ▶️ 4. Run Locally

```bash
python app.py
```

Then open [http://127.0.0.1:5000](http://127.0.0.1:5000) in your browser.

---

## 🚢 Deployment on Render

You can deploy this project on [Render](https://render.com/) using:

* A `render.yaml` file
* Or manually via their dashboard using:

  * **Start Command**: `gunicorn app:app`
  * **Environment Variables**: Add your API keys

> 📝 Note: Spotify may not allow localhost or unverified URLs as redirect URIs — we’ve used client credentials flow which doesn’t need user login.

---

## 🔍 Notes

* The **free tier** of Google Custom Search limits you to 100 queries/day.
* Ensure image fetching follows Google’s acceptable use policy.
* Song previews may not be available for all tracks.

---

## 📄 License

This project is licensed under the MIT License.
