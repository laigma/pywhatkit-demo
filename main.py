import pywhatkit

print("Introduce número (+34 xxx xx xx xx):")
phone_number = input()

print("Introduce mensaje:")
message = input()

print("Introduce hora de envío:")
hour = input()

print("Introduce minuto de envío:")
minute = input()

pywhatkit.sendwhatmsg(phone_number, message, int(hour), int(minute), 45)
