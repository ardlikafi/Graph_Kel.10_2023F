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
kota_list_jawa_timur = ["Surabaya", "Malang", "Sidoarjo", "Madiun", "Jombang", "Tuban", "Lamongan", "Probolinggo", 
                        "Pasuruan", "Banyuwangi", "Bondowoso", "Tulungagung", "Ponorogo", "Magetan", "Ngawi", "Bojonegoro", 
                        "Kediri", "Blitar", "Trenggalek", "Pacitan"]

for kota in kota_list_jawa_timur:
    peta_jawa_timur.tambahkanKota(kota)

edges_jawa_timur = [("Surabaya", "Malang"), ("Surabaya", "Sidoarjo"), ("Malang", "Sidoarjo"), ("Malang", "Madiun"), 
                    ("Madiun", "Jombang"), ("Jombang", "Tuban"), ("Tuban", "Lamongan"), ("Lamongan", "Probolinggo"), 
                    ("Probolinggo", "Pasuruan"), ("Pasuruan", "Banyuwangi"), ("Banyuwangi", "Bondowoso"), ("Bondowoso", "Tulungagung"), 
                    ("Tulungagung", "Ponorogo"), ("Ponorogo", "Magetan"), ("Magetan", "Ngawi"), ("Ngawi", "Bojonegoro"), 
                    ("Bojonegoro", "Kediri"), ("Kediri", "Blitar"), ("Blitar", "Trenggalek"), ("Trenggalek", "Pacitan")]

for edge in edges_jawa_timur:
    peta_jawa_timur.tambahkanJalan(edge[0], edge[1])

peta_jawa_timur.printPeta()