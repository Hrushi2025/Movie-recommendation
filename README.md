
# 🎬 Movie Recommendation System

This is a Content-Based Movie Recommendation System built using **Python**, **Pandas**, **Streamlit**, and the **TMDb API**. The system recommends 5 movies similar to the one selected by the user, and displays their posters.

---

## 📌 Features

- Select a movie from a dropdown list
- Get top 5 similar movie recommendations
- View posters of recommended movies using TMDb API
- Interactive user interface with Streamlit

---

## 📁 Project Structure

```
.
├── app.py                   # Main Streamlit application
├── Movie Recommendation System.ipynb  # Jupyter notebook for feature engineering & similarity logic
├── movie_dict.pkl          # Pickled dictionary of movies and metadata
├── similarity.pkl          # Pickled similarity matrix for recommendation engine
```

---

## 🛠️ Installation & Setup

1. **Clone the repository** or download the project files.

2. **Install required packages**:

   ```bash
   pip install streamlit pandas requests
   ```

3. **Ensure the following files are present in the same directory as `app.py`**:
   - `movie_dict.pkl`
   - `similarity.pkl`

4. **Run the Streamlit app**:

   ```bash
   streamlit run app.py
   ```

---

## 🔑 API Key

This project uses **TMDb API** to fetch movie posters. A demo key is already included in the code, but for production:

1. Create a free TMDb account.
2. Visit: https://www.themoviedb.org/settings/api
3. Generate your API key.
4. Replace the key in `app.py`:

   ```python
   url = f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=YOUR_API_KEY'
   ```

---

## 🧠 How It Works

- The recommendation logic is built using **cosine similarity** on movie feature vectors (like genres, keywords, etc.).
- These vectors are generated using CountVectorizer or TF-IDF in the notebook (`Movie Recommendation System.ipynb`).
- The similarity matrix is precomputed and stored as `similarity.pkl`.
- When a user selects a movie, the top 5 most similar movies (based on similarity score) are retrieved and their posters are fetched via the TMDb API.

---

## 📸 Example Output

When a movie is selected:

- The top 5 similar movies are shown
- Their posters are displayed side-by-side in columns

---

## ⚠️ Notes

- If TMDb API fails or the poster path is missing, a placeholder image will be shown.
- All recommendations are based on static data loaded from `.pkl` files — ensure those files are available before running the app.

---

## 🧪 Future Improvements

- Add hybrid recommendation (collaborative + content-based)
- Implement search by genre or actor
- Improve UI styling and error handling

---

## 📚 License

This project is for educational and demonstration purposes only.
