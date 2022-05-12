#Debugged and coded by: Wonjin Ko
#hours: 3 hours
from __future__ import absolute_import, division, print_function 
#import Psychopy library
from psychopy import visual, core, event

#create a visual window
win = visual.Window()

#create text (not display yet)
title = visual.TextStim(win, text=u"VID: Viral Illness Detector",height = 0.1, wrapWidth = 1)
directions = visual.TextStim(win, text=u"Directions: Please fill out this questionnaire to the best of your ability. Based on your symptoms, our Viral Illness Detector will attempt to diagnose the most likely viral illness you possess.\n\nPress any key to continue",height = 0.1,wrapWidth = 2)
preface = visual.TextStim(win, text=u"Preface:The results of the Viral Illness Detector are not 100% accurate. It simply diagnoses you with the viral disease it believes you most likely possess. Also note that this medical illness detector is simply for viral diseases. This means that bacterial diseases such as tuberculosis, bacterial pneumonia, STDs, etc. are not considered. Please take that into consideration.\n\nPress any key to continue", height = 0.1, wrapWidth = 2)
diseases1 = visual.TextStim(win, text=u"The diseases this Viral Illness Detector is able to identify are the following:",pos=(0, +0.7), height = 0.1, wrapWidth = 2)
diseases2 = visual.TextStim(win, text=u"-Influenza (Flu)\n-Hepatitis A, B, and C\n-Malaria\n-Chicken Pox\n-Dengue\n-Fever\n-Rhinovirus (Common Cold)\n-Viral Pneumonia\n-Shingles\n-COVID-19",pos=(0.7, -0.1),height = 0.1, alignText='left', wrapWidth = 2)
anykey = visual.TextStim(win, text=u"Press any key to continue",pos=(0, -0.8), height = 0.1, wrapWidth = 1)
last_title = visual.TextStim(win, text=u"If you do not believe you have any of the viral diseases above, it is not recommended you fill out this questionnaire\n\nPress any key to continue ",height = 0.1, wrapWidth = 2)
#draw the text to the hidden visual buffer
title.draw()

#show the hidden buffer
win.flip()
event.waitKeys()
#Wait 3 sec
#core.wait(3)

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

#quit program
win.close()
core.quit()

