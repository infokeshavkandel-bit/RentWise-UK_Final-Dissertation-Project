import requests

query = """
[out:json];
area["name"="England"]->.searchArea;

(
  node["amenity"="school"](area.searchArea);
  node["amenity"="hospital"](area.searchArea);
  node["shop"="supermarket"](area.searchArea);
);

out body;
"""

response = requests.post(
    "https://overpass-api.de/api/interpreter",
    data=query
)