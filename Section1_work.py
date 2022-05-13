#coded and debugged by Wonjin Ko
#time: 10 hours
from __future__ import absolute_import, division, print_function 
from psychopy import visual,core,event
win = visual.Window()

#texts used
Section1 = visual.TextStim(win, text=u"Section I: General Symptoms")
General1 = visual.TextStim(win, text=u"General Symptoms: Please indicate whether you are experiencing any of the following symptoms")

#titlepage
Section1.draw()
win.flip()
event.waitKeys()

#question
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
body_temperature = answer
print(body_temperature)
win.flip()
event.waitKeys()

q_list = ['Coughing (y/n)', 'Sneezing (y/n)', 'Runny or Congested Nose (y/n)', 'Shortness of Breath (y/n)', 'Excess Mucus (Phlegm) (y/n)', 'Sore Throat (y/n)', 'Headache (y/n)', 'Abdominal Pain (y/n)', 'Sensations of Fatigue or Lethargy (y/n)', 'Muscle or Body Aching (y/n', 'Chest Pain (y/n)', 'Joint Pain (y/n)', 'Chills (y/n)', 'General Feeling of Being Unwell (y/n)', 'Nausea (y/n)','Vomiting (y/n)', 'Diarrhea (y/n)', 'Loss of Appetite (y/n)', 'Dehydration (y/n)', 'Sweating (y/n)']
symptom_list = []
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
        if event.getKeys(['backspace']):
            answer = answer[:-1]
        if event.getKeys([quitKeys[0]]):
            core.quit()
        if event.getKeys([ansKeys[0]]):
            complete_answer = True
    symptom_list.append(answer)

for i in range(len(symptom_list)):
    if symptom_list[i] == 'y':
        symptom_list[i] = 1
    elif symptom_list[i] == 'n':
        symptom_list[i] = 0
print(symptom_list)