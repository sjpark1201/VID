# Code written and debugged by Sean Park
# Time: 30 Hours (Putting it All Together)

# The code below takes the CSV we created and imports it using Pandas

# when running this code: cd Documents/CLPS_0950_Final_Project

# the code below will be used for the final diagnosis page portion

from __future__ import absolute_import, division, print_function

#import Psychopy library

from psychopy import visual, core, event

# -----------------------------------------------------------------------------------------------------
import pandas as pd

# Refer to GITHUB repository to access CSV file. CSV file written by all of us
# Time: 2 Hours Each

url = 'https://raw.githubusercontent.com/sjpark1201/VID/main/viral_illness_dataset_official.csv'
viral_illness_dataset_prior = pd.read_csv(url)
viral_illness_dataset= viral_illness_dataset_prior.set_index('Symptoms') # changes the index of the dataframe from numbers to symptoms

# -----------------------------------------------------------------------------------------------------
# Code for User Input - Symptoms Test (Rhiovirus)

import pandas as pd
import random as r

# Determines whether patient has no fever, mild fever, or high fever based on the body temperature they input

symptoms = []

from VID import body_temperature # references VID.py which consists of psychopy user interface code

if body_temperature < 99.5:
  symptoms = [0,0]

if body_temperature >= 99.5 and body_temperature <= 102.4:
  symptoms = [1,0]

if body_temperature > 102.4:
  symptoms = [0,1]

# ERASE LATER - Creates a random set of 1s and 0s as "test symptoms" for now

from VID import symptom_list

symptoms.extend(symptom_list)

my_symptoms = pd.Series(data = symptoms, index = ['mild_fever', 'high_fever', 'cough', 'sneezing', 'runny_or_stuffed_nose', 'shortness_of_breath', 'mucus', 'sore_throat','headache ','abdominal_pain','fatigue','muscle_or_body_aches','chest_pain','joint_pain','chills','malaise_(feeling_unwell)','nausea','vomiting','diarrhea','loss_of_appetite','dehydration','sweating','red_rash','shingles_rash','papules_(red_spots)','fluid_filled_blisters','itching','yellowish_skin','yellowish_eyes','red_eyes','dark_urine','mouth_ulcers','swollen_lymph_nodes','receiving_blood_transfusion','receiving_unsterile_injections']) # Patient's symptoms are converted to a Pandas series
# -----------------------------------------------------------------------------------------------------

import numpy as np

symptom_presence_evaluation_prior = viral_illness_dataset.eq(my_symptoms, axis = 0) # compares the patient's symptoms to our viral_illness_dataset

new_index = ['mild_fever', 'high_fever', 'cough', 'sneezing', 'runny_or_stuffed_nose', 'shortness_of_breath', 'mucus', 'sore_throat','headache ','abdominal_pain','fatigue','muscle_or_body_aches','chest_pain','joint_pain','chills','malaise_(feeling_unwell)','nausea','vomiting','diarrhea','loss_of_appetite','dehydration','sweating','red_rash','shingles_rash','papules_(red_spots)','fluid_filled_blisters','itching','yellowish_skin','yellowish_eyes','red_eyes','dark_urine','mouth_ulcers','swollen_lymph_nodes','receiving_blood_transfusion','receiving_unsterile_injections']

symptom_presence_evaluation = symptom_presence_evaluation_prior.reindex(new_index)

spe_np = symptom_presence_evaluation.to_numpy() # converts the Pandas dataframe into a numpy array

symptom_matching = np.count_nonzero(spe_np, axis = 0) # counts the number of times "True" appears across a column (per disease)

# CODE EXPLATION: Outputs the most likely viral disease the patient possesses based on which disease possesed the most similar symptoms that they descriubed

most_alike_symptoms = np.where(symptom_matching == np.amax(symptom_matching)) # find the location with the maximum value of "True" and return that index in a tuple

disease_value = most_alike_symptoms[0] # converts value in tuple to array

# Certain Exceptions Occur when a disease has a specific symptom that no other disease possesses (CODE LATER: Shingles, viral pneumonia)

# Based on disease_value, we will convert this value to a specific disease

if disease_value[0] == 0:
  viral_disease = 'influenza (flu)'

if disease_value[0] == 1:
  viral_disease = 'hepatitis a'

if disease_value[0] == 2:
  viral_disease = 'hepatitis b or c'

if disease_value[0] == 3:
  viral_disease = 'malaria'

