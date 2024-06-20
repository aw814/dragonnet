from numpy import load
INDEX = 0
data = load(f'./ihdp/dragonnet/{INDEX}/simulation_outputs.npz')  # Notice the f before the string
lst = data.files
for item in lst:
    print(item)
    print(data[item])
