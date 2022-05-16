#coded and debugged by Wonjin Ko
#time: 1 hours
from __future__ import absolute_import, division, print_function 
#import Psychopy library
from psychopy import visual, core, event

#create a visual window
win = visual.Window(color = [0, 1, 0])

#create text (not display yet)
title = visual.TextStim(win, text=u"VID: Viral Illness Detector",height = 0.1, wrapWidth = 1)
directions = visual.TextStim(win, text=u"Directions: Please fill out this questionnaire to the best of your ability. Based on your symptoms, our Viral Illness Detector will attempt to diagnose the most likely viral illness you possess.\n\nPress any key to continue",height = 0.1,wrapWidth = 1)
preface = visual.TextStim(win, text=u"Preface: The results of the Viral Illness Detector are not 100% accurate. It simply diagnoses you with the viral disease it believes you most likely possess. Also note that this medical illness detector is simply for viral diseases. This means that bacterial diseases such as tuberculosis, bacterial pneumonia, STDs, etc. are not considered. Please take that into consideration.\n\nPress any key to continue", height = 0.08, wrapWidth = 1)
diseases1 = visual.TextStim(win, text=u"The diseases this Viral Illness Detector is able to identify are the following:",pos=(0, +0.7), height = 0.08, wrapWidth = 1)
diseases2 = visual.TextStim(win, text=u"-Influenza (Flu)\n-Hepatitis A, B, and C\n-Malaria\n-Chicken Pox\n-Dengue\n-Fever\n-Rhinovirus (Common Cold)\n-Viral Pneumonia\n-Shingles\n-COVID-19",pos=(0.7, -0.1),height = 0.08, alignText='left', wrapWidth = 2)
anykey = visual.TextStim(win, text=u"Press any key to continue",pos=(0, -0.8), height = 0.1, wrapWidth = 1)
last_title = visual.TextStim(win, text=u"If you do not believe you have any of the viral diseases above, it is not recommended you fill out this questionnaire\n\nPress any key to continue ",height = 0.1, wrapWidth = 2)

#draw the text to the hidden visual buffer
title.draw()

#show the hidden buffer and wait for input
win.flip()
event.waitKeys()

#open directions
directions.draw()
win.flip()
event.waitKeys()

#open preface
preface.draw()
win.flip()
event.waitKeys()

#open diseases
diseases1.draw()
diseases2.draw()
anykey.draw()
win.flip()
event.waitKeys()

#last warning
last_title.draw()
win.flip()
event.waitKeys()

###SECTION 1####
#texts used
Section1 = visual.TextStim(win, text=u"Section I: General Symptoms")
General1 = visual.TextStim(win, text=u"General Symptoms: Please indicate whether you are experiencing any of the following symptoms")

#titlepage
Section1.draw()
win.flip()
event.waitKeys()

#temperature question
instruction = visual.TextStim(win,color="white")
quitKeys = ['escape', 'esc']
ansKeys = ['return']
keyboardKeys = ['1','2','3','4','5','6','7','8','9','0','period']
answer = ''
complete_answer = False
while not complete_answer:
    instruction.setText(u'Please type in your current body temperature (deg F):\n{0}'.format(answer))
    instruction.draw()
    win.flip()
    for letter in (keyboardKeys):
        if event.getKeys([letter]):
            if letter == 'period':
                answer += '.'
            else :
                answer += letter
    if event.getKeys(['backspace']):
        answer = answer[:-1]
    if event.getKeys([quitKeys[0]]):
        core.quit()
    if event.getKeys([ansKeys[0]]):
        complete_answer = True
        General1.draw()
#recieves user input and stores into variable called body_temperature
body_temperature = answer
print(body_temperature)
#presents general 1
win.flip()
event.waitKeys()

#List containing Part I symptoms
q_list = ['Coughing (y/n)', 'Sneezing (y/n)', 'Runny or Congested Nose (y/n)', 'Shortness of Breath (y/n)', 'Excess Mucus (Phlegm) (y/n)', 'Sore Throat (y/n)', 'Headache (y/n)', 'Abdominal Pain (y/n)', 'Sensations of Fatigue or Lethargy (y/n)', 'Muscle or Body Aching (y/n)', 'Chest Pain (y/n)', 'Joint Pain (y/n)', 'Chills (y/n)', 'General Feeling of Being Unwell (y/n)', 'Nausea (y/n)','Vomiting (y/n)', 'Diarrhea (y/n)', 'Loss of Appetite (y/n)', 'Dehydration (y/n)', 'Sweating (y/n)']
symptom_list = []
instruction = visual.TextStim(win, color="white")
quitKeys = ['escape', 'esc']
ansKeys = ['return']
keyboardKeys = ['y','n']

#for loop that goes through every symptom in q_list and restricts user to 2 answer choices
#stores user inputs in a list called symptom_list
for i in range(len(q_list)):
    answer = ''
    complete_answer = False
    while not complete_answer:
        instruction.setText(q_list[i]+'\n{0}'.format(answer))
        instruction.draw()
        win.flip()
        for letter in (keyboardKeys):
            if event.getKeys([letter]):
                answer = letter
                complete_answer = True
        if event.getKeys(['backspace']):
            answer = answer[:-1]
        if event.getKeys([quitKeys[0]]):
            core.quit()
    symptom_list.append(answer)