if disease_value[0] == 4:
  viral_disease = 'chicken pox'

if disease_value[0] == 5:
  viral_disease = 'dengue fever'

if disease_value[0] == 6:
  viral_disease = 'rhinovirus (common cold)'

if disease_value[0] == 7:
  viral_disease = 'viral pneumonia'

if disease_value[0] == 8:
  viral_disease = 'shingles'

if disease_value[0] == 9:
  viral_disease = 'covid-19'

# -----------------------------------------------------------------------------------------------------

# CODE EXPLANATION - CHECKER: Many diseases have similar symptoms to one another and certain exceptions occur when a disease has a specific symptom that no other disease possesses. Therefore, the code below checks
# whether the diagnosed disease possesses a specific symptom and compares them to other similar illnesses. This ensures it assigns the most likely viral disease.

# Time: 5 Hours (Checking and Editing Each One)

if viral_disease == 'influenza (flu)':
  if spe_np[16,0] == False and spe_np[17,0] == False and spe_np[5,0] == True: #checks whether there is no presence of nausea, vomiting but presence of chest pain (distinguishing cold and flu)
    viral_disease = 'rhinovirus (common cold)'
  elif spe_np[1,0] == False and spe_np[12,0] == False and spe_np[16,0] == True and spe_np[17,0] == True: # checks whether the patient has a high fever, nausea, vomiting, and chest pain (viral pneumonia)
    viral_disease = 'viral pneumonia'
  elif spe_np[24,0] == False or spe_np[25,0] == False: # checks whether the patient is experiencing papules or fluid-filled blisters (must have symptoms for chicken pox)
    viral_disease = 'chicken pox'
  elif spe_np[23,0] == False: # checks for presence of shingles rash
    viral_disease = 'shingles'
  else:
    viral_disease = 'influenza (flu)'

if viral_disease == 'heptatis a':
  if spe_np[33,1] == False or spe_np[34,1] == False: #checks whether the patient is currently recieving a blood transfusion or unsterile injections (must have symptom for hep b and c)
    viral_disease = 'heptatis b or c'
  elif spe_np[24,1] == False or spe_np[25,1] == False: # checks whether the patient is experiencing papules or fluid-filled blisters (must have symptoms for chicken pox)
    viral_disease = 'chicken pox'
  elif spe_np[23,1] == False: # checks for presence of shingles rash
    viral_disease = 'shingles'
  else:
    viral_disease = 'hepatitis a'

if viral_disease == 'heptatis b or c':
  if spe_np[33,2] == False and spe_np[34,2] == False: #checks whether the patient is not currently recieviing a blood transfusion and unsterile injections (must have symptom for hep a)
    viral_disease = 'heptatis a'
  elif spe_np[24,2] == False or spe_np[25,2] == False: # checks whether the patient is experiencing papules or fluid-filled blisters (must have symptoms for chicken pox)
    viral_disease = 'chicken pox'
  elif spe_np[23,2] == False: # checks for presence of shingles rash
    viral_disease = 'shingles'
  else:
    viral_disease = 'hepatitis b or c'

if viral_disease == 'malaria':
  if spe_np[22,3] == False: # checks whether thre is the presence of a red rash (common symptom in dengue not malaria)
    viral_disease = 'dengue fever'
  elif spe_np[24,3] == False or spe_np[25,3] == False: # checks whether the patient is experiencing papules or fluid-filled blisters (must have symptoms for chicken pox)
    viral_disease = 'chicken pox'
  elif spe_np[23,3] == False: # checks for presence of shingles rash
    viral_disease = 'shingles'
  else:
    viral_disease = 'malaria'

if viral_disease == 'chicken pox':
  if spe_np[24,4] == False or spe_np[25,4] == False: # checks whether the patient is experiencing papules or fluid-filled blisters (must have symptoms for chicken pox)
    viral_disease = 'unidentifiable or early chicken pox'
  elif spe_np[23,4] == False: # checks for presence of shingles rash
    viral_disease = 'shingles'
  else:
    viral_disease = 'chicken pox'

if viral_disease == 'dengue fever':
  if spe_np[22,5] == False: # checks whether the patient does not have red rash (common symptom in dengue not malaria)
    viral_disease = 'malaria'
  elif spe_np[24,5] == False or spe_np[25,5] == False: # checks whether the patient is experiencing papules or fluid-filled blisters (must have symptoms for chicken pox)
    viral_disease = 'chicken pox'
  elif spe_np[23,5] == False: # checks for presence of shingles rash
    viral_disease = 'shingles'
  else:
    viral_disease = 'dengue fever'

