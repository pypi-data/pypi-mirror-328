# SAMBA_ilum Copyright (C) 2024 - Closed source

from pymatgen.io.vasp import Poscar
from pymatgen.core import Structure
from pymatgen.symmetry.analyzer import SpacegroupAnalyzer
#--------------------------------------------------------
import numpy as np
import shutil
import json
import uuid
import sys
import os


pseudo_type = 'PAW_PBE'
exchange_correlation_functional = 'GGA'
vdW = 'optB86b'


# replace_type_pseudo
# replace_type_XC
# replace_type_vdW


# =========================================
# Verificando arquivos da sereme lidos: ===
# =========================================
l_file = 'null';  l_file_SO = 'null'
if os.path.isfile('output/info_scf.txt'):       l_file = 'info_scf.txt'
if os.path.isfile('output/info_bands.txt'):     l_file = 'info_bands.txt'
if os.path.isfile('output/info_scf_SO.txt'):    l_file_SO = 'info_scf_SO.txt'
if os.path.isfile('output/info_bands_SO.txt'):  l_file_SO = 'info_bands_SO.txt'
if (l_file == 'null' and l_file_SO == 'null'):  sys.exit(0)


#==========================================================
# Extraindo o k-path para o plot da Estrutura de Bandas ===
#==========================================================
kpoints_file = []
kpath = []
#---------
if os.path.isdir('output/Bandas'):     dir_kpath = 'bands'
if os.path.isdir('output/Bandas.SO'):  dir_kpath = 'bands.SO'
#-----------------------------------------------------------------------------
if os.path.isfile(dir_kpath + '/' + 'KPOINTS'): kpoints_file.append('KPOINTS')
#--------------------------------------------------------------------------------------
nkpoints = len([file for file in os.listdir(dir_kpath) if file.startswith("KPOINTS.")])
for i in range(nkpoints):
    file = 'KPOINTS.' + str(i+1)
    if os.path.isfile(dir_kpath + '/' + file): kpoints_file.append(file)
#---------------------------------
for i in range(len(kpoints_file)):
    #-----------------------------
    with open(dir_kpath + '/' + kpoints_file[i], 'r') as file: lines = file.readlines()
    #----------------------------------------------------------------------------------
    if (len(kpoints_file) == 1):
       for j in range(len(lines)):
           if (j > 3 and len(lines[j]) > 1):
              line = lines[j].split()
              line[3] = line[3].replace('!', '').replace('#1', 'Gamma').replace('#', '')
              kpath.append([float(line[0]), float(line[1]), float(line[2]), str(line[3])])
    #-------------------------------------------------------------------------------------
    if (len(kpoints_file) > 1):
       for j in range(len(lines)):
           if (i == 0 and j > 3 and len(lines[j]) > 1):
              line = lines[j].split()
              line[3] = line[3].replace('!', '').replace('#1', 'Gamma').replace('#', '')
              kpath.append([float(line[0]), float(line[1]), float(line[2]), str(line[3])])
           if (i > 0  and j > 4 and len(lines[j]) > 1):
              line = lines[j].split()
              line[3] = line[3].replace('!', '').replace('#1', 'Gamma').replace('#', '')
              kpath.append([float(line[0]), float(line[1]), float(line[2]), str(line[3])])
#----------------------------------------------------------
# Removendo elementos adjacentes e repetidos da lista kpath
#----------------------------------------------------------
i = 0
while i < (len(kpath) -1):
    if kpath[i] == kpath[i +1]: del kpath[i +1]
    else: i += 1  # Avança para o próximo par de elementos


# ===================================================
# Iniciando tags com valores vazios "--" ============
# ===================================================
area_perc_mismatch = '--';  perc_area_change = '--';  perc_mod_vectors_change = '--';
angle_perc_mismatch = '--';  perc_angle_change = '--';  rotation_angle = '--';
supercell_matrix = '--';  deformation_matrix = '--';  strain_matrix = '--'
shift_plane = '--'

