import random
import numpy as np

dungeon_dataset = []
for x in range(500):
  # Generate a random M between 3 and 19
  M = random.randint(2, 21)
  N = random.randint(2, 21)


  # Create an MxN array of zeroes
  array = [[0 for _ in range(N)] for _ in range(M)]

  # Print M, N, and the array
  print(f"M = {M}, N = {N}")
  my_dict = {}
  lengthened = False
  counter = 0

  for i in range(M):
    if (M < N/2 and M >= 3):
        if(i != 0):
          smaller = my_dict[i-1] - (N//2)
          bigger = my_dict[i-1] + (N//2)
          randomLocation = random.randint(smaller, bigger)
          if(my_dict[i-1] < randomLocation ):
            randomLocation += N//2
          elif(my_dict[i-1] > randomLocation):
            randomLocation -= N//2
          if(randomLocation < 0):
            randomLocation = 0
          elif(randomLocation > N-1):
            randomLocation = N-1
          elif(randomLocation == i):
            if(randomLocation < N//2):
              randomLocation + random.randint(N//4, N//2)
            elif(randomLocation > N//2):
              randomLocation - random.randint(N//4, N//2)
            else:
              randomLocation - random.randint(-N//2, N//2)
        else:
          randomLocation = random.randint(0,N-1)

    elif (counter > 2):
      lengthened = False
      counter = 0
    if (lengthened == True):
      smaller = my_dict[i-1] - 2
      bigger = my_dict[i-1] + 2
      if(smaller < 0):
        smaller = 0
      if(bigger > N-1):
        bigger = N-1
      randomLocation = random.randint(smaller, bigger)
      counter += 1
    else:
      randomLocation = random.randint(0,N-1)
    if (randomLocation >= 5):
      lengthened = True

    array[i][randomLocation] = 1
    my_dict[i] = randomLocation



  for i in range(M-1):
    if (my_dict[i] != my_dict[i+1]):
      if(my_dict[i] > my_dict[i+1]):
        greater = my_dict[i]
        lesser = my_dict[i+1]
      else:
        greater = my_dict[i+1] + 1
        lesser = my_dict[i]+1
      if lesser == greater:
        array[i][lesser] = 1
      for j in range(lesser, greater):
        array[i][j] += 1
  arrayNP = np.array(array)
  instance = {"layout": arrayNP, "size": arrayNP.shape}
  dungeon_dataset.append(instance)
  
print(len(dungeon_dataset))  

for i in dungeon_dataset:
  print("M = " + str(i['size'][0]) + ", N = " + str(i['size'][1]))
  if(i['size'][0] < i['size'][1]/2):
    print("this one is a weird one")
  print(i['layout'], end="\n\n")

# Save the array to a file
np.save("dungeon.npy", dungeon_dataset, allow_pickle=True)
