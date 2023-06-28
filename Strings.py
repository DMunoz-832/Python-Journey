# The following text was provided from a random sentence generator

phrase = "hand sanitizer"

print(phrase.lower())
print("Is the above text upper case: ", phrase.isupper())

print("----------------")

test = len(phrase)
print("Length of " + phrase + " is: ", test)

print("----------------")

print(phrase[3])
print(phrase[8])
print(phrase[13])
print(phrase[9])

print(phrase.index("d san"))
print(phrase.replace("hand", "Eye"))

print("----------------")

print("The hand sanitizer was\n ...\"clear\" glue.")

print("----------------")

print(phrase.swapcase())

print("----------------")

testing_text = input("Please enter secret word:\n")
# examples: aåb∫cçd∂e´´´ƒg©1¡ ; wi@vår!05v
bytes_encoded = testing_text.encode()
testing_decoded = bytes_encoded.decode()

print("Encoded bytes = ", bytes_encoded)
print("Decoded bytes = ", testing_decoded)
print("testing_text equals testing_decoded = ", testing_text == testing_decoded)

print("----------------")