# ============================================================
# Extraindo informações de configuração da Heteroestrutura ===
# ============================================================
if os.path.isfile('output/POSCAR.info'):
   #---------------------------------------
   poscar = open('output/POSCAR.info', "r")
   VTemp = poscar.readline().split()
   param = float(poscar.readline())
   poscar.close()
   #------------------------
   if (VTemp[0] == 'SAMBA'):
      #----------------------------------------------------------------
      l_materials = VTemp[1].replace('+', ' ').replace('_', '').split()
      n_materials = len(l_materials)
      #------------------------------------------
      r_ions_materials = []; nions_materials = []
      nion = 0;  passo = 0
      #-----------------------------
      for m in range(n_materials):
          r_ions_materials.append( str(1 + nion) + ':')
          nion += int(VTemp[m+2])
          r_ions_materials[m] += str(nion)
          nions_materials.append(int(VTemp[m+2]))
      #------------------------------------------
      id_materials = []
      #--------------------


      if (n_materials > 1):
         #----------------------------------------------------------------------
         area_perc_mismatch = []; angle_perc_mismatch = [];  rotation_angle = []
         perc_area_change = [];  perc_mod_vectors_change = [];  perc_angle_change = []
         supercell_matrix = [];  deformation_matrix = [];  strain_matrix = []
         shift_plane = []
         #---------------------
         passo = n_materials +1
         passo += 4
         temp1 = str(VTemp[passo]).replace('_', ' ').split()
         area_perc_mismatch.append([float(temp1[0]), float(temp1[1])])
         if (n_materials == 3):
            area_perc_mismatch.append([float(temp1[2]), float(temp1[3])])
         #---------------------------------------------------------------
         passo += 4
         temp1 = str(VTemp[passo]).replace('_', ' ').split()
         for ii in range(len(temp1)): perc_area_change.append(float(temp1[ii]))
         #---------------------------------------------------------------------
         passo += 4
         temp1 = str(VTemp[passo]).replace('_', ' ').split()
         perc_mod_vectors_change.append([float(temp1[0]), float(temp1[1])])
         perc_mod_vectors_change.append([float(temp1[2]), float(temp1[3])])
         if (n_materials == 3):
            perc_mod_vectors_change.append([float(temp1[4]), float(temp1[5])])
         #--------------------------------------------------------------------
         passo += 4
         temp1 = str(VTemp[passo]).replace('_', ' ').split()
         angle_perc_mismatch.append([float(temp1[0]), float(temp1[1])])
         if (n_materials == 3):
            angle_perc_mismatch.append([float(temp1[2]), float(temp1[3])])
         #----------------------------------------------------------------
         passo += 4
         temp1 = str(VTemp[passo]).replace('_', ' ').split()
         for ii in range(len(temp1)): perc_angle_change.append(float(temp1[ii]))
         #----------------------------------------------------------------------
         passo += 4
         temp1 = str(VTemp[passo]).replace('_', ' ').split()
         for ii in range(len(temp1)): rotation_angle.append(float(temp1[ii]))
         #-------------------------------------------------------------------
         for i in range(n_materials):
             passo += 4
             temp1 = str(VTemp[passo]).replace('_', ' ').split()
             supercell_matrix.append([[int(temp1[0]), int(temp1[1])], [int(temp1[2]), int(temp1[3])]])
         #--------------------------------------------------------------------------------------------
         for i in range(n_materials):
             passo += 4
             temp1 = str(VTemp[passo]).replace('_', ' ').split()
             deformation_matrix.append([[float(temp1[0]), float(temp1[1])], [float(temp1[2]), float(temp1[3])]])
         #------------------------------------------------------------------------------------------------------
         for i in range(n_materials):
             passo += 4
             temp1 = str(VTemp[passo]).replace('_', ' ').split()
             strain_matrix.append([[float(temp1[0]), float(temp1[1])], [float(temp1[2]), float(temp1[3])]])
         #-------------------------------------------------------------------------------------------------
         passo += 4
         temp1 = str(VTemp[passo]).replace('_', ' ').split()
         for ii in range(len(temp1)): shift_plane.append(float(temp1[ii]))
         #----------------------------------------------------------------
         passo += 1
         for i in range(n_materials):
             id_materials.append(str(VTemp[-n_materials -1 +i]))
      #--------------------------------------------
      temp_id = VTemp[-1].replace('_', ' ').split()
      if (len(temp_id) > 1): estequiometria = temp_id[0]
      id_code = VTemp[-1]
   #-------------------------------------------------------
   if (n_materials == 1): id_materials.append(str(id_code))
   #-------------------------------------------------------
   if (VTemp[0] != 'SAMBA'): exit()
   #-------------------------------


# ============================================================
# Extraindo informações de configuração da Heteroestrutura ===
# ============================================================
poscar = open('output/POSCAR.info', "r")
VTemp = poscar.readline().split()
materials = VTemp[1].replace('+', ' ').split()
#---------------------------------------------
t_ions_materials = []
for i in range(len(materials)):
    ions_vector = []
    mat_temp = materials[i].replace('_', ' ').split()
    for j in range(len(mat_temp)): 
        ions_vector.append(str(mat_temp[j]))
    t_ions_materials.append(ions_vector)
#-------------------------------------------
for i in range(6): VTemp = poscar.readline().split()
t_nions_materials = [];  number = -1
for i in range(len(materials)):
    nions_vector = []
    mat_temp = materials[i].replace('_', ' ').split()
    for j in range(len(mat_temp)):
        number += 1
        nions_vector.append(int(VTemp[number]))
    t_nions_materials.append(nions_vector)
#-------------
poscar.close()
#-------------


