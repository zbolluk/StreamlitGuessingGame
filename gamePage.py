import streamlit as st
import random
from openai import OpenAI


client = OpenAI(
    api_key=st.secrets["api_key"], 
)

model = "gpt-4o-mini"

def Game_page():
    # Session state variables
    if "Goal" not in st.session_state:
        st.session_state.Goal = random.randint(1, 100)
    if "Guess_count" not in st.session_state:
        st.session_state.Guess_count = 0
    if "history" not in st.session_state:
        st.session_state.history = []
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []
    if "games_played" not in st.session_state:
        st.session_state.games_played = 0
    if "guesses_per_game" not in st.session_state:
        st.session_state.guesses_per_game = []

    # Instructions
    st.title("Number Guessing Game")
    st.write("In this game, you guess a number between 0-100.")
    st.write("Then, you will see a feedback for your guess. Revise your guess based on the feedback.")
    st.write("Your goal is finding the target number. Good luck!")

    for chat in st.session_state.chat_history:
        st.chat_message(chat["role"]).write(chat["content"])

    with st.chat_message("user"):
        Guess = st.text_input("Your guess:", label_visibility="collapsed")

    # Submit button
    if st.button("Submit Guess"):
        try:
            # Convert guess to integer
            Guess = int(Guess)
            feedback = ""
            # Compare guess with the target number
            if Guess < st.session_state.Goal:
                feedback = "Too low!"
            elif Guess > st.session_state.Goal:
                feedback = "Too high!"
            else:
                feedback = "Correct! 🎉"

                # Update statistics when the correct guess is made
                st.session_state.games_played += 1
                st.session_state.guesses_per_game.append(st.session_state.Guess_count)

                # Reset game for the next round
                st.session_state.Goal = random.randint(1, 100)
                st.session_state.Guess_count = 0
                st.session_state.history = []
                st.session_state.chat_history.append({"role": "assistant", "content": "Game reset! Start a new round."})

            # Add user guess to chat history
            st.session_state.chat_history.append({"role": "user", "content": f"My guess is {Guess}"})
            # Add feedback to chat history
            st.session_state.chat_history.append({"role": "assistant", "content": feedback})

            # Update guess count and history
            st.session_state.Guess_count += 1
            st.session_state.history.append(Guess)
            # Chatbot 
            try:
                messages = [
                    {"role": "system", "content": "You are a helpful assistant for a number guessing game."}
                     ]
                messages.extend(st.session_state.chat_history)
                chat_completion = client.chat.completions.create(
                    model = model,
                    messages = messages
                )
                bot_response = chat_completion.choices[0].message.content
                st.session_state.chat_history.append({"role": "assistant", "content": bot_response})
            except Exception as e:
                st.session_state.chat_history.append(
                    {"role": "assistant", "content": f"Error with OpenAI API: {str(e)}"}
                )

        except ValueError:
            # Handle invalid input
            feedback = "Please enter a valid number!"
            st.session_state.chat_history.append({"role": "assistant", "content": feedback})

        # Rerun the app to refresh the chat interface
        st.rerun()

    # Reset button to restart the game manually
    if st.button("Reset Game"):
        st.session_state.Goal = random.randint(1, 100)
        st.session_state.Guess_count = 0
        st.session_state.history = []
        st.session_state.chat_history = []
        st.rerun()

    # Display guess history and total guesses
    st.write("Guess History:", st.session_state.history)
    st.write(f"Total Guesses: {st.session_state.Guess_count}")
