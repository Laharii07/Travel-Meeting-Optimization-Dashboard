from datetime import datetime, timedelta

UNDERGROUND_BUFFER = 20  # minutes
AIRPORT_CHECKIN_DOMESTIC = 60
AIRPORT_CHECKIN_INTL = 120
HEATHROW_TO_CENTRAL = 45  # Piccadilly Line, minutes
GATWICK_TO_CENTRAL = 30   # Gatwick Express, minutes

def generate_itinerary(meeting_time_str, origin_city='Manchester', airport='LHR'):
    meeting = datetime.strptime(meeting_time_str, '%Y-%m-%d %H:%M')
    
    transfer = HEATHROW_TO_CENTRAL if airport == 'LHR' else GATWICK_TO_CENTRAL
    checkin = AIRPORT_CHECKIN_DOMESTIC
    
    land_by = meeting - timedelta(minutes=transfer + UNDERGROUND_BUFFER + 30)
    depart_by = land_by - timedelta(minutes=60)  # ~1hr domestic flight
    arrive_airport_by = depart_by - timedelta(minutes=checkin)
    
    print(f"\n--- Itinerary for: {meeting.strftime('%a %d %b %Y, %H:%M')} meeting ---")
    print(f"  Leave for airport:  {arrive_airport_by.strftime('%H:%M')}")
    print(f"  Depart {origin_city}:     {depart_by.strftime('%H:%M')}")
    print(f"  Land {airport}:         {land_by.strftime('%H:%M')}")
    print(f"  Travel to office:   {(land_by + timedelta(minutes=transfer)).strftime('%H:%M')}")
    print(f"  Buffer time:        {UNDERGROUND_BUFFER} min (Underground delays)")
    print(f"  Meeting starts:     {meeting.strftime('%H:%M')}")
    print(f"\n  Tip: Book outbound flight by {(meeting - timedelta(days=14)).strftime('%d %b')} for ~30% saving.")

# Example usage
generate_itinerary('2024-06-15 10:00', origin_city='Manchester', airport='LHR')
