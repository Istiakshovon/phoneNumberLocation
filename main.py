import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

number = "+237 6 99 78 05 59"

ch_number = phonenumbers.parse(number,"CH")
print(geocoder.description_for_number(ch_number, "en"))

service_number = phonenumbers.parse(number,"RO")
print(carrier.name_for_number(service_number,"en"))