import pandas as pd
import numpy as np

# --- Flight data ---
flights = pd.read_csv('flights.csv')
flights.columns = flights.columns.str.lower().str.replace(' ', '_')
flights['date_of_journey'] = pd.to_datetime(flights['date_of_journey'], dayfirst=True)
flights['booking_date'] = pd.to_datetime(flights['booking_date'], dayfirst=True)

# This is the key column for your trend chart
flights['days_before_flight'] = (flights['date_of_journey'] - flights['booking_date']).dt.days
flights['price'] = flights['price'].astype(float)

# Save cleaned version
flights.to_csv('flights_clean.csv', index=False)

# --- Room data ---
rooms = pd.read_csv('room_bookings.csv')
rooms['date'] = pd.to_datetime(rooms['date'])
rooms['week'] = rooms['date'].dt.isocalendar().week
rooms.to_csv('rooms_clean.csv', index=False)

print("Done. Files saved.")
