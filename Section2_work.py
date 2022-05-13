#coded and debugged by Wonjin Ko
#time: 10 hours
from __future__ import absolute_import, division, print_function 
from psychopy import visual,core,event
win = visual.Window()

#texts used
Section2 = visual.TextStim(win, text=u"Section II: Rashes and Skin")
General1 = visual.TextStim(win, text=u"1.Please indicate whether you are experiencing any of the following symptoms")
#titlepage
Section2.draw()
win.flip()
event.waitKeys()

General1.draw()
win.flip()
event.waitKeys()

q_list = ['General Red Rash (y/n)','Shingles Rash (y/n)','Papules (Tiny Red Spots) (y/n)','Fluid-Filled Blisters (y/n)','2. Are you experiencing any form of itchiness on your body? (y/n)']
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