import requests
import API_setup
import hashlib
import hmac


host_API = "https://sandbox-authservice.priaid.ch/login"

my_hmac = hmac.new(api_key, [], hashlib.md5)

print("hope this works " + str(my_hmac_cpy.digest()))