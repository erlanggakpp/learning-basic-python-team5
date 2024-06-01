# try:
#     a = 10
#     b = 2
#     if b == 0: 
#         raise Exception("Sorry, no numbers below zero")
#     if b == 2:
#         raise Exception("JANGAN KASIH 2")

#     result = 10 / 0
# except Exception as e:
#     print(f"An error occurred: {e}")
#     print(f"Error type: {type(e).__name__}")

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 2, "a": 1, "c": 2}
print(dict1 == dict2)