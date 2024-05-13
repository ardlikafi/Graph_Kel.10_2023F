from itertools import permutations

class Peta:
    def __init__(self):
        """Initialize a new Peta object."""
        self.city_list = {}

    def print_peta(self):
        """Print the current state of the peta."""
        for city in self.city_list:
            print(f"{city}: {self.city_list[city]}")

    def add_city(self, city: str) -> bool:
        """Add a new city to the peta."""
        if city not in self.city_list:
            self.city_list[city] = {"roads": {}, "weights": {}}
            return True
        return False

    def remove_city(self, city: str) -> bool:
        """Remove a city from the peta."""
        if city in self.city_list:
            for other_city in self.city_list:
                if city in self.city_list[other_city]["weights"]:
                    self.city_list[other_city]["weights"].pop(city)
            del self.city_list[city]
            return True
        return False

    def add_road(self, city1: str, city2: str, weight: int) -> bool:
        """Add a road between two cities."""
        if city1 in self.city_list and city2 in self.city_list:
            if city2 in self.city_list[city1]["weights"]:
                if self.city_list[city1]["weights"][city2] != weight:
                    return False
            else:
                self.city_list[city1]["weights"][city2] = weight

            if city1 in self.city_list[city2]["weights"]:
                if self.city_list[city2]["weights"][city1] != weight:
                    return False
            else:
                self.city_list[city2]["weights"][city1] = weight

            return True
        return False

    def remove_road(self, city1: str, city2: str) -> bool:
        """Remove a road between two cities."""
        if city1 in self.city_list and city2 in self.city_list:
            if city2 in self.city_list[city1]["weights"]:
                self.city_list[city1]["weights"].pop(city2)
            if city1 in self.city_list[city2]["weights"]:
                self.city_list[city2]["weights"].pop(city1)
            return True
        return False

    def distance(self, city1: str, city2: str) -> int:
        """Calculate the distance between two cities."""
        if city1 not in self.city_list or city2 not in self.city_list:
            return -1
        if city1 == city2:
            return 0
        if city2 not in self.city_list[city1]["weights"]:
            return -1
        return self.city_list[city1]["weights"][city2]

    def total_distance(self, city: str) -> int:
        """Calculate the total distance from a city to all other cities."""
        total_distance = 0
        for other_city in self.city_list:
            distance_to_city = self.distance(city, other_city)
            if distance_to_city != -1:
                total_distance += distance_to_city
        return total_distance

    def djikstra(self, source):
        
        distance = {}
        for city in self.city_list:
            distance[city] = float('inf')
        distance[source] = 0

        unvisited_cities = list(self.city_list.keys())

        while unvisited_cities:
            min_distance = float('inf')
            closest_city = None
            for city in unvisited_cities:
                if distance[city] < min_distance:
                    min_distance = distance[city]
                    closest_city = city

            unvisited_cities.remove(closest_city)

            for neighbor, jarak in self.city_list[closest_city]["weights"].items():
                jarakNeighbor = distance[closest_city] + jarak
                if jarakNeighbor < distance[neighbor]:
                    distance[neighbor] = jarakNeighbor
        return distance
    
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
            self.city_list[city] = {}  # Inisialisasi dictionary kosong untuk tetangga
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
        if city1 in self.city_list and city2 in self.city_list:
            self.city_list[city1][city2] = weight
            self.city_list[city2][city1] = weight
            return True
        return False

    def remove_road(self, city1: str, city2: str) -> bool:
        """Remove a road between two cities."""
        if city1 in self.city_list and city2 in self.city_list:
            if city2 in self.city_list[city1]:
                del self.city_list[city1][city2]
            if city1 in self.city_list[city2]:
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

    def djikstra(self, source):
        """Menghitung jarak terpendek dari source ke semua kota lain menggunakan algoritma Dijkstra."""
        distance = {}
        for city in self.city_list:
            distance[city] = float('inf')
        distance[source] = 0

        unvisited_cities = list(self.city_list.keys())

        while unvisited_cities:
            min_distance = float('inf')
            closest_city = None
            for city in unvisited_cities:
                if distance[city] < min_distance:
                    min_distance = distance[city]
                    closest_city = city

            unvisited_cities.remove(closest_city)

            for neighbor, jarak in self.city_list[closest_city].items():
                jarakNeighbor = distance[closest_city] + jarak
                if jarakNeighbor < distance[neighbor]:
                    distance[neighbor] = jarakNeighbor

        return distance

    def tsp(self, start_city):
        """Menghitung jalur dan jarak terpendek untuk mengunjungi semua kota dan kembali ke kota awal (TSP)."""
        from itertools import permutations
        cities = list(self.city_list.keys())
        cities.remove(start_city)
        shortest_path = None
        shortest_distance = float('inf')

        for path in permutations(cities):
            path = (start_city,) + path + (start_city,)
            total_distance = 0
            for i in range(len(path) - 1):
                total_distance += self.distance(path[i], path[i + 1])
            if total_distance < shortest_distance:
                shortest_distance = total_distance
                shortest_path = path
        return shortest_path, shortest_distance
    def tsp(self, start_city):
        """
        Menghitung jalur dan jarak terpendek untuk mengunjungi semua kota
        dan kembali ke kota awal (Traveling Salesperson Problem).
        """
        cities = list(self.city_list.keys())
        cities.remove(start_city)
        shortest_path = None
        shortest_distance = float('inf')

        for path in permutations(cities):
            path = (start_city,) + path + (start_city,)
            total_distance = 0
            for i in range(len(path) - 1):
                total_distance += self.distance(path[i], path[i + 1])
            if total_distance < shortest_distance:
                shortest_distance = total_distance
                shortest_path = path
        return shortest_path, shortest_distance

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
jarakSemuaKota = peta_jawa_timur.djikstra(source_city)

print(f"\nMenampilkan jarak terpendek dari kota {source_city} ke kota lain di Jawa Timur:\n")
for city, distance in jarakSemuaKota.items():
    if city != source_city:
        print(f"{source_city} -> {city}: {distance} KM")

print("\nJarak terpendek dalam format dictionary:")
print(jarakSemuaKota)

# Output TSP
shortest_tsp_path, shortest_tsp_distance = peta_jawa_timur.tsp(source_city)
print(f"\nJalur TSP terpendek: {shortest_tsp_path}")
print(f"Jarak TSP terpendek: {shortest_tsp_distance} KM")
