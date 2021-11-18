import phonenumbers
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode
print("\n")
number = input("Enter a phone number with country code : ")
print("\n")
print("Information of :" + number)
print("_________________________________________________")
Key = "a942af39052c4d55908efe5c3a6813f5"
num = phonenumbers.parse(number)
from phonenumbers import geocoder
country = geocoder.description_for_number(num, "en")
print("Country : " + country)
print("\n")
service_provider = phonenumbers.parse(number)
sp = carrier.name_for_number(service_provider, "en")      # prints the service provider
print("Service Provider : " + sp)
print("\n")
geocoder = OpenCageGeocode(Key)
query = str(country)
result = geocoder.geocode(query)
lat = result[0]['geometry']['lat']
lng = result[0]['geometry']['lng']
a = str(lat) + " , " + str(lng)
print("Location : " + a + " (Approximate Location)")
print("_________________________________________________")
