# 🎯 Video Relevance Scorer (Manual Transcript Version)

A simple and interactive *Streamlit web application* that calculates the *relevance score* between a topic (Title + Description) and a manually pasted transcript.

This app uses *keyword overlap*, *heatmap visualization*, and a *score justification engine* to help evaluate how closely a transcript matches the expected video topic.

---

## 🚀 Features

### ✅ Manual Input
- Enter *Title*
- Enter *Description*
- Paste *Transcript*
- Optional: Enter a Youtube URL (for reference only)

### ✅ Relevance Score
- Calculates score using *keyword overlap percentage*
- Displays score out of 100

### 🎨 Visualizations
- Beautiful *heatmap* showing matching vs non-matching keywords
- Highlighted matched keywords
- Automatic justification (high, medium, low relevance)

### ✨ UI Enhancements
- Clean soft-colored layout
- White text boxes
- Smooth animations (balloons/snow based on score)

### 🔒 No Machine Learning Models Required
- Extremely fast  
- No heavy downloads

## 📁 Project Structure

. ├── app.py ├── README.md └── requirements.txt   (optional)

---

## 🛠️ Installation

**1. Clone the repository:**

git clone https://github.com/rashmisurya-b/video-relevance-scorer.git

**2. Install required dependencies:**

pip install streamlit seaborn matplotlib numpy

**3. Run the app:**

streamlit run app.py

---
## 📊 How the Scoring Works

**The app uses a simple non-ML logic:**

1. Convert text to lowercase

2. Remove punctuation

3. Split into words

4. Compare Title + Description against Transcript

5. Score = (matching words / total unique topic words) × 100

This makes the tool:

Fast

Lightweight

Very reliable for simple relevance checks

---

## 🎥 Demo

**You can create a demo video using OBS, Loom, or ScreenStudio:**

Install screen recorder

Record how you use the app

Upload video to YouTube or Google Drive

Add link here:

👉 Demo Video: [Coming Soon]

---

## 🌐 Deployment

You can deploy this app for free using:

**1. Streamlit Cloud (Recommended)**

Very easy — no Docker, no servers.

1. Push your code to GitHub

2. Go to
🔗 https://streamlit.io/cloud

3. Click New App

4. Select your GitHub repo

5. Choose app.py

6. Deploy 🎉

**2. HuggingFace Spaces**

Also easy.

1. Create a new space

2. Select Streamlit

3. Upload your files

4. Add requirements.txt

5. Deploy

**3. Render.com**

For more backend control.

---

## 📦 Optional: requirements.txt

streamlit
seaborn
matplotlib
numpy


---

## 🤝 Contributing

Pull requests are welcome!
If you’d like to add features such as:

TF-IDF relevance

Word-cloud visualization

PDF report generator

Multi-language support


Feel free to contribute.


---

## 📄 License

MIT License — free to use & modify.


---

## 💡 Author

**Rashmi Surya B**
Feel free to reach out or star the repo ⭐ if you find this useful!
- Works offline once installed

---
