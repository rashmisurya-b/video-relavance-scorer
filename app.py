import streamlit as st
import re
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------------------------
# CUSTOM BACKGROUND (SOFT CREAM)
# ---------------------------------
page_bg_style = """
<style>
[data-testid="stAppViewContainer"] {
    background: linear-gradient(135deg, #eef2f3, #e3f2fd);
    background-size: cover;
}
[data-testid="stHeader"] {
    background: rgba(0, 0, 0, 0);
}
[data-testid="stSidebar"] {
    background: #ffffffcc;
}
.stTextInput, .stTextArea, textarea, input {
        background-color: #FFFFFF !important;   /* white boxes */
        color: #000000 !important;
}
</style>
"""

st.markdown(page_bg_style, unsafe_allow_html=True)

# -----------------------------
# CLEAN TEXT FUNCTION
# -----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', ' ', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# -----------------------------
# BASIC RELEVANCE SCORE
# -----------------------------
def compute_relevance(title, description, transcript):
    ref = clean_text(title + " " + description)
    ref_words = set(ref.split())

    trans = clean_text(transcript)
    trans_words = set(trans.split())

    if len(ref_words) == 0:
        return 0.0, [], 0

    overlap = ref_words.intersection(trans_words)
    score = (len(overlap) / len(ref_words)) * 100

    return round(score, 2), sorted(list(overlap)), len(ref_words)

# -----------------------------
# SCORE EXPLANATION
# -----------------------------
def explain_score(score):
    if score >= 80:
        return "This transcript is highly relevant to the topic, with most keywords matched."
    elif score >= 60:
        return "Good relevance. Many important keywords appear, but some are missing."
    elif score >= 40:
        return "Moderate relevance. Transcript partially matches the topic."
    elif score >= 20:
        return "Low relevance. Only a few keywords match."
    else:
        return "Very low relevance. The transcript is mostly unrelated to the topic."

# -----------------------------
# STREAMLIT UI
# -----------------------------
st.set_page_config(page_title="Video Relevance Scorer", layout="wide")

st.title("🎯 Video Relevance Scorer")

url = st.text_input("🔗 YouTube URL:")

st.subheader("📝 Topic Inputs")
title = st.text_input("Enter Expected Topic / Title:")
description = st.text_area("Enter Expected Description:")

st.subheader("📄 Transcript (Paste Manually)")
transcript = st.text_area("Paste Transcript Here:", height=220)


# Placeholder for animation
animation_placeholder = st.empty()

# -----------------------------
# CALCULATE SCORE
# -----------------------------
if st.button("✨ Calculate Relevance Score"):
    if not title.strip() or not description.strip():
        st.error("Please enter both title and description.")
    elif not transcript.strip():
        st.error("Please paste the transcript.")
    else:
        # Calculate score
        st.snow()
        score, overlap_words, total_keywords = compute_relevance(title, description, transcript)

        # Show score
        st.success(f"🎉 Relevance Score: *{score} / 100*")

        # Explanation
        st.subheader("📌 Explanation")
        st.write(explain_score(score))

        # Matched words
        st.subheader("🔑 Matched Keywords")
        if overlap_words:
            st.success(", ".join(overlap_words))
        else:
            st.warning("No matching keywords found.")

        # -----------------------------
        # HEATMAP
        # -----------------------------
        st.subheader("🔥 Keyword Overlap Heatmap")

        match_count = len(overlap_words)
        not_match = total_keywords - match_count

        heatmap_data = np.array([[match_count, not_match]])

        fig, ax = plt.subplots(figsize=(6, 2))
        sns.heatmap(
            heatmap_data,
            annot=True,
            fmt="d",
            cmap="YlOrRd",
            xticklabels=["Matched", "Not Matched"],
            yticklabels=["Keywords"],
            cbar=True,
            linewidths=2
        )
        st.pyplot(fig)