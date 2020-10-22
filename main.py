from tkinter import *
import tkinter as tk


class WebSpider:
    def __init__(self, master):
        self.window = master
        self.mainFrame = Frame(master=master, width=500, height=500)
        self.mainFrame.pack()
        self.objects = {
            'main': self.mainFrame
        }

    def handleEvent(self, event):
        print('Some event has happend: '.format(event))

    def start(self):
        self.window.mainloop()

    def countStart(self, obj: dict, s: str) -> int:
        """
        Function countStart - returns counter of starts elements of list 'obj' with string 's'
        :obj: dictionary
        :s: string
        :rtype: int
        """
        counter = 0
        for ob in obj.keys():
            if ob.startswith(s):
                counter += 1
        return counter

    def add(self, tp: str, params: dict, x=False, y=False, func=False):
        if not func:
            func = self.handleEvent
        name = tp + '-' + str(self.countStart(self.objects, tp) + 1)
        self.objects[name] = eval('{}(master=self.objects[\'main\'])'.format(tp))
        if tp == 'Button':
            self.objects[name]['command'] = func
        for param in params.keys():
            self.objects[name][param] = params[param]
        if not x and not y:
            self.objects[name].pack()
        else:
            self.objects[name].place(x=x, y=y)
        return name

    def get(self, name: str):
        return self.objects[name]


def evl():
    print('Clicked')
    ws.get('Label-1')['text'] = eval(ws.get('Entry-1').get())


window = Tk()
global ws
ws = WebSpider(master=window)
ws.add('Label', {'text': 'Evaling: 0'})
ws.add('Entry', {'width': 10})
ws.add('Button', {'text': 'Eval!'}, func=evl)
print(ws.objects)
ws.start()
