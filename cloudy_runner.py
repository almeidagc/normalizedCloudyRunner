#-----------------------------Instructions -------------------------------------------------------------------------
# Remember to adjust the path for Cloudy execution in the 'command' variable (line 63);
# In Cloudy version c17, 'normalize' should be changed to 'normalise' ( line 35);
# Carvalho et al. (2020) - doi: 10.1093/mnras/staa193 (line 25)
# Dors et al. (2022) - doi: 10.1093/mnras/stac1722 (line 22)

import os
import numpy as np

aox = np.arange (-1.1, -1, 0.1)
u = np.arange (-4.0, -3.5, 0.5)
d = np.arange (99, 100, 1)
z = np.arange (2, 2.1, 0.1)


for val_aox in aox:
	for val_u in u:
		for val_d in d:
			for val_z in z:
				oh = 12 + (np.log10(val_z * (10 ** -3.31)))
												
				he = 0.1215 * oh**2 - 1.8183 * oh + 17.6732
				he_sol = 11.00
				
				no = 1.29 * oh - 11.84
				nh = (no+(oh-12))
				
				n_scale = (10**nh)/(val_z*(10**-4.07))
				
				file_name = f'agn_aox{val_aox:.2f}_U{val_u:.2f}_d-{val_d:.2f}_z-{val_z:.2f}.in'
				file = open (file_name, "w")
				file.write ("agn 1.5e5 k, a(ox)= " + str (val_aox) + ", a(uv)= -1.0 \n")      
				file.write ("ionization parameter "+ str (val_u) + "\n")
				file.write ("hden " + str (val_d) + " linear \n")
				file.write ('normalize to "H  1" 4861.36A  [scale factor= 100.0] \n')
				file.write ("metals scale " + str (val_z) + "\n")
				file.write ("element nitrogen scale " + str (n_scale) + "\n")
				file.write ("element helium scale " + str (he/he_sol) + "\n")  
				file.write ("element sulphur scale 1.20 \n")
				file.write ("filling factor 0.01  \n")
				file.write ("iterate 2  \n")
				file.write ("print last  \n")
				file.write ("cosmic rays background linear 40\n")
				file.write ("stop temperature 1000 K\n")
				file.close ()
				
#------------------------------------running outputs-----------------------------------------------------------------------------------------

directory = os.getcwd()			
file_in = os.listdir(directory)

files = []

for input_file in file_in:
    if input_file.endswith('.in'):
        files.append(input_file)

for input_file in files:
    output_file = input_file.replace('.in', '.out')
    
    print(f"Running model {input_file}, please wait...\n")
    
    command = f"/home/user/cloudy/c23.00/source/cloudy.exe < {input_file} > {output_file}"
    os.system(command)
    
    print(f"The file '{output_file}' for the model '{input_file}' is ready!\n")