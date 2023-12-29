import d20
import sys
from prettytable import PrettyTable

itr = 10000
target = int(sys.argv[1])
bonus = int(sys.argv[2])

results = [0, 0, 0, 0]
for _ in range(itr):
    rolls = [
        d20.roll(f"2d20kh1+1d4+{bonus}").total,
        d20.roll(f"2d20kh1+1d4+{bonus}").total,
        d20.roll(f"2d20kh1+1d4+{bonus}").total,
    ]
    success = sum([x >= target for x in rolls])
    results[success] = results[success] + 1

# Transform into percentages
results = [(x * 100) / itr for x in results]

print(f"Crafting DC:    {target}")
print(f"Crafting Bonus: {bonus}")

x = PrettyTable()

x.field_names = ["Failure", "Success"]
x.add_row([results[0] + results[1], results[2] + results[3]])
x.float_format = "2.2"
print(x)

x.clear()

x.field_names = ["Write Off", "Salvage", "Crafted", "Masterworked"]
x.add_row([results[0], results[1], results[2], results[3]])
x.float_format = "2.2"
print(x)