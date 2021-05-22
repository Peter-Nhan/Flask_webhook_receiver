import base64
  
user_pass = "username:password"
username = input ("Enter Username: ")
password = input ("Enter Password: ")
user_pass = username + ":" + password
print(user_pass)
user_pass_bytes = user_pass.encode("ascii")
base64_bytes = base64.b64encode(user_pass_bytes)
base64_string = base64_bytes.decode("ascii")
  
print(f"Encoded string: {base64_string}")

print("Header for Basic Authentication")
print("Authorization Header value: " + f"Basic {base64_string}")
