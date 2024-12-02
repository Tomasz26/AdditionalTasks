dice = {}
key = []


for i in range(0, 11):
  key.append(i+2)

print(f"Dostępne wartości z rzutów: {key}")

i = 1

for value in key:
  dice[value] = []
  a = 1
  while a >= 1:
    a = value - i
    b = i
    if a<=6 and b<=6 and a > 0 and b > 0:
      dice[value].append((a, b))
    i += 1
  i = 1

print(f"Słownik możliwych rzutów dla danych wartości: {dice}")