if viral_disease == 'rhinovirus (common cold)':
  if spe_np[0,6] == True and spe_np[12,6] == False and spe_np[16,6] == False and spe_np[17,6] == False: # checks whether the patient has a mild fever, nausea, and vomiting but not chest pain (influenza)
    viral_disease = 'influenza (flu)'
  elif spe_np[0,6] == False and spe_np[12,6] == True and spe_np[16,6] == False and spe_np[17,6] == False: # checks whether the patient has a high fever, nausea, vomiting, and chest pain (viral pneumonia)
    viral_disease = 'viral pneumonia'
  elif spe_np[24,6] == False or spe_np[25,6] == False: # checks whether the patient is experiencing papules or fluid-filled blisters (must have symptoms for chicken pox)
    viral_disease = 'chicken pox'
  elif spe_np[23,6] == False: # checks for presence of shingles rash
    viral_disease = 'shingles'
  else:
    viral_disease = 'rhinovirus (common cold)'

if viral_disease == 'viral pneumonia':
  if spe_np[0,7] == False and spe_np[12,7] == False and spe_np[16,7] == True and spe_np[17,7] == True: # checks whether the patient has a mild fever, nausea, and vomiting but not chest pain (influenza)
    viral_disease = 'influenza (flu)'
  elif spe_np[0,7] == False and spe_np[12,7] == True and spe_np[16,7] == False and spe_np[17,7] == False: # checks whether the patient has a mild fever and chest pain but no nausea and vomiting (common cold)
    viral_disease = 'rhinovirus (common cold)'
  elif spe_np[24,7] == False or spe_np[25,7] == False: # checks whether the patient is experiencing papules or fluid-filled blisters (must have symptoms for chicken pox)
    viral_disease = 'chicken pox'
  elif spe_np[23,7] == False: # checks for presence of shingles rash
    viral_disease = 'shingles'
  else:
    viral_disease = 'viral_pneumonia'

if viral_disease == 'shingles':
  if spe_np[23,8] == False: # checks whether the patient has the presence of a shingles rash (must have symptom for shingles)
    viral_disease = 'unidentifiable or early shingles'
  elif spe_np[24,8] == False or spe_np[25,8] == False: # checks whether the patient is experiencing papules or fluid-filled blisters (must have symptoms for chicken pox)
    viral_disease = 'chicken pox'
  else:
    viral_disease = 'shingles'

if viral_disease == 'covid-19':
  if spe_np[1,9] == False and spe_np[5,9] == True: # checks whether the patient has a high fever and shortness of breath (viral pneumonia)
    viral_disease = 'viral pneumonia'
  elif spe_np[0,9] == True and spe_np[5,9] == False: # checks whether the patient has a mild fever and no shortness of breath (common cold)
    viral_disease = 'rhinovirus (common cold)'
  elif spe_np[0,9] == True and spe_np[5,9] == False and spe_np[16,9] == False and spe_np[17,9] == False: # checks whether the patient has a mild fever and no shortness of breath in addition to symptoms of nausea and vomiting (influenza):
    viral_disease = 'influenza (flu)'
  elif spe_np[24,9] == False or spe_np[25,9] == False: # checks whether the patient is experiencing papules or fluid-filled blisters (must have symptoms for chicken pox)
    viral_disease = 'chicken pox'
  elif spe_np[23,9] == False: # checks for presence of shingles rash
    viral_disease = 'shingles'
  else:
    viral_disease = 'covid-19'
# -----------------------------------------------------------------------------------------------------
# CODE EXPLANATION: Uses pychopy to display the diagnosis page
# Coded and Debugged by Wonjin Ko
# Time: 1 Hour


win = visual.Window(color = [0.2, 0.6, 0.1])
diagnosis_title = visual.TextStim(win, text=u"Diagnosis",pos=(0, +0.3))
diagnosis = visual.TextStim(win, text=u"You have:\n" + viral_disease,pos=(0, 0))
warning = visual.TextStim(win, text=u"Note: diagnosis may not be 100% accurate",pos=(0, -0.4))

diagnosis.draw()
warning.draw()
diagnosis_title.draw()
win.flip()
event.waitKeys()

End.draw()
win.flip()
core.wait(10)
win.close()
core.quit()
