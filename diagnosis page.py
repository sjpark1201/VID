from __future__ import absolute_import, division, print_function 
#import Psychopy library
from psychopy import visual, core, event

viral_disease = 'HIV'
win = visual.Window()
diagnosis_title = visual.TextStim(win, text=u"Diagnosis",pos=(0, +0.3))
diagnosis = visual.TextStim(win, text=u"You have:\n" + viral_disease,pos=(0, 0))
warning = visual.TextStim(win, text=u"Note: diagnosis may not be 100% accurate",pos=(0, -0.4))


diagnosis.draw()
warning.draw()
diagnosis_title.draw()
win.flip()
event.waitKeys()