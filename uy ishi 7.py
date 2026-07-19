# Asosiy klass
class Shaxs:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh

    def malumot(self):
        return f"Ism: {self.ism}, Yosh: {self.yosh}"


# O'quvchi klassi
class Oquvchi(Shaxs):
    def __init__(self, ism, yosh, sinf):
        super().__init__(ism, yosh)
        self.sinf = sinf

    def malumot(self):
        return f"Ism: {self.ism}, Yosh: {self.yosh}, Sinf: {self.sinf}"


# Kitob klassi
class Kitob:
    def __init__(self, nomi, muallif):
        self.nomi = nomi
        self.muallif = muallif
        self.oquvchilar = []   # Bo'sh ro'yxat

    # Kitob berish
    def berish(self, oquvchi):
        self.oquvchilar.append(oquvchi)
        print(f"{oquvchi.ism} ga '{self.nomi}' kitobi berildi.")

    # Kitobni qaytarish
    def qaytar(self, oquvchi):
        if oquvchi in self.oquvchilar:
            self.oquvchilar.remove(oquvchi)
            print(f"{oquvchi.ism} '{self.nomi}' kitobini qaytardi.")
        else:
            print("Bu kitob sizda emas.")

    def malumot(self):
        print(f"\nKitob: {self.nomi}")
        print(f"Muallif: {self.muallif}")

        if self.oquvchilar:
            print("O'quvchilar:")
            for i in self.oquvchilar:
                print("-", i.ism)
        else:
            print("Hech kim olmagan.")


# Kutubxona klassi
class Kutubxona:
    def __init__(self, nomi):
        self.nomi = nomi
        self.kitoblar = []

    def kitob_qoshish(self, kitob):
        self.kitoblar.append(kitob)

    def korsat(self):
        print(f"\n{self.nomi} kutubxonasidagi kitoblar:")
        for kitob in self.kitoblar:
            print("-", kitob.nomi)


# Kutubxonachi klassi (Shaxsdan meros oladi)
class Kutubxonachi(Shaxs):
    def __init__(self, ism, yosh, ish_staji):
        super().__init__(ism, yosh)
        self.ish_staji = ish_staji

    def malumot(self):
        return f"Kutubxonachi: {self.ism}, Yosh: {self.yosh}, Ish staji: {self.ish_staji} yil"


# =====================
# Obyektlar
# =====================

o1 = Oquvchi("Ali", 17, "11-A")
o2 = Oquvchi("Vali", 16, "10-B")

k1 = Kitob("Python", "Abdulloh")
k2 = Kitob("OOP", "Hasan")

kutubxona = Kutubxona("Markaziy")

kutubxona.kitob_qoshish(k1)
kutubxona.kitob_qoshish(k2)

# Kitob berish
k1.berish(o1)
k1.berish(o2)

# Ma'lumot
k1.malumot()

# Kitob qaytarish
k1.qaytar(o1)
k1.qaytar(o1)   # Ro'yxatda yo'q

# Kutubxona
kutubxona.korsat()

# Kutubxonachi
kutubxonachi = Kutubxonachi("Sardor", 35, 10)
print("\n" + kutubxonachi.malumot())s