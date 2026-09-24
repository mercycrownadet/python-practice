distance_mi = 5
is_raining = False
has_bike = True
has_car = True
has_ride_share_app = True

#  Check for Distance (Falsy check)
if not distance_mi:
    print(False) 

# Short Distance (<= 1 mile and not raining)
elif distance_mi <= 1 and not is_raining:
    print(True) 

#  Medium Distance (between 1 and 6 miles, has bike, not raining)
elif 1 < distance_mi <= 6 and has_bike and not is_raining:
    print(True)

#  Long Distance (> 6 miles, has car or ride-share)
elif distance_mi > 6 and (has_car or has_ride_share_app):
    print(True)

#   Any other scenario (raining, no bike, etc.)
else:
    print(False)
