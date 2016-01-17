#!/usr/bin/python
#     TRIGRSInterface - Interface that facilitates data input for TRIGRS 2.0
#     Developed by Julian Camilo Marin Sanchez - marin.julian@gmail.com - @juliancms
#     Under the guidance of Roberto José Marín Sánchez - rjose.marin@udea.edu.co - @roberttwolf
# 
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
# 
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
# 
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

import Tkinter, os, tkFileDialog, ttk
from __builtin__ import str

class trigrsinterface(Tkinter.Tk):
    def __init__(self,parent):
        Tkinter.Tk.__init__(self,parent)
        self.parent = parent
        self.initialize()
    def initialize(self):
        
        vcmd_e = (self.register(self.validateexponent),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        vcmd_i = (self.register(self.validateiterations),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        vcmd_n = (self.register(self.validateidname),
                '%d', '%i', '%P', '%s', '%S', '%v', '%V', '%W')
        
        self.grid()
        
        #Elements
        
        self.ncols_e = ''
        self.nrows_e = ''
        self.flowdirection = 2
        self.elevationname = ''
        self.directionname = ''
        options = ('T', 'F')
        
        label = Tkinter.Label(self, text="Name of project")
        label.grid(column=0,row=0)
        
        self.projectname = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.projectname)
        self.entry.grid(column=0,row=1,sticky='EW')
        
        button_e = Tkinter.Button(self,text="Select elevation grid file", command= self.openelevation)
        button_e.grid(column=0,row=2)
        
        self.labelElevation = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=self.labelElevation)
        label.grid(column=0,row=3)
        
        button_d = Tkinter.Button(self,text="Select direction grid file", command= self.opendirection)
        button_d.grid(column=0,row=4)
        
        self.labelDirection = Tkinter.StringVar()
        label = Tkinter.Label(self, textvariable=self.labelDirection)
        label.grid(column=0,row=5)
        
        label = Tkinter.Label(self, text="Exponent")
        label.grid(column=0,row=6)
        
        self.exponent = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.exponent, validate='key', validatecommand = vcmd_e)
        self.entry.grid(column=0,row=7,sticky='EW')
        
        label = Tkinter.Label(self, text="Number of Iterations")
        label.grid(column=0,row=8)
        
        self.iterations = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.iterations, validate='key', validatecommand = vcmd_i)
        self.entry.grid(column=0,row=9,sticky='EW')
        
        label = Tkinter.Label(self, text="Save listing of D8 downslope neighbor cells?")
        label.grid(column=0,row=10)
        
        self.box1 = Tkinter.StringVar()
        self.box = ttk.Combobox(self, values=options, textvariable=self.box1, state='readonly')
        self.box.current(0)
        self.box.grid(column=0, row=11,sticky='EW')
        
        label = Tkinter.Label(self, text="Save grid of D8 downslope neighbor cells?")
        label.grid(column=0,row=12)
        
        self.box2 = Tkinter.StringVar()
        self.box = ttk.Combobox(self, values=options, textvariable=self.box2, state='readonly')
        self.box.current(0)
        self.box.grid(column=0, row=13,sticky='EW')
        
        label = Tkinter.Label(self, text="Save cell index number grid?")
        label.grid(column=0,row=14)
        
        self.box3 = Tkinter.StringVar()
        self.box = ttk.Combobox(self, values=options, textvariable=self.box3, state='readonly')
        self.box.current(0)
        self.box.grid(column=0, row=15,sticky='EW')
        
        label = Tkinter.Label(self, text="Save list of cell number and corresponding index number?")
        label.grid(column=0,row=16)
        
        self.box4 = Tkinter.StringVar()
        self.box = ttk.Combobox(self, values=options, textvariable=self.box4, state='readonly')
        self.box.current(0)
        self.box.grid(column=0, row=17,sticky='EW')
        
        label = Tkinter.Label(self, text="Save flow-direction grid remapped from ESRI to TopoIndex?")
        label.grid(column=0,row=18)
        
        self.box5 = Tkinter.StringVar()
        self.box = ttk.Combobox(self, values=options, textvariable=self.box5, state='readonly')
        self.box.current(0)
        self.box.grid(column=0, row=19,sticky='EW')
        
        label = Tkinter.Label(self, text="Name of folder to store output")
        label.grid(column=0,row=20)
        
        self.maps = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, text="maps", textvariable=self.maps)
        self.entry.grid(column=0,row=21,sticky='EW')
        
        label = Tkinter.Label(self, text="Id code for output files")
        label.grid(column=0,row=22)
        
        self.idname = Tkinter.StringVar()
        self.entry = Tkinter.Entry(self, textvariable=self.idname, validate='key', validatecommand = vcmd_n)
        self.entry.grid(column=0,row=23,sticky='EW')
        
        button_e = Tkinter.Button(self,text="Execute", command= self.execute)
        button_e.grid(column=0,row=24)
        
        # define options for opening or saving a file
        self.file_opt = options = {}
        options['defaultextension'] = '.txt'
        options['filetypes'] = [('text files', '.txt')]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'file.txt'
        
    def openelevation(self):
        fp = tkFileDialog.askopenfile(mode='r', **self.file_opt)
        for i, line in enumerate(fp):
            if i == 0:
                self.ncols_e = line.replace(" ", "")
                self.ncols_e = self.ncols_e.replace("ncols", "")
            if i == 1:
                self.nrows_e = line.replace(" ", "")
                self.nrows_e = self.nrows_e.replace("nrows", "")
                break
        fp.close()
        self.iterations.set(((int(self.nrows_e) + int(self.ncols_e)) / 20) + 1)
        self.elevationname = os.path.abspath(fp.name)
        self.labelElevation.set(os.path.abspath(fp.name))
        return True
    
    def opendirection(self):
        fp = tkFileDialog.askopenfile(mode='r', **self.file_opt)
        for i, line in enumerate(fp):
            if i == 0:
                ncols_d = line.replace(" ", "")
                ncols_d = ncols_d.replace("ncols", "")
            if i == 1:
                nrows_d = line.replace(" ", "")
                nrows_d = nrows_d.replace("nrows", "")
            if i > 5:
                numbers = line.split(' ')
                if(any(j > 9 for j in numbers)):
                    self.flowdirection = 1
        fp.close()
        self.directionname = os.path.abspath(fp.name)
        self.labelDirection.set(os.path.abspath(fp.name))
        return True
    
    def validateexponent(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if text in '0123456789-':
            return True
        return False
    
    def validateiterations(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if text in '0123456789':
            return True
        return False
        
    def validateidname(self, action, index, value_if_allowed,
                       prior_value, text, validation_type, trigger_type, widget_name):
        if len(self.idname.get()) < 8:
            return True
        return False
    
    def execute(self):
        tpx_in = open("tpx_in.txt", "w")
        tpx_in.write("Name of project (up to 255 characters)\n")
        tpx_in.write(self.projectname.get() + "\n")
        tpx_in.write("Rows, Columns, flow-direction numbering scheme (ESRI=1, TopoIndex=2)\n")
        tpx_in.write(str(int(self.ncols_e)) + ", " + str(int(self.nrows_e)) + ", " + str(self.flowdirection) + "\n")
        tpx_in.write("Exponent, Number of iterations\n")
        tpx_in.write(self.exponent.get() + ", " + self.iterations.get() + "\n")
        tpx_in.write("Name of elevation grid file\n")
        tpx_in.write(self.elevationname + "\n")
        tpx_in.write("Name of direction grid\n")
        tpx_in.write(self.directionname + "\n")
        tpx_in.write("Save listing of D8 downslope neighbor cells?  Enter T (.true.) or F (.false.)\n")
        tpx_in.write(self.box1.get() + "\n")
        tpx_in.write("Save grid of D8 downslope neighbor cells? Enter T (.true.) or F (.false.)\n")
        tpx_in.write(self.box2.get() + "\n")
        tpx_in.write("Save cell index number grid?  Enter T (.true.) or F (.false.)\n")
        tpx_in.write(self.box3.get() + "\n")
        tpx_in.write("Save list of cell number and corresponding index number? Enter T (.true.) or F (.false.)\n")
        tpx_in.write(self.box4.get() + "\n")
        tpx_in.write("Save flow-direction grid remapped from ESRI to TopoIndex? Enter T (.true.) or F (.false.)\n")
        tpx_in.write(self.box5.get() + "\n")
        tpx_in.write("Name of folder to store output?\n")
        tpx_in.write(self.maps.get() + "\n")
        tpx_in.write("ID code for output files? (8 characters or less)\n")
        tpx_in.write(self.idname.get() + "\n")
        tpx_in.close()
        os.system("TopoIndex.exe")
        return True
        
if __name__ == "__main__":
    app = trigrsinterface(None)
    app.title('TRIGRSInterface')
    app.maps.set("maps\\")
    app.mainloop()