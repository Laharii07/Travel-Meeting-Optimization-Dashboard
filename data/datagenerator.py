import pandas as pd
import numpy as np
import random

rooms = ['Boardroom A', 'Meeting Room 1', 'Meeting Room 2', 
         'Quiet Pod 1', 'Quiet Pod 2', 'Conference Suite']
dates = pd.date_range('2024-01-01', '2024-03-31', freq='B')

records = []
for date in dates:
    for room in rooms:
        # Boardroom A is most used, Quiet Pods least
        booking_prob = {'Boardroom A': 0.85, 'Meeting Room 1': 0.70,
                        'Meeting Room 2': 0.65, 'Quiet Pod 1': 0.30,
                        'Quiet Pod 2': 0.25, 'Conference Suite': 0.50}
        if random.random() < booking_prob[room]:
            records.append({
                'date': date,
                'room': room,
                'day_of_week': date.strftime('%A'),
                'booked': 1
            })

df = pd.DataFrame(records)
df.to_csv('room_bookings.csv', index=False)
print(f"Generated {len(df)} booking records")
