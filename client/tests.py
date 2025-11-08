#editado

from onlinevars import OnlineVars

client = OnlineVars()


print("\n--- Initial State ---")
variables = client.list()
assert(variables==[])


print("\n--- Creating 'greeting' ---")
status, text = client.set("greeting", "Hello, World!")
assert(status==201)
assert(text=="created")


print("\n--- Creating 'counter' ---")
client.set("counter", 100)


print("\n--- Listing all variables ---")
variables = client.list()
assert(variables==["counter","greeting"])


print("\n--- Getting a specific variable ---")
greeting_value = client.get("greeting")
assert(greeting_value=="Hello, World!")


print("\n--- Updating 'greeting' ---")
status, text = client.set("greeting", "Hello, API Client!")
assert(status==200)
assert(text=="updated")


print("\n--- Getting the updated variable ---")
greeting_value = client.get("greeting")
assert(greeting_value=="Hello, API Client!")


print("\n--- Deleting 'counter' ---")
client.rem("counter")


print("\n--- Getting a deleted variable ---")
counter_value = client.get("counter")
assert(counter_value==None)


print("\n--- Final State ---")
variables = client.list()
assert(variables==["greeting"])


print("\n--- Testing invalid variable name ---")
nullvar = client.get("invalid-name!")
assert(nullvar==None)


print("\n Passed all tests!!!")