##### SECTION 2 ######

#texts used
Section2 = visual.TextStim(win, text=u"Section II: Rashes and Skin")
General1 = visual.TextStim(win, text=u"1.Please indicate whether you are experiencing any of the following symptoms")

#titlepage
Section2.draw()
win.flip()
event.waitKeys()

#Directions
General1.draw()
win.flip()
event.waitKeys()

#see above for explanation
q_list = ['General Red Rash (y/n)','Shingles Rash (y/n)','Papules (Tiny Red Spots) (y/n)','Fluid-Filled Blisters (y/n)','2. Are you experiencing any form of itchiness on your body? (y/n)']
instruction = visual.TextStim(win, color="white")
quitKeys = ['escape', 'esc']
ansKeys = ['return']
keyboardKeys = ['y','n']
for i in range(len(q_list)):
    answer = ''
    complete_answer = False
    while not complete_answer:
        instruction.setText(q_list[i]+'\n{0}'.format(answer))
        instruction.draw()
        win.flip()
        for letter in (keyboardKeys):
            if event.getKeys([letter]):
                answer = letter
                complete_answer = True
        if event.getKeys(['backspace']):
            answer = answer[:-1]
        if event.getKeys([quitKeys[0]]):
            core.quit()
    symptom_list.append(answer)

##### SECTION III #####
#texts used
Section3 = visual.TextStim(win, text=u"Section III: Specific Symptoms")
General1 = visual.TextStim(win, text=u"Please indicate in the following slides if you are experiencing any form of jaundice (yellowing):")
General2 = visual.TextStim(win, text=u"Please indicate if you have detected any of the following:")
General3 = visual.TextStim(win, text=u"Are you currently undergoing, experiencing, or receiving any of the following?")
End = visual.TextStim(win, text=u"END OF QUESTIONAIRE")

#titlepage
Section3.draw()
win.flip()
event.waitKeys()

#directions
General1.draw()
win.flip()
event.waitKeys()

#see above 
q_list = ['yellowish skin (y/n)', 'yellowish eyes (y/n)', '3. Are you experiencing any redness of the eyes? (y/n)','Is your urine darker than usual (non-yellow, orange-brownish)? (y/n)']
instruction = visual.TextStim(win, color="white")
quitKeys = ['escape', 'esc']
ansKeys = ['return']
keyboardKeys = ['y','n']
for i in range(len(q_list)):
    answer = ''
    complete_answer = False
    while not complete_answer:
        instruction.setText(q_list[i]+'\n{0}'.format(answer))
        instruction.draw()
        win.flip()
        for letter in (keyboardKeys):
            if event.getKeys([letter]):
                answer = letter
                complete_answer = True
        if event.getKeys(['backspace']):
            answer = answer[:-1]
        if event.getKeys([quitKeys[0]]):
            core.quit()
    symptom_list.append(answer)

#Directions 2
General2.draw()
win.flip()
event.waitKeys()

q_list = ['Mouth Ulcers (y/n)', 'Swollen Lymph Nodes (y/n)']
instruction = visual.TextStim(win, color="white")
quitKeys = ['escape', 'esc']
ansKeys = ['return']
keyboardKeys = ['y','n']
for i in range(len(q_list)):
    answer = ''
    complete_answer = False
    while not complete_answer:
        instruction.setText(q_list[i]+'\n{0}'.format(answer))
        instruction.draw()
        win.flip()
        for letter in (keyboardKeys):
            if event.getKeys([letter]):
                answer = letter
                complete_answer = True
        if event.getKeys(['backspace']):
            answer = answer[:-1]
        if event.getKeys([quitKeys[0]]):
            core.quit()
    symptom_list.append(answer)

#Directions 3 
General3.draw()
win.flip()
event.waitKeys()

q_list = ['Blood Transfusion (y/n)','Unsterile Injections (y/n)']
instruction = visual.TextStim(win, color="white")
quitKeys = ['escape', 'esc']
ansKeys = ['return']
keyboardKeys = ['y','n']
for i in range(len(q_list)):
    answer = ''
    complete_answer = False
    while not complete_answer:
        instruction.setText(q_list[i]+'\n{0}'.format(answer))
        instruction.draw()
        win.flip()
        for letter in (keyboardKeys):
            if event.getKeys([letter]):
                answer = letter
                complete_answer = True
        if event.getKeys(['backspace']):
            answer = answer[:-1]
        if event.getKeys([quitKeys[0]]):
            core.quit()
    symptom_list.append(answer)

#code that transforms all 'y' values to 1 and 'n' values to 0, which will be processed later
for i in range(len(symptom_list)):
    if symptom_list[i] == 'y':
        symptom_list[i] = 1
    elif symptom_list[i] == 'n':
        symptom_list[i] = 0

print(symptom_list)

End.draw()
win.flip()
core.wait(3)
win.close()
core.quit()
