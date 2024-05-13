from itertools import permutations

class Peta:
    def __init__(self):
        """Initialize a new Peta object."""
        self.city_list = {} 

    def print_peta(self):
        """Print the current state of the peta."""
        for city, neighbors in self.city_list.items():
            print(f"{city}: {neighbors}")

    def add_city(self, city: str) -> bool:
        """Add a new city to the peta."""
        if city not in self.city_list:
            self.city_list[city] = {} 
            return True
        return False

    def remove_city(self, city: str) -> bool:
        """Remove a city from the peta."""
        if city in self.city_list:
            del self.city_list[city]
            for other_city in self.city_list:
                if city in self.city_list[other_city]:
                    del self.city_list[other_city][city]
            return True
        return False

    def add_road(self, city1: str, city2: str, weight: int) -> bool:
        """Add a road between two cities."""
        if city1 in self.city_list and city2 in self.city_list and weight > 0:
            self.city_list[city1][city2] = weight
            self.city_list[city2][city1] = weight
            return True
        return False

    def remove_road(self, city1: str, city2: str) -> bool:
        """Remove a road between two cities."""
        if city1 in self.city_list and city2 in self.city_list:
            if city2 in self.city_list[city1]:
                del self.city_list[city1][city2]
                del self.city_list[city2][city1]
                return True
        return False

    def distance(self, city1: str, city2: str) -> int:
        """Calculate the distance between two cities."""
        if city1 not in self.city_list or city2 not in self.city_list:
            return -1
        if city1 == city2:
            return 0
        if city2 in self.city_list[city1]:
            return self.city_list[city1][city2]
        return -1

    def total_distance(self, city: str) -> int:
        """Calculate the total distance from a city to all other cities."""
        total_distance = 0
        for other_city in self.city_list:
            distance_to_city = self.distance(city, other_city)
            if distance_to_city != -1:
                total_distance += distance_to_city
        return total_distance

    def djikstra(self, source: str):
        """Menghitung jarak terpendek dari source ke semua kota lain menggunakan algoritma Dijkstra."""
        distances = {}
        for city in self.city_list:
            distances[city] = float('inf')
        distances[source] = 0
        
        unvisited_cities = list(self.city_list.keys())

        while unvisited_cities:
            min_distance = float('inf')
            closest_city = None
            for city in unvisited_cities:
                if distances[city] < min_distance:
                    min_distance = distances[city]
                    closest_city = city
            unvisited_cities.remove(closest_city)

            for neighbor, weight in self.city_list[closest_city].items():
                distance = distances[closest_city] + weight
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
        
        return distances

def tsp(self, start_city: str):
    """
    Menghitung jalur dan jarak terpendek untuk mengunjungi semua kota
    dan kembali ke kota awal (Traveling Salesperson Problem).
    """
    cities = list(self.city_list.keys())
    cities.remove(start_city)

    def tsp_recursive(current_city, remaining_cities, total_distance=0, path=None):
        if path is None:
            path = [current_city]

        if not remaining_cities:
            return total_distance + self.distance(current_city, start_city), path + [start_city]

        shortest_distance = float('inf')
        shortest_path = None

        for next_city in remaining_cities:
            if next_city in self.city_list[current_city] and next_city in remaining_cities: # Periksa keberadaan next_city
                distance_to_next = self.distance(current_city, next_city)
                new_distance = total_distance + distance_to_next
                new_path = path + [next_city]
                remaining = remaining_cities[:]
                remaining.remove(next_city)
                dist, p = tsp_recursive(next_city, remaining, new_distance, new_path)
                if dist < shortest_distance:
                    shortest_distance = dist
                    shortest_path = p

        return shortest_distance, shortest_path

    return tsp_recursive(start_city, cities)
    
# Contoh penggunaan
peta_jawa_timur = Peta()
peta_jawa_timur.add_city("Surabaya")
peta_jawa_timur.add_city("Malang")
peta_jawa_timur.add_city("Sidoarjo")
peta_jawa_timur.add_city("Madiun")
peta_jawa_timur.add_city("Situbondo")
peta_jawa_timur.add_city("Tuban")
peta_jawa_timur.add_city("Lamongan")
peta_jawa_timur.add_city("Probolinggo")
peta_jawa_timur.add_city("Pasuruan")
peta_jawa_timur.add_city("Banyuwangi")
peta_jawa_timur.add_city("Bondowoso")
peta_jawa_timur.add_city("Tulungagung")
peta_jawa_timur.add_city("Ponorogo")
peta_jawa_timur.add_city("Nganjuk")
peta_jawa_timur.add_city("Ngawi")
peta_jawa_timur.add_city("Bojonegoro")
peta_jawa_timur.add_city("Kediri")
peta_jawa_timur.add_city("Blitar")
peta_jawa_timur.add_city("Trenggalek")
peta_jawa_timur.add_city("Pacitan")

peta_jawa_timur.add_road("Surabaya", "Sidoarjo", 32) 
peta_jawa_timur.add_road("Surabaya", "Lamongan", 57)
peta_jawa_timur.add_road("Malang", "Sidoarjo", 103)
peta_jawa_timur.add_road("Situbondo", "Bondowoso", 63)
peta_jawa_timur.add_road("Bondowoso", "Pasuruan", 157)
peta_jawa_timur.add_road("Malang", "Pasuruan", 67)
peta_jawa_timur.add_road("Madiun", "Ngawi", 44)
peta_jawa_timur.add_road("Madiun", "Nganjuk", 40)
peta_jawa_timur.add_road("Bojonegoro", "Tuban", 61)
peta_jawa_timur.add_road("Tuban", "Lamongan", 57)
peta_jawa_timur.add_road("Lamongan", "Bojonegoro", 82) 
peta_jawa_timur.add_road("Probolinggo", "Pasuruan", 92)
peta_jawa_timur.add_road("Tulungagung", "Trenggalek", 45)
peta_jawa_timur.add_road("Situbondo", "Banyuwangi", 77)
peta_jawa_timur.add_road("Banyuwangi", "Bondowoso", 84)
peta_jawa_timur.add_road("Ponorogo", "Nganjuk", 79)
peta_jawa_timur.add_road("Nganjuk", "Ngawi", 74)
peta_jawa_timur.add_road("Situbondo", "Probolinggo", 111)
peta_jawa_timur.add_road("Ngawi", "Bojonegoro", 73)
peta_jawa_timur.add_road("Nganjuk", "Kediri", 55)
peta_jawa_timur.add_road("Kediri", "Tulungagung", 56)
peta_jawa_timur.add_road("Blitar", "Malang", 73)
peta_jawa_timur.add_road("Blitar", "Tulungagung", 40)
peta_jawa_timur.add_road("Trenggalek", "Ponorogo", 66)
peta_jawa_timur.add_road("Pacitan", "Ponorogo", 69)
peta_jawa_timur.add_road("Trenggalek", "Pacitan", 94)

source_city = "Surabaya"
print("-" * 30)
print("Peta Jawa Timur:")
print("-" * 30)
peta_jawa_timur.print_peta()

print("\n" + "=" * 30)
print(f"Jarak Terpendek dari {source_city}:")
print("=" * 30)
jarakSemuaKota = peta_jawa_timur.djikstra(source_city)
for city, distance in jarakSemuaKota.items():
    if city != source_city:
        print(f"{source_city} -> {city}: {distance} KM")



