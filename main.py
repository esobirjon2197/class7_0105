
# 7-m
class Device:
    def __init__(self, brand, power, warranty):
        self.brand = brand
        self.power = power
        self.warranty = warranty

    def turn_on(self):
        print(f"{self.brand} yoqildi")


class Phone(Device):
    def __init__(self, brand, power, warranty, model, sim_count):
        super().__init__(brand, power, warranty)
        self.model = model
        self.sim_count = sim_count

    def turn_on(self):
        super().turn_on()
        print(f"Model: {self.model}, SIM: {self.sim_count}")

    def call(self):
        print("Qo‘ng‘iroq qilinmoqda...")


p = Phone("Samsung", "4000mAh", "1 yil", "A15", 2)
p.turn_on()
p.call()
