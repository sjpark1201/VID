#coded and debugged by Wonjin Ko
#time: 10 hours
from __future__ import absolute_import, division, print_function 
from psychopy import visual,core,event
win = visual.Window()

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

General1.draw()
win.flip()
event.waitKeys()

q_list = ['yellowish skin (y/n)', 'yellowish eyes (y/n)', '3. Are you experiencing any redness of the eyes? (y/n)','Is your urine darker than usual (non-yellow, orange-brownish)? (y/n)']
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
        if event.getKeys(['backspace']):
            answer = answer[:-1]
        if event.getKeys([quitKeys[0]]):
            core.quit()
        if event.getKeys([ansKeys[0]]):
            complete_answer = True
    symptom_list.append(answer)

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

End.draw()
win.flip()
core.wait(3)
win.close()
core.quit()
