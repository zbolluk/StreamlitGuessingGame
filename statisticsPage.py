import streamlit as st
import pandas as pd

# Stats Page
def Stats_page():
    # Initialize session state for stats if not already done
    if "games_played" not in st.session_state:
        st.session_state.games_played = 0
    if "guesses_per_game" not in st.session_state:
        st.session_state.guesses_per_game = []

    # Display Stats
    st.title("Game Statistics")
    st.write("Here are your game statistics so far!")

    # Games Played
    st.write(f"Total Games Played: {st.session_state.games_played}")

    # Average Guesses
    if st.session_state.guesses_per_game:
        avg_guesses = sum(st.session_state.guesses_per_game) / len(st.session_state.guesses_per_game)
        st.write(f"Average Number of Guesses Per Game: {avg_guesses:.2f}")
    else:
        st.write("No games played yet!")

    # Bar Chart for Number of Guesses Per Game
    if st.session_state.guesses_per_game:
        st.write("Number of Guesses Per Game:")
        # Create a DataFrame for visualization
        df = pd.DataFrame({
            "Game Number": range(1, len(st.session_state.guesses_per_game) + 1),
            "Number of Guesses": st.session_state.guesses_per_game
        })
        # Plotting the bar chart
        st.bar_chart(df.set_index("Game Number"))
    else:
        st.write("Play some games to see your statistics!")