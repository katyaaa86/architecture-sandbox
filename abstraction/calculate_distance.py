import math

if __name__ == '__main__':
	first_point = [55.621506, 37.786676]
	last_point = [55.044887, 38.82657]

	first_lat = first_point[0]
	first_long = first_point[1]
	last_lat = last_point[0]
	last_long = last_point[1]

	first_lat_rad = math.radians(first_lat)
	first_long_rad = math.radians(first_long)
	last_lat_rad = math.radians(last_lat)
	last_long_rad = math.radians(last_long)

	lat_diff = last_lat_rad - first_lat_rad
	long_diff = last_long_rad - first_long_rad

	haversine = (
		math.sin(lat_diff / 2) ** 2
		+ math.cos(first_lat_rad)
		* math.cos(last_lat_rad)
		* math.sin(long_diff / 2) ** 2
	)
	print(6371 * (2 * math.atan2(math.sqrt(haversine), math.sqrt(1 - haversine))))
