import streamlit as st 
from src.monty_hall import simulate_game


st.title(":sparkler: Monty Hall Simulation")

num_games = st.number_input(
            "Enter number of games to simulate",
            min_value=1, 
            max_value=100000, 
            value=100
)

col1, col2 = st.columns(2)
col1.subheader("Win Percentage With Switching")
col2.subheader("Win Percentage Without Switching")

chart1 = col1.line_chart(x=None, y=None, height=400)
chart2 = col2.line_chart(x=None, y=None, height=400)


wins_no_switch = 0
wins_switch = 0

for i in range(num_games):
    num_wins_with_switching, num_wins_without_switching = simulate_game(i)

    chart1.add_rows([num_wins_with_switching / (i + 1)])
    chart2.add_rows([num_wins_without_switching / (i + 1)])