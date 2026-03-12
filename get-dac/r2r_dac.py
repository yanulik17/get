import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

class R2R_DAC:
    def __init__(self, gpio_bits, dynamic_range, verbose = False):
        self.gpio_bits = gpio_bits
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.gpio_bits, GPIO.OUT, initial = 0)

    def set_number(self, number):
        if number < 0 or number > 255:
            print("Ошибка: число вне диапазона 0-255. Устанавлиается 0. \n")
            number = 0
        for i, pin in enumerate(self.gpio_bits):
            state = (number >> i) & 1
            GPIO.output(pin, state)



    def set_voltage(self, voltage):
        if not(0.0 <= voltage <= dynamic_range):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.0 - {dynamic_range:.2f} В \n")
            print("Устанавливаем 0.0 В\n")
            number = 0
        else:
            number = int(voltage / self.dynamic_range * 255)

        self.set_number(number)      

        def deinit(self):
            GPIO.output(self.gpio_bits, 0)
            GPIO.cleanup()

if __name__ == "__main__":
    try:
        dac = R@R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.183, verbose=True)

        while True:
            try:
                voltage = float(input("Введите напряжение: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("Вы ввели не число. Попробуйте еще раз. \n")
    
    finally:
        dac.deinit()

