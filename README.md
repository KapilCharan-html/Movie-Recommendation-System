# 🎬 Movie Recommendation System

A web app that recommends similar movies based on your selected movie. Built using **Python**, **Streamlit**, and **TMDb API**, it also displays movie posters using live API requests.

---

## 🚀 Features

- ✅ Get 5 movie recommendations based on similarity
- 🖼️ Shows posters of recommended movies
- 🔍 Intelligent search with error handling
- 📂 Handles large files using Git LFS

---

## 🛠️ Tech Stack

- Python 3.10+
- Pandas, Scikit-learn
- Streamlit
- Requests
- Git LFS (for handling large `.pkl` and `.csv` files)

---
📥 Download Large Files
These files exceed GitHub's 25MB upload limit. Download from Google Drive:
### 🔗 Download Large Files
Some files exceed GitHub’s 25MB limit. Download them from Google Drive:

- [similarity.pkl](https://drive.google.com/file/d/1ZXiwuWjtj098VyFRnF0Nt3ZqgbV7SRYk/view?usp=drive_link)


similarity.pkl

tmdb_5000_credits.csv
## 📁 Files Included

| File Name               | Description                            |
|------------------------|----------------------------------------|
| `app.py`               | Streamlit web app                      |
| `similarity.pkl`       | Precomputed similarity matrix (LFS)    |
| `movies.pkl`           | Movie title & ID mapping               |
| `tmdb_5000_credits.csv`| Original movie data from TMDb (LFS)    |

---

## 🧠 How to Run

### ⚙️ 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
cd YOUR_REPO
📦 2. Set up Environment
bash
Copy
Edit
pip install -r requirements.txt
💾 3. Install Git LFS
bash
Copy
Edit
git lfs install
git lfs pull
▶️ 4. Run the App
bash
Copy
Edit
streamlit run app.py
🔑 TMDb API Key
Replace YOUR_API_KEY in app.py:

python
api_key = "your_actual_tmdb_api_key"
📝 Sample Output

🧠 Future Work
Add genres & ratings filters

Improve poster loading speed

Deploy on Streamlit Cloud or Render

📢 Acknowledgements
TMDb for the API and movie dataset

Vel Tech University – Internship support

Project developed during AI ML Internship Of Elevate Latbs

📬 Contact
Kapil Charan
📧 kapilcharan207@gmail.com



