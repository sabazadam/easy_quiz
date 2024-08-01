# 1) Aşağıdaki sözlükte, değerler içinde c harfinin geçip geçmediğini gösteren bir if koşulu yazınız
import random
my_dictionary = {"k1":10,"k2k":"a","k32":30,"k4":"c"}
if "c" in my_dictionary.values():
    print("c harfi var")

# 2) Aşağıdaki listedeki sayılardan sadece çift sayı olanları başka bir listeye kaydeden bir kod yazınız.

my_numbers = [1,2,3,4,5,6,19,20,32,21,20,1111,23,24]
new_list = [num for num in my_numbers if num % 2 == 0]
print(new_list)

# 3) Tüm dairelerin çevresini içeren başka yeni bir liste oluşturunuz. (İpucu: 2 * pi * r)  Pi 3.14 alınabilir.

r_list = [3,2,5,8,4,6,9,12]

circumference = [r * 2 * 3.14 for r in r_list]
print(circumference)
# 4) Aşağıdaki listede isim - yaş eşleşmelerinin bulunduğu yapılar mevcuttur. Sadece yaşların olduğu yeni ve ayrı bir liste oluşturunuz.

age_name_list = [("Ahmet",30),("Ayse",24),("Mehmet",40),("Fatma",29)]
age_list = [age[1] for age in age_name_list ]

print(age_list)
# 5) Aşağıdaki müzik gruplarından birini rastgele yazdıran bir kod yazınız

metal_list = ["Metallica","Iron Maiden","Dream Theater","Megadeth","AC/DC"]
print(random.choice(metal_list))

# 6) Aşağıdaki kodun çıktısı ne olacaktır?

number_list = [5,7,18,21,20,10,405,24]

# [num % 2 == 0 for num in number_list]
output = [1,1,0,1,0,0,1,0]

#7) Aşağıdaki string dizisinde, içinde sadece XYZ geçen barkodları gösterecek yeni bir liste oluşturunuz

barcodeList = ["ABC231","SA3123XYZ","XYZA123Q","QRE1231KJ","X112QGL"]
xyz_barcodeList = [code for code in barcodeList if "XYZ" in code]
print(xyz_barcodeList)
#8) Aşağıda yazdırılan sınıfı incelediğinizde my_cat.multiply_age() kodunun çıktısı ne olacaktır?


class Cat:
    def __init__(self, name, age=5):
        self.name = name
        self.age = age

    def multiply_age(self):
        return self.age * 3

my_cat = Cat("Whiskers")
#my_cat.multiply_age()  -> 15