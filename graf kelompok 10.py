class Peta:
    def __init__(self):
        self.cityList = {}
    
    def printPeta(self):
        for kota in self.cityList:
            print(kota, ":", self.cityList[kota])
    
    def tambahkanKota(self, kota):
        if kota not in self.cityList:
            self.cityList[kota] = []
            return True
        return False
    
    def tambahkanJalan(self, kota1, kota2):
        if kota1 in self.cityList and kota2 in self.cityList:
            self.cityList[kota1].append(kota2)
            self.cityList[kota2].append(kota1)
            return True
        return False

peta_jawa_timur = Peta()
kota_list_jawa_timur = ["Surabaya", "Malang", "Sidoarjo", "Madiun", "Situbondo", "Tuban", "Lamongan", "Probolinggo", 
                        "Pasuruan", "Banyuwangi", "Bondowoso", "Tulungagung", "Ponorogo", "Nganjuk", "Ngawi", "Bojonegoro", 
                        "Kediri", "Blitar", "Trenggalek", "Pacitan"]

for kota in kota_list_jawa_timur:
    peta_jawa_timur.tambahkanKota(kota)

edges_jawa_timur = [("Surabaya", "Sidoarjo"), ("Surabaya", "Lamongan"), ("Malang", "Sidoarjo"), ("Situbondo", "Bondowoso"), ("Bondowoso", "Pasuruan"), ("Malang", "Pasuruan"), 
                    ("Madiun", "Ngawi"), ("Madiun", "Nganjuk"), ("Bojonegoro", "Tuban"), ("Tuban", "Lamongan"), ("Lamongan", "Bojonegoro"), 
                    ("Probolinggo", "Pasuruan"), ("Tulungagung", "Trenggalek"), ("Situbondo", "Banyuwangi"), ("Banyuwangi", "Bondowoso"), ("Bondowoso"), 
                    ("Ponorogo", "Nganjuk"), ("Nganjuk", "Ngawi"), ("Situbondo", "Probolinggo"), ("Ngawi", "Bojonegoro"), 
                    ("Nganjuk", "Kediri"), ("Kediri","Tulungagung"),("Blitar", "Malang"), ("Blitar", "Tulungagung"), ("Trenggalek", "Ponorogo"), ("Pacitan", "Ponorogo"), ("Trenggalek", "Pacitan")]

for edge in edges_jawa_timur:
    peta_jawa_timur.tambahkanJalan(edge[0], edge[1])

peta_jawa_timur.printPeta()
