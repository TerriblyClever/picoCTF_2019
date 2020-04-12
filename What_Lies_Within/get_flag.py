#a quick script to extract a hidden message from an image
from stegano import lsb
from stegano import lsbset
from stegano import red

secret = lsb.hide("buildings_test.png", "Hello World")
secret.save("buildings_secret.png")

hidden_message = lsb.reveal("buildings_secret.png")
print(hidden_message)

hidden_message = lsb.reveal("buildings.png")
print(hidden_message)
