import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
import os

# Create output folder
os.makedirs("output", exist_ok=True)

# Load Datasets

matches = pd.read_csv("data/matches.csv")
deliveries = pd.read_csv("data/deliveries.csv")

print("Datasets Loaded Successfully")

# Top Batsmen Analysiss

top_batsmen = (
    deliveries.groupby("batter")["batsman_runs"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(10,5))
top_batsmen.plot(kind="bar")

plt.title("Top 10 IPL Run Scorers")
plt.ylabel("Runs")

plt.tight_layout()
plt.savefig("output/top_batsmen.png")
plt.close()

# Team Wins Analysis

team_wins = matches["winner"].value_counts()

plt.figure(figsize=(10,5))
team_wins.plot(kind="bar")

plt.title("Team Wins in IPL")
plt.ylabel("Wins")

plt.tight_layout()
plt.savefig("output/team_wins.png")
plt.close()

# Toss Impact Analysis

matches["toss_match_win"] = (
    matches["toss_winner"] == matches["winner"]
)

toss_impact = matches["toss_match_win"].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    toss_impact,
    labels=["Won Toss & Match","Lost Match"],
    autopct="%1.1f%%"
)

plt.title("Impact of Toss on Match Outcome")

plt.savefig("output/toss_impact.png")
plt.close()

# Venue Analysis

venue_matches = (
    matches["venue"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10,5))
venue_matches.plot(kind="bar")

plt.title("Top IPL Venues by Matches Hosted")
plt.ylabel("Matches")

plt.tight_layout()
plt.savefig("output/venue_analysis.png")
plt.close()

# SQL Database Storage

conn = sqlite3.connect("ipl.db")

matches.to_sql(
    "matches",
    conn,
    if_exists="replace",
    index=False
)

deliveries.to_sql(
    "deliveries",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

# Project Insights

print("\n===== PROJECT INSIGHTS =====")

print("\nMost Successful Team:")
print(team_wins.head(1))

print("\nTop Run Scorer:")
print(top_batsmen.head(1))

print("\nTotal Matches:")
print(len(matches))

print("\nProject Completed Successfully")
