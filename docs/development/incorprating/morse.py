import numpy as np
import sys, os, yaml

def Vmorse(r,De, a, re):
    """Calculate the Morse potential, V(r).
    """
    return De * (1.0 - np.exp(-a*(r - re)))**2.0 - De


if __name__ == '__main__':
    
    with open('rendered_wano.yml') as file:
        wano_file = yaml.full_load(file)

    decimal_points = 6 # decimal points

    De = wano_file["De (Ry)"] #0.48 #Ry
    a =  wano_file["a"] #1.8 
    re = wano_file["re (A)"] #0.8 #Angs
    r = wano_file["Mol_distance (A)"]  #0.4 #Angs
    
    # get morse potential energy
    ymorse = Vmorse(r, De, a, re)

    MOROUT = wano_file  # output file
    
    MOROUT["energy"] = float(round(ymorse,decimal_points))
    try:   
        with open("MOROUT.yml",'w') as out:
            yaml.dump(MOROUT, out,default_flow_style=False)
    except IOError:
        print("I/O error")
