import phonenumbers
from phonenumbers import timezone,geocoder,carrier   #carrier show sim knowlede

number=input("Enter your phone number  with +1_ +91_ +63:")

phone=phonenumbers.parse(number)                        #parse give phone number details

time=timezone.time_zones_for_geographical_number(phone)

car=carrier.name_for_number(phone,"en")            #en means whatever they show name in english

reg=geocoder.description_for_number(phone,"en")     #geocoder give phone number details

print(phone)
print(time)
print(car)
print(reg)