# ==========================================
# Extraindo as posições dos ions da Rede ===
# ==========================================
poscar = open('output/CONTCAR', "r")
for i in range(5): VTemp = poscar.readline()
type_ions = poscar.readline().split()
type_ions_n = poscar.readline().split()
poscar.readline()
coord_ions = []
for i in range(len(type_ions)):
    for j in range(int(type_ions_n[i])):
        VTemp = poscar.readline().split()
        coord_ions.append([ float(VTemp[0]), float(VTemp[1]), float(VTemp[2]), str(type_ions[i]) ])
poscar.close()


# ========================================================
# Extraindo as espessuras e separação do(s) materiais ====
# ========================================================
thickness = []; temp_z = [];  z_separation = []
#----------------------------------------------
poscar = open('output/POSCAR.info', "r")
for i in range(8): VTemp = poscar.readline()
for i in range(nion):
    VTemp = poscar.readline().split()
    temp_z.append(float(VTemp[2]))
total_thickness = (max(temp_z) -min(temp_z))*param
poscar.close()
#---------------------------------------------------------
if (n_materials == 1): thickness.append( total_thickness )
#---------------------------------------------------------
if (n_materials > 1):
   poscar = open('output/POSCAR.info', "r")
   for i in range(8): VTemp = poscar.readline()
   for i in range(n_materials):
       temp_z = []
       for j in range(int(nions_materials[i])):
           VTemp = poscar.readline().split()
           temp_z.append(float(VTemp[2]))
       thickness.append( (max(temp_z) -min(temp_z))*param )
       #---------------------------------------------------------------
       if (i > 0): z_separation.append( (min(temp_z) -temp_max)*param )
       temp_max = max(temp_z)
       #---------------------
   poscar.close()   
#----------------


# =================================================
# Extraindo a Energia de Ligação ==================
# =================================================

if os.path.isfile('output/z-scan/info_z-scan.dat'):
   e_binding = '--'
   #--------------------------------------------------
   zscan = open('output/z-scan/info_z-scan.dat', "r")
   #--------------------------------------------------
   for i in range(5): VTemp = zscan.readline().split()
   e_binding = float(VTemp[2])
   #-------------
   zscan.close()

   # -------------------------------------
   # Atualizando a Energia de Ligação ----
   # -------------------------------------
   file_oszicar   = 'relax/OSZICAR'
   file_oszicar_f = 'relax/OSZICAR_frozen'
   #--------------------------------------
   if os.path.isfile(file_oszicar):
      if os.path.isfile(file_oszicar_f):
         #------------------------------------
         with open(file_oszicar, 'r') as file:
            lines = file.readlines()
            last_line = lines[-1].split()
            energ_r = float(last_line[2])
         #--------------------------------------
         with open(file_oszicar_f, 'r') as file:
            lines = file.readlines()
            last_line = lines[-1].split()
            energ_f = float(last_line[2])
         #-------------------------------
         e_binding += (energ_f - energ_r)


# =================================================
# Extraindo a Energia de Deslizamento =============
# =================================================
if os.path.isfile('output/xy-scan/info_xy-scan.dat'):
   e_slide = '--'
   #----------------------------------------------------
   xyscan = open('output/xy-scan/info_xy-scan.dat', "r")
   #----------------------------------------------------
   for i in range(6): VTemp = xyscan.readline().split()
   e_slide = float(VTemp[2])
   #-------------
   xyscan.close()


# ==========================================
# Splitando o arquivo POSCAR ===============
# ==========================================

if (n_materials > 1):

   #---------------------------------------
   poscar = open('output/POSCAR.info', 'r')
   #---------------------------------------
   VTemp = poscar.readline().split()
   label_materials = VTemp[1].replace('+', ' ').split()
   n_Lattice = len(label_materials);  nion = 0
   range_ion_Lattice = []; ntype_ions = ['']*n_Lattice           
   #--------------------------------------------------
   for m in range(n_Lattice):
       range_ion_Lattice.append( str(1 + nion) + ' ')
       nion += int(VTemp[m+2])
       range_ion_Lattice[m] += str(nion)
   #----------------------------------------------------
   for m in range(6):  VTemp = poscar.readline().split()
   #----------------------------------------------------
   poscar.close()
   #-------------
   for m in range(n_Lattice):
       contador = 0
       for n in range(len(VTemp)):
           contador += int(VTemp[n])
           range_ion = range_ion_Lattice[m].split()
           ion_i = int(range_ion[0]);  ion_f = int(range_ion[1])
           if (contador >= ion_i and contador <= ion_f):
              ntype_ions[m] += str(VTemp[n]) + ' '

   for m in range(n_Lattice):
       #---------------------------------------
       poscar = open('output/POSCAR.info', 'r')
       poscar_new = open('output/POSCAR.material_' + str(m+1), 'w')
       #-----------------------------------------------------------
       VTemp = poscar.readline()
       poscar_new.write(f'POSCAR \n')
       #-----------------------------
       for n in range(4):
           VTemp = poscar.readline()
           poscar_new.write(f'{VTemp}')
       #-------------------------------
       VTemp = poscar.readline()
       temp = label_materials[m].replace('_', ' ')
       poscar_new.write(f'{temp} \n')
       #-----------------------------
       VTemp = poscar.readline()
       poscar_new.write(f'{ntype_ions[m]} \n')
       #--------------------------------------
       VTemp = poscar.readline()
       poscar_new.write(f'direct \n')
       #---------------------------------------
       range_ion = range_ion_Lattice[m].split()
       ion_i = int(range_ion[0]);  ion_f = int(range_ion[1])
       #----------------------------------------------------
       for n in range(1,(nion+1)):
           VTemp = poscar.readline()
           if (n >= ion_i and n <= ion_f):  poscar_new.write(f'{VTemp}')
       #----------------------------------------------------------------
       poscar.close()
       poscar_new.close()
       #-----------------


