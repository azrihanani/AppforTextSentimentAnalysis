import streamlit as st
from textblob import TextBlob

# Function to display the text analysis page
def display_page():
    st.subheader("Text Analysis Using TextBlob")
    st.text("Enter text to be analyzed:")
    user_text = st.text_input("Input", placeholder="Input text here")
    st.text(" ")

    if st.button("Predict"):
        if user_text:  # Check for non-empty user input
            st.markdown("""<h3 style="color:#02C7C7;font-family:'Poppins'; font-size:30px; margin-bottom:8px; margin-top:40px;">RESULT</h3>""",unsafe_allow_html=True,)
            get_sentiment(user_text)

# Function to analyze sentiment and display results
def get_sentiment(user_text):
    try:
        # Perform sentiment analysis
        blob = TextBlob(user_text)
        polarity = round(blob.polarity, 2)
        subjectivity = round(blob.subjectivity, 2)

        # Determine sentiment label
        if polarity > 0:
            sentiment_label = "Positive"
            image_path = "./images/positive.png"
        elif polarity == 0:
            sentiment_label = "Neutral"
            image_path = "./images/neutral.png"
        else:
            sentiment_label = "Negative"
            image_path = "./images/negative.png"

        # Display results
        st.markdown(f"**Polarity:** {polarity}")
        st.markdown(f"**Subjectivity:** {subjectivity}")
        st.markdown(f"**Sentiment:** {sentiment_label}")
        st.image(image_path, caption=sentiment_label)

    except Exception as e:  # Handle potential errors
        st.error(f"An error occurred: {e}")

# Call the main function to start the app
display_page()
