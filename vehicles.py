# dictionary of DC heroes and their vehicles. Nested set for Batman
# to account for multiple vehicles
vehicles = {"Wonder Woman": "Invisible Plane",
            "The Flash": None,
            "Batman": {"Tumbler", "Batmobile", "The Bat", "Batpod"}
            }
# print a list of thhe hero's vehicles
for heroes in vehicles:
    vehicle = vehicles[heroes]
    # we need a nested loop for Batman because he has multiple vehicles
    if heroes == "Batman":
        batvehicles = vehicles["Batman"]
        print(f"{heroes}'s vehicles:")
        for results in batvehicles:
            print(f"* {results}")
    else:
        print(f"{heroes}'s vehicles:")
        print(f"* {vehicle}")
    print("\n")