# ===============================================
# Construindo o arquivo .json ===================
# ===============================================

#------------------------------------------------------
# Inicializando o arquivo JSON com um dicionário vazio:
#------------------------------------------------------
with open('output/info.json', 'w') as file_json:
    json.dump({}, file_json)

# ===============================================
# Atualizando as informações do arquivo .json ===
# ===============================================

for n in range(2):


    #-------
    crit = 1
    #-----------
    if (n == 0):
       file = l_file
       if (file == 'null'):  crit = 0
    #-----------
    if (n == 1):
       file = l_file_SO
       if (file == 'null'):  crit = 0
    #---------


    if (crit == 1):
       # ===================================================
       # Iniciando tags com valores vazios "--" ============
       # ===================================================
       loop = 0
       id = '--';  id_monolayers = '--'
       label = '--';  label_materials = '--';  formula = '--'
       nlayers = '--';  nions = '--';  nions_monolayers = '--';  range_ions_materials = '--'
       type_ions_materials = '--';  type_nions_materials = '--' 
       lattice_type = '--';  point_group = [];  point_group_schoenflies = [];  space_group = [];  space_group_number = [];  inversion_symmetry = []
       param_a = '--';  a1 = '--';  a2 = '--';  a3 = '--';  param_b = '--';  b1 = '--';  b2 = '--';  b3 = '--'
       module_a1_a2_a3 = '--'; module_b1_b2_b3 = '--';  angle_a1a2_a1a3_a2a3 = '--'; angle_b1b2_b1b3_b2b3 = '--'
       cell_area = '--';  cell_vol = '--';  zb_area = '--';  zb_volume = '--'
       direct_coord_ions = '--';  k_path = '--'


       #----------------------------------------------------------------------------------------------------------
       e_vbm = '--';  e_cbm = '--';  e_fermi = '--';  e_vacuum = '--';  work_function = '--';  total_energy = '--'
       tk_vbm = '--';  tk_cbm = '--'; k_vbm = '--';  k_cbm = '--' 
       nk = '--';  nb = '--';  ne = '--';  ne_valence = '--';  vbm = '--';  cbm = '--';  charge_transfer = [];  
       gap = '--';  type_gap = '--';  k_vbm = [];  k_cbm = [];  lorbit = '--';  ispin = '--'
       #------------------------------------------------------------------------------------------
       non_collinear = '--';  spin_orbit = '--';  lorbit = '--';  ispin = '--'
       #----------------------------------------------------------------------


       # =========================================  ????????????????????????????????????????????????????????????????????????????????????????????????????????????
       # Extraindo o nível de vácuo: =============  ??????????????????????????? Somente faz sentido para sistemas 2D confinados em Z ???????????????????????????
       # =========================================  ????????????????????????????????????????????????????????????????????????????????????????????????????????????
       l_pot = 'null';  l_pot_SO = 'null'
       #-----------------------------------------------------------
       if os.path.isfile('output/Potencial_bands/Potencial_Z.dat'):     l_pot = 'output/Potencial_bands/Potencial_Z.dat'
       if os.path.isfile('output/Potencial_scf/Potencial_Z.dat'):       l_pot = 'output/Potencial_scf/Potencial_Z.dat'
       if os.path.isfile('output/Potencial_bands_SO/Potencial_Z.dat'):  l_pot_SO = 'output/Potencial_bands_SO/Potencial_Z.dat'
       if os.path.isfile('output/Potencial_scf_SO/Potencial_Z.dat'):    l_pot_SO = 'output/Potencial_scf_SO/Potencial_Z.dat'
       #------------------------------------------------------------
       if (l_pot != 'null'):
          file0 = np.loadtxt(l_pot)
          file0.shape
          #-----------------
          date_e = file0[:,1]
          e_vacuum = max(date_e)
       #------------------------
       if (l_pot_SO != 'null'):
          file1 = np.loadtxt(l_pot_SO)
          file1.shape
          #-----------------
          date_e = file1[:,1]
          e_vacuum = max(date_e) 


       # ===========================================
       # Extraindo dados da saída do VASProcar =====
       # ===========================================
       with open('output/' + file, "r") as info: lines = info.readlines()
       #-----------------------------------------------------------------
       for i in range(len(lines)):
           VTemp = lines[i].replace('(', ' ( ').replace(')', ' ) ').replace(';', '').replace(',', '').split()
           if (len(VTemp) > 0):
              #----------------------------------------
              if (VTemp[0] == 'LNONCOLLINEAR'):  non_collinear = str(VTemp[2])
              #----------------------------------------
              elif (VTemp[0] == 'LSORBIT'):  spin_orbit = str(VTemp[2])
              #----------------------------------------
              elif (VTemp[0] == 'nº' or VTemp[0] == 'nÂº'):
                 if (VTemp[1] == 'k-points'):  nk = int(VTemp[3])
                 if (VTemp[5] == 'bands'):  nb = int(VTemp[7])
                 if (VTemp[1] == 'ions'):  ni = int(VTemp[3])
                 if (VTemp[5] == 'electrons'):  ne = float(VTemp[7])
              #----------------------------------------
              elif (VTemp[0] == 'LORBIT'):
                 lorbit = int(VTemp[2])
                 if (VTemp[3] == 'ISPIN'):  ispin = int(VTemp[5])
              #----------------------------------------
              elif (VTemp[0] == 'Last'):  vbm = int(VTemp[4])
              #----------------------------------------
              elif (VTemp[0] == 'First'):  cbm = vbm +1
              #----------------------------------------
              elif (VTemp[0] == 'Valence'):
                   e_vbm = float(VTemp[7])
                   tk_vbm = int(VTemp[11])
              #----------------------------------------
              elif (VTemp[0] == 'Conduction'):
                   e_cbm = float(VTemp[7])
                   tk_cbm = int(VTemp[11])
              #----------------------------------------
              elif (VTemp[0] == 'GAP'):
                type_gap = str(VTemp[2])
                gap = float(VTemp[5])
              #----------------------------------------
              elif (VTemp[0] == 'Fermi'): e_fermi = float(VTemp[3])
              #----------------------------------------
              elif (VTemp[0] == 'free'):
                   total_energy = float(VTemp[4])
                   # e_per_ion = total_energy/ni
              #----------------------------------------
              elif (VTemp[0] == 'Volume_cell'):  Volume_cell = float(VTemp[2])   
              #----------------------------------------
              elif (VTemp[0] == 'Param.'):  param = float(VTemp[2])   
              #----------------------------------------
              elif (VTemp[0] == 'A1'):
                   a1 = [float(VTemp[4])*param, float(VTemp[5])*param, float(VTemp[6])*param]                  
                   A1 = np.array([float(VTemp[4]), float(VTemp[5]), float(VTemp[6])])*param;  module_a1_a2_a3 = []; module_a1_a2_a3.append(np.linalg.norm(A1))
              elif (VTemp[0] == 'A2'):
                   a2 = [float(VTemp[4])*param, float(VTemp[5])*param, float(VTemp[6])*param]
                   A2 = np.array([float(VTemp[4]), float(VTemp[5]), float(VTemp[6])])*param;  module_a1_a2_a3.append(np.linalg.norm(A2))
              elif (VTemp[0] == 'A3'):
                   a3 = [float(VTemp[4])*param, float(VTemp[5])*param, float(VTemp[6])*param]
                   A3 = np.array([float(VTemp[4]), float(VTemp[5]), float(VTemp[6])])*param;  module_a1_a2_a3.append(np.linalg.norm(A3))
                   #-------------------------------------------------------
                   angle_a1a2_a1a3_a2a3 = []
                   angle_a1a2_a1a3_a2a3.append(round(np.degrees(np.arccos(np.dot(A1,A2) / (np.linalg.norm(A1) * np.linalg.norm(A2)))), 3))
                   angle_a1a2_a1a3_a2a3.append(round(np.degrees(np.arccos(np.dot(A1,A3) / (np.linalg.norm(A1) * np.linalg.norm(A3)))), 3))
                   angle_a1a2_a1a3_a2a3.append(round(np.degrees(np.arccos(np.dot(A2,A3) / (np.linalg.norm(A2) * np.linalg.norm(A3)))), 3))
              #----------------------------------------
              elif (VTemp[0] == '2pi/Param.'):  fator_rec = float(VTemp[2])   
              #----------------------------------------
              elif (VTemp[0] == 'B1'):
                   b1 = [float(VTemp[4])*fator_rec, float(VTemp[5])*fator_rec, float(VTemp[6])*fator_rec]
                   B1 = np.array([float(VTemp[4]), float(VTemp[5]), float(VTemp[6])])*fator_rec;  module_b1_b2_b3 = []; module_b1_b2_b3.append(np.linalg.norm(B1))
              elif (VTemp[0] == 'B2'):
                   b2 = [float(VTemp[4])*fator_rec, float(VTemp[5])*fator_rec, float(VTemp[6])*fator_rec]
                   B2 = np.array([float(VTemp[4]), float(VTemp[5]), float(VTemp[6])])*fator_rec;  module_b1_b2_b3.append(np.linalg.norm(B2))
              elif (VTemp[0] == 'B3'):
                   b3 = [float(VTemp[4])*fator_rec, float(VTemp[5])*fator_rec, float(VTemp[6])*fator_rec]
                   B3 = np.array([float(VTemp[4]), float(VTemp[5]), float(VTemp[6])])*fator_rec;  module_b1_b2_b3.append(np.linalg.norm(B3))
                   #-------------------------------------------------------
                   angle_b1b2_b1b3_b2b3 = []
                   angle_b1b2_b1b3_b2b3.append(round(np.degrees(np.arccos(np.dot(B1,B2) / (np.linalg.norm(B1) * np.linalg.norm(B2)))), 3))
                   angle_b1b2_b1b3_b2b3.append(round(np.degrees(np.arccos(np.dot(B1,B3) / (np.linalg.norm(B1) * np.linalg.norm(B3)))), 3))
                   angle_b1b2_b1b3_b2b3.append(round(np.degrees(np.arccos(np.dot(B2,B3) / (np.linalg.norm(B2) * np.linalg.norm(B3)))), 3))
              #----------------------------------------
              elif (VTemp[0] == 'Volume_ZB'):  vol_zb = float(VTemp[2])   
              #----------------------------------------
              elif (VTemp[0] == 'k-points'):  loop = i+3



       if (tk_vbm != '--' and tk_cbm != '--'):
          # ===========================================
          # Buscando os pontos-k do GAP da banda ======
          # ===========================================
          if (file == 'info_bands.txt' or file == 'info_bands_SO.txt'):
             if (n == 0): info = open('output/info_bands.txt', "r")
             if (n == 1): info = open('output/info_bands_SO.txt', "r")
             #-----------
             test = 'nao'
             #-----------
             while (test == 'nao'):             
               #--------------------------------
               VTemp = info.readline().split()
               #-----------------------------------------------------------
               if (len(VTemp) > 0 and VTemp[0] == 'k-points'): test = 'sim'                       
               #-----------------------------------------------------------
             for nn in range(2): VTemp = info.readline()
             for nn in range(1,(nk+1)):
                 VTemp = info.readline().split()
                 if (nn == int(tk_vbm)): k_vbm = [float(VTemp[1]), float(VTemp[2]), float(VTemp[3])]
                 if (nn == int(tk_cbm)): k_cbm = [float(VTemp[1]), float(VTemp[2]), float(VTemp[3])]


       # =================================================================
       # Buscando os valores para a Transferência de Carga de Bader ======
       # =================================================================
       if (n_materials > 1):
          #===========
          if (n == 0):
             if os.path.isfile('output/Charge_transfer/Bader_charge_transfer.dat'):
                file_bader = 'output/Charge_transfer/Bader_charge_transfer.dat'
                #----------------------------
                bader = open(file_bader, "r")
                for nn in range(4): VTemp = bader.readline()
                for mn in range(len(t_ions_materials)):
                    vector_bader = []
                    VTemp = bader.readline()
                    VTemp = bader.readline().split()
                    vector_bader.append(float(VTemp[2]))
                    for mm in range(len(t_ions_materials[mn])):
                        VTemp = bader.readline().split()
                        vector_bader.append(float(VTemp[3]))
                    charge_transfer.append(vector_bader)
          #===========
          if (n == 1):
             if os.path.isfile('output/Charge_transfer_SO/Bader_charge_transfer.dat'):
                file_bader = 'output/Charge_transfer_SO/Bader_charge_transfer.dat'
                #----------------------------
                bader = open(file_bader, "r")
                for nn in range(4): VTemp = bader.readline()
                for mn in range(len(t_ions_materials)):
                    vector_bader = []
                    VTemp = bader.readline()
                    VTemp = bader.readline().split()
                    vector_bader.append(float(VTemp[2]))
                    for mm in range(len(t_ions_materials[mn])):
                        VTemp = bader.readline().split()
                        vector_bader.append(float(VTemp[3]))
                    charge_transfer.append(vector_bader)


       """
       # ===========================================================
       # Obtando e organizando as informações dos pontos-k =========
       # ===========================================================
       if (file == 'info_bands.txt' or file == 'info_bands_SO.txt'):
          #---------------------------------
          info = open('output/' + file, "r")
          #---------------------------------
          if (loop != 0):
             #-----------------------------------------------------
             k_points_direct = []; k_points_cart = [];  k_path = []
             #---------------------------------------------
             for i in range(loop):  VTemp = info.readline()
             for i in range(nk):
                 VTemp = info.readline().split()
                 k_points_direct.append([float(VTemp[1]), float(VTemp[2]), float(VTemp[3])])
                 k_points_cart.append([float(VTemp[4]), float(VTemp[5]), float(VTemp[6])])
                 k_path.append(float(VTemp[7]))
          print(k_path)
          #-----------
          info.close()
       """


       # =========================================================
       # Obtendo as simetrias da rede ============================
       # =========================================================

       #--------------------------------------------------------------------
       # Dicionário de mapeamento de Hermann-Mauguin para Schoenflies ------
       #--------------------------------------------------------------------
       schoenflies = {"1": "C1",  "-1": "Ci",  "2": "C2",  "m": "Cs",  "2/m": "C2h",  "222": "D2",  "mm2": "C2v",  "mmm": "D2h",  "4": "C4",  "-4": "S4",  "4/m": "C4h",
                      "422": "D4",  "4mm": "C4v",  "-42m": "D2d",  "4/mmm": "D4h",  "3": "C3",  "-3": "C3i",  "32": "D3",  "3m": "C3v",  "-3m": "D3d",  "6": "C6",  "-6": "C3h",  
                      "6/m": "C6h",  "622": "D6",  "6mm": "C6v",  "-6m2": "D3h",  "6/mmm": "D6h",  "23": "T",  "m-3": "Th",  "432": "O",  "-43m": "Td",  "m-3m": "Oh"}
       #--------------------------------------------------------------------
       if (n_materials == 1): passo = 1
       if (n_materials >  1): passo = n_materials +1
       #--------------------------------------------
       for i in range(passo):
           #-----------------
           if (i == 0): structure = Poscar.from_file('output/POSCAR.info').structure
           if (i >  0): structure = Poscar.from_file('output/POSCAR.material_' + str(i)).structure
           analyzer = SpacegroupAnalyzer(structure)
           #----------------------------------------------------
           point_group.append(analyzer.get_point_group_symbol())
           space_group.append(analyzer.get_space_group_symbol())
           space_group_number.append(analyzer.get_space_group_number())
           inversion_symmetry.append(analyzer.is_laue())
           if (i == 0): lattice_type = analyzer.get_lattice_type()
           point_group_schoenflies.append(schoenflies.get(point_group[0], "Desconhecido"))
           #------------------------------------------------------------------------------
           # if (i > 0): os.remove('output/POSCAR.material_' + str(i)) # ERROR !!!!!!!!!!!


       #=======================================
       # Obtendo a área no plano XY da rede ===
       #=======================================
       V1 = np.array([A1[0], A1[1]])
       V2 = np.array([A2[0], A2[1]])
       #----------------------------
       # Área da célula no plano XY
       Area_cell = np.linalg.norm(np.cross(V1, V2))
       #-------------------------------------------


       #=======================================
       # Obtendo a área no plano KxKy da ZB ===
       #=======================================
       V1 = np.array([B1[0], B1[1]])
       V2 = np.array([B2[0], B2[1]])
       #----------------------------
       # Área da zb no plano KxKy
       Area_ZB = np.linalg.norm(np.cross(V1, V2))
       #-----------------------------------------


       # ===========================================
       # Criando o Dicionário ======================
       # ===========================================

       dados0 = {
                "id": id_code,
                "number_layers": n_materials,
                "id_layers": id_materials,
                "formula": estequiometria,
                "type_ions_layers": t_ions_materials,
                "number_ions_layers": nions_materials,
                "number_type_ions_layers": t_nions_materials,
                "range_ions_layers": r_ions_materials,
                "number_ions": ni,
                # ---------------------------------------------------------------------
                "area_perc_mismatch": area_perc_mismatch  if n_materials > 1 else None,
                "perc_area_change": perc_area_change  if n_materials > 1 else None,
                "perc_mod_vectors_change": perc_mod_vectors_change  if n_materials > 1 else None,
                "angle_perc_mismatch": angle_perc_mismatch  if n_materials > 1 else None,
                "perc_angle_change": perc_angle_change  if n_materials > 1 else None,
                "rotation_angle": rotation_angle  if n_materials > 1 else None,
                "supercell_matrix": supercell_matrix  if n_materials > 1 else None,
                "deformation_matrix": deformation_matrix  if n_materials > 1 else None,
                "strain_matrix": strain_matrix  if n_materials > 1 else None,
                # "structural_optimization": 'DFT',      # 'none', 'DFT', 'ML', 'ML/DFT'
                "shift_plane": shift_plane if n_materials > 1 else None,
                "z_separation": z_separation  if n_materials > 1 else None,
                "thickness": thickness,
                "total_thickness": total_thickness,
                # ---------------------------------------------------------------------
                "lattice_type": lattice_type,
                "point_group": point_group,
                # "point_group_schoenflies": point_group_schoenflies,
                "space_group": space_group,
                "space_group_number": space_group_number,
                "inversion_symmetry": inversion_symmetry,
                "pseudo_type": pseudo_type,
                "exchange_correlation_functional": exchange_correlation_functional,
                "vdW": vdW,
                "non_collinear": non_collinear,
                "spin_orbit": spin_orbit,
                # "param_a": param,
                "a1": a1,
                "a2": a2,
                "a3": a3,
                "module_a1_a2_a3": module_a1_a2_a3,
                "angle_a1a2_a1a3_a2a3": angle_a1a2_a1a3_a2a3,
                "cell_area": Area_cell,
                # "cell_vol": Volume_cell,
                # "param_b": fator_rec,
                "b1": b1,
                "b2": b2,
                "b3": b3,
                "module_b1_b2_b3": module_b1_b2_b3,
                "angle_b1b2_b1b3_b2b3": angle_b1b2_b1b3_b2b3,
                "zb_area": Area_ZB,
                # "zb_volume": vol_zb,
                "direct_coord_ions": coord_ions,
                "kpath": kpath,
                }


       if (n == 0):
          #---------
          dados1 = {
                   "lorbit": lorbit,
                   "ispin": ispin,
                   "nk": nk,
                   "nb": nb,
                   "ne": ne,
                   "gap": gap,
                   "e_vbm": e_vbm,
                   "e_cbm": e_cbm,
                   "vbm": vbm,
                   "cbm": cbm,
                   "type_gap": type_gap,
                   "k_vbm": k_vbm,
                   "k_cbm": k_cbm,
                   "e_fermi": e_fermi,
                   "e_vacuum": e_vacuum,
                   # "work_function": work_function,
                   "total_energy": total_energy,
                   "e_per_ion":  total_energy/ni,
                   "e_per_area": total_energy/Area_cell,
                   "e_binding": e_binding  if n_materials > 1 else None,
                   "e_slide": e_slide  if n_materials > 1 else None,
                   "charge_transfer": charge_transfer  if n_materials > 1 else None,
                   }


       if (n == 1):
          #---------
          dados1 = {
                   "lorbit_SO": lorbit,
                   "ispin_SO": ispin,
                   "nk_SO": nk,
                   "nb_SO": nb,
                   "ne_SO": ne,
                   "gap_SO": gap,
                   "e_vbm_SO": e_vbm,
                   "e_cbm_SO": e_cbm,
                   "vbm_SO": vbm,
                   "cbm_SO": cbm,
                   "type_gap_SO": type_gap,
                   "k_vbm_SO": k_vbm,
                   "k_cbm_SO": k_cbm,
                   "e_fermi_SO": e_fermi,
                   "e_vacuum_SO": e_vacuum,
                   # "work_function_SO": work_function,
                   "total_energy_SO": total_energy,
                   "e_per_ion_SO":  total_energy/ni,
                   "e_per_area_SO": total_energy/Area_cell,
                   "charge_transfer": charge_transfer  if n_materials > 1 else None,
                   }


       # ==================================================
       # Inserindo as informações no arquivo .json ========
       # ==================================================
       with open('output/info.json', 'r') as file:  data = json.load(file)            # Carregando o conteúdo atual do arquivo info.json
       data.update(dados0)                                                            # Atualizando o dicionário com as novas informações
       with open('output/info.json', 'w') as file: json.dump(data, file, indent=4)    # Salvar o conteúdo atualizado no arquivo info.json
       #----------------------
       with open('output/info.json', 'r') as file:  data = json.load(file)            # Carregando o conteúdo atual do arquivo info.json
       data.update(dados1)                                                            # Atualizando o dicionário com as novas informações
       with open('output/info.json', 'w') as file: json.dump(data, file, indent=4)    # Salvar o conteúdo atualizado no arquivo info.json


#===============================================================
# Atualizando os arquivos POSCAR e CONTCAR =====================
#===============================================================
with open('output/POSCAR', 'r') as file: line = file.readlines()
tline = line[0].split()
#--------------------
replace_line = tline[0] + ' ' + tline[1] + ' '
for i in range(n_materials): replace_line += tline[2 +i] + ' '
replace_line += tline[-1] + '\n'
#------------------------------
line[0] = replace_line
with open('output/POSCAR', 'w') as file: file.writelines(line)
#================================================================
with open('output/CONTCAR', 'r') as file: line = file.readlines()
line[0] = replace_line
with open('output/CONTCAR', 'w') as file: file.writelines(line)
#==============================================================


"""
# ===============================================
# Abrindo e lendo o data-base .json =============
# ===============================================
with open('output/info.json', "r") as file_json: date = json.load(file_json)
#------------------------------------------------
print(" ")
print("===========================")
print("Dados do arquivo info.json:")
print("===========================")
print(" ")
for chave, valor in date.items(): print(f"{chave}: {valor}")
"""

