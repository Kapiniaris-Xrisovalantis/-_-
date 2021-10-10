import requests
key = "eDB3cGMne4pQiXsQf6CBh8DIBIbPG4RUgkKEdVr2"

url = f"https://api.nasa.gov/neo/rest/v1/feed?api_key={key}"
# Χωρίς παραμέτρους, επιστρέφονται τα στοιχεία για τις ημερομηνίες ανάμεσα στην σημερινή και τις 7 επόμενες ημέρες.

requests = requests.get(url)
result = requests.json()
r = result['near_earth_objects']
total = result['element_count']

d = [] 
for date in r.keys():
    d.append(date)

data = dict()
data['count'] = result['element_count']
data['hazard_count'] = 0
data['max_speed'] = -1
data['max_speed_name'] = ""
data['estimated_diameter_max'] = -1
data['estimated_diameter_max_name'] = ""

for date_iterator in range(len(d)):
    for asteroid in range(len(r[d[date_iterator]])):
        if r[d[date_iterator]][asteroid]['is_potentially_hazardous_asteroid']:
            data['hazard_count'] += 1

        if float(r[d[date_iterator]][asteroid]['close_approach_data'][0]['relative_velocity']['kilometers_per_hour']) > data['max_speed']:
            data['max_speed'] = float(r[d[date_iterator]][asteroid]['close_approach_data'][0]['relative_velocity']['kilometers_per_hour'])
            data['max_speed_name'] = r[d[date_iterator]][asteroid]['name']

        if float(r[d[date_iterator]][asteroid]['estimated_diameter']['kilometers']['estimated_diameter_max'] > data['estimated_diameter_max']):
            data['estimated_diameter_max'] = float(r[d[date_iterator]][asteroid]['estimated_diameter']['kilometers']['estimated_diameter_max'])
            data['estimated_diameter_max_name'] = r[d[date_iterator]][asteroid]['name']

print(f"Το σύνολο των σωμάτων είναι: {data['count']}")
print(f"Το σύνολο των σωμάτων που μπορούν να δημιουργήσουν πρόβλημα είναι: {data['hazard_count']}")
print(f"Το όνομα του ουράνιου σώματος με την μεγαλύτερη ταχύτητα είναι το: '{data['max_speed_name']}' με ταχύτητα {data['max_speed']} χιλιόμετρα την ώρα")
print(f"Το όνομα του ουράνιου σώματος με την μεγαλύτερη (εκτιμώμενη) διάμετρο είναι το: '{data['estimated_diameter_max_name']}' με εκτιμώμενη διάμετρο {data['estimated_diameter_max']} χιλιόμετρα")