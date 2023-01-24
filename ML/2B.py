#B. For a given set of training data examples stored in .CSV file, implement and demonstrate the CandidateElimination algorithm to output a description of the set of all hypotheses consistent with the training examples.

import numpy as np
import pandas as pd

data = pd.read_csv(r'Dataset.csv')
concepts = np.array(data.iloc[:, 0:-1])
print("\nInstances are:\n", concepts)
target = np.array(data.iloc[:, -1])
print("\nTarget Values are: ", target)

def learn(concepts, target):
      specific_h = concepts[0].copy()
      print("\nInitialization of specific h and genearal h")
      print("\nSpecific Boundary: ", specific_h)
      general_h = [["?"for i in range(len(specific_h))] for i in range(len(specific_h))]
      print("\nGeneric Boundary: ", general_h)

      for i, h in enumerate(concepts):
            print("\nInstance", i + 1, "is ", h)
            if target[i] == "Yes":
                  print("Instance is Positive")
            for x in range(len(specific_h)):
                  if h[x] != specific_h[x]:
                        specific_h[x] = '?'
                        general_h[x][x] = '?'
                        if target[i] == "No":
                              print("Instance is Negative ")
                  for x in range(len(specific_h)):
                        ifh[x] != specific_h[x]:
                        general_h[x][x] = specific_h
                        else:
                        general_h[x][x] = '?'
                        print("Specific Bundary after "
                        print("Generic Boundary after "
                        print("\n")
                        indices = [ifori, valinenumerate
                                   '?', '?', '?']]
                        foriinindices:
                        general_h.remove(['?', '?',
                                          returnspecific_h, general_h
                                          s_final, g_final = learn(concepts
                        print("Final Specific_h: ",
                              print("Final General_h: ", g_final

                        specific_h[x]
                        "Specific Bundary after ", i + 1, "Instance is ", specific_h
                        "Generic Boundary after ", i + 1, "Instance is ", general_h
                        enumerate(general_h)
                        ifval == ['?', '?',
                        , '?', '?', '?', '?'])
                        concepts, target)
                        , s_final, sep = "\n")
                        g_final, sep = "\n")
                        specific_h)
                        general_h)
                        '?',