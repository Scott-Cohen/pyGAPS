# %%
import os
import adsutils

json_path = os.path.join(os.getcwd(), 'tests', 'data', 'isotherms_json')
json_file_paths = adsutils.util_get_file_paths(json_path, '.json')
isotherms = []
for filepath in json_file_paths:
    with open(filepath, 'r') as text_file:
        isotherms.append(adsutils.isotherm_from_json(text_file.read()))

#################################################################################
#################################################################################
# Henrys constant calculations
#
# %%
# Regular method

for isotherm in isotherms:
    adsutils.calc_initial_henry(isotherm, max_adjrms=0.01, verbose=True)

# %%
# Virial method
for isotherm in isotherms:
    adsutils.calc_initial_henry_virial(isotherm, verbose=True)