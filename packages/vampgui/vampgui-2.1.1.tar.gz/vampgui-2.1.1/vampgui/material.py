# -*- coding: utf-8 -*-
#
# Author: G. Benabdellah
# Departement of physic
# University of Tiaret , Algeria
# E-mail ghlam.benabdellah@gmail.com
#
# this program is part of VAMgui 
# first creation 28-05-2024
#  
#
# License: GNU General Public License v3.0
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
#  log change:
# 04/11/2024
#

import re
import os
import tkinter as tk
from tkinter import filedialog
from tkinter import scrolledtext, messagebox,ttk
from vampgui.file_io import InputFileViewer 
from vampgui.helpkey import  show_help




class MainInputTab:
    def __init__(self, tab):
        self._canvas(tab)
        frame=self.frame
        self._button_frame(frame)
        self._sub_notebook(frame)
        self.material_attributes(tab)
        #self.load_default_values()
        self.new_indices = {}                                     # for added indexed suffix like exchange-matrix[index]
        self.k_list = []                                          # to add more indexed suffix  to list
        self.load_input_values                                    # imported  material attributes keywords
        self.all_material_suffix = list(self.default_values.keys())  # full material attributes  keywords
        self.samples = []
        self.indx =0
        self.add_sample(self.sample_tab)


#==========================
#==========================
    def add_sample(self, tab):
        index = len(self.samples) + 1
        
        self.indx += 1
        frame = tk.LabelFrame(tab, text=f"Sample {index} : Material attributes (Note: Before import the .mat file or add sample, ensure you add the necessary indexed material suffix by clicking on the + button.)",font=("Helvetica", 12, "bold"))
        frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, padx=5, pady=(5, 5))
        entries = {}
        row = 0
        col = 0
        self.max_row = 13  # Set the maximum number of rows
        Padx = 0
        Wdth = 14
        indexed_mat_suffix=[ "exchange-matrix[1]=", "biquadratic-exchange[1]=", "neel-anisotropy-constant[1]=", "alloy-fraction[1]=", "intermixing[1]="]

        for mat_suffix in self.all_material_suffix:
            ncol = 3 * col
            var = tk.BooleanVar()
            check = tk.Checkbutton(frame, text=mat_suffix, variable=var, font=13)
            check.config(command=lambda skw=mat_suffix, v=var, chk=check: self.set_color_selected_prefix(skw, v, chk))
            check.grid(row=row, column=ncol+1, sticky="w")
            loaded_value = self.default_values[mat_suffix]
            pur_mat_suffix = mat_suffix.strip().strip("=").strip()

            if pur_mat_suffix == "num-materials":
                entry = tk.Entry(frame, width=Wdth, state='disabled')
                entry.grid(row=row, column=ncol+2, sticky="w", padx=Padx)
                entry.insert(0, loaded_value)
                var.set(True)
                entries[mat_suffix] = (var, entry, check)
            elif pur_mat_suffix == "non-magnetic":
                entry = ttk.Combobox(frame, values=["remove", "keep"], state="readonly", width=Wdth)
                entry.grid(row=row, column=ncol+2, padx=Padx  , sticky="e")
                if loaded_value.lower() in ["remove", "keep"]:
                    entry.set(loaded_value.lower())
                    entry.insert(0, loaded_value)
                else:
                    entry.set("remove")
                    entry.insert(0, "remove")
                entries[mat_suffix] = (var, entry, check)
                
                
            elif pur_mat_suffix == "alloy-distribution":
                entry = ttk.Combobox(frame, values=["native", "reciprocal" , "homogeneous"], state="readonly", width=Wdth)
                entry.grid(row=row, column=ncol+2, padx=Padx  , sticky="e")
                if loaded_value.lower() in ["native", "reciprocal" , "homogeneous"]:
                    entry.set(loaded_value.lower())
                    entry.insert(0, loaded_value)
                else:
                    entry.set("native")
                    entry.insert(0, "native")
                entries[mat_suffix] = (var, entry, check)
                
            elif loaded_value == "none":
                entry = tk.Entry(frame, width=Wdth, state='disabled')
                entry.grid(row=row, column=ncol+2, sticky="w", padx=Padx)
                entry.insert(0, loaded_value)
                entries[mat_suffix] = (var, entry, check)
            else:
                entry = tk.Entry(frame, bg='white', width=Wdth)
                entry.grid(row=row, column=ncol+2, sticky="w", padx=Padx)
                entry.insert(0, loaded_value)
                entries[mat_suffix] = (var, entry, check)

            help_button = tk.Button(frame, text="?", command=lambda kw=mat_suffix: show_help(kw)) 
            help_button.grid(row=row, column=ncol+3,padx=1, sticky="w")
            # Add a button to dynamically add more mat_suffix
            if mat_suffix in indexed_mat_suffix:
                add_plus_button = tk.Button(frame, text="+", command=lambda   skw=mat_suffix: self.add_indexed_suffix(frame,skw))
                add_plus_button.grid(row=row, column=ncol+3, padx=35, sticky="e")
            row += 1
            if row == self.max_row:
                row = 0
                col += 1
            
        self.last_row=row
        self.max_col=col
        self.samples.append((frame, entries))
        self.k_list.append((f'material[{index}]', entries))


    def add_indexed_suffix(self, frame, suffix):
        pur_suffix = suffix.strip().strip("=").strip()
        indexed_suffix = pur_suffix.split("[")[0]

        # Initialize the index for this  suffix type if not already done
        if indexed_suffix not in self.new_indices:
            self.new_indices[indexed_suffix] = 2
        else:
            # Increment the index for this suffix type
            self.new_indices[indexed_suffix] += 1

        new_suffix = f"{indexed_suffix}[{self.new_indices[indexed_suffix]}]="
        if self.last_row == self.max_row:
            self.last_row = 0
            self.max_col += 1

        row = self.last_row
        col = self.max_col

        var = tk.BooleanVar()
        check = tk.Checkbutton(frame, text=new_suffix, variable=var, font=13)
        check.config(command=lambda skw=new_suffix, v=var, chk=check: self.set_color_selected_prefix(skw, v, chk))
        check.grid(row=row, column=3 * col + 1, sticky="w")

        entry = tk.Entry(frame, bg='white', width=10)
        entry.grid(row=row, column=3 * col + 2, sticky="w")
        entry.insert(0, "0.0")
        self.all_material_suffix.append(new_suffix)

        # Add the new suffix to default_values with an initial default value
        self.default_values[new_suffix] = "0.0"  # Set the initial value as needed

        # Update self.samples and self.k_list
        self.samples[-1][1][new_suffix] = (var, entry, check)
        self.k_list[-1][1][new_suffix] = (var, entry, check)
        self.last_row += 1
#==========================
    def _canvas(self,tab):
        # Create a canvas
        def configure_scroll_region(event):
            canvas.configure(scrollregion=canvas.bbox("all"))
        canvas = tk.Canvas(tab)
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        frame = tk.Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor=tk.NW)
        v_scrollbar = tk.Scrollbar(tab, orient=tk.VERTICAL, command=canvas.yview, bg='black')
        v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        canvas.config(yscrollcommand=v_scrollbar.set)
        h_scrollbar = tk.Scrollbar(tab, orient=tk.HORIZONTAL, command=canvas.xview, bg='black')
        h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        canvas.config(xscrollcommand=h_scrollbar.set)
        canvas.bind_all("<MouseWheel>", lambda event: canvas.yview_scroll(-1 * int(event.delta / 120), "units"))
        canvas.bind_all("<Shift-MouseWheel>", lambda event: canvas.xview_scroll(-1 * int(event.delta / 120), "units"))
        frame.bind("<Configure>", configure_scroll_region)
        # Create a notebook for sub-tabs
        self.frame=frame
        
    def _sub_notebook(self,frame):
        sub_notebook = ttk.Notebook(frame)
        sub_notebook.pack(side=tk.TOP, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.sample_tab = ttk.Frame(sub_notebook)
        sub_notebook.add(self.sample_tab, text="Sample")
       
    def _button_frame(self,frame):
        button_frame = tk.Frame(frame)
        button_frame.pack(side=tk.TOP, fill=tk.X, padx=10, pady=10)      
        tk.Button(button_frame, bg='cyan'   , text="Add Sample"             , command=lambda: self.add_sample(self.sample_tab)).grid(row=0, column=0, padx=5, pady=5,sticky="w")
        tk.Button(button_frame, bg='bisque' , text="Import from file.mat"   , command=self.load_file).grid(row=0, column=1, padx=5, pady=5, sticky="w")
        tk.Button(button_frame, bg='#99ff99', text="Save to sample.mat"     , command=self.save_to_file).grid(row=0, column=2, padx=5, pady=5,sticky="w")
        tk.Button(button_frame, bg='#ffff99', text="View/Edit sample.mat"   , command=self.open_sample_file).grid(row=0, column=3,padx=5, pady=5,sticky="w")
        tk.Button(button_frame, text="                      ",).grid(row=0  , column=4, padx=4, pady=5, sticky="e")
        tk.Button(button_frame, bg='#ff9999', text="Deselect All", command=self.deselect_all_checkboxes).grid(row=0, column=5, padx=5, pady=5, sticky="e")
        tk.Button(button_frame, bg='#ff9999', text="Remove Last Sample", command=self.remove_sample).grid(row=0, column=6,padx=5, pady=5,sticky="e")

#==========================
    def set_color_selected_prefix(self, subkeyword, var, check):
        if var.get():
            self.set_checkbox_color(check, 'blue')
            sub_key=subkeyword.strip().strip("=").strip() 
        else:
            self.set_checkbox_color(check, 'black')
#==========================
    def open_sample_file(self):
        InputFileViewer("sample.mat")
##==========================
    #def deselect_checkbox(self, suffix):
        #pur_suffix=suffix.strip().strip("=").strip()
        #if pur_suffix in shaps:
            #for keyword, entries in self.k_list:
                #if suffix in entries:
                    #entries[suffix][0].set(False)
##======================                
    def set_checkbox_color(self, checkbutton, color):
        checkbutton.config(fg=color) 
#==========================        
    #def select_checkbox(self, subkeyword):
        #sub_key=subkeyword.strip().strip("=").strip()
        #if sub_key in shaps:
            #for keyword, entries in self.k_list:
                #if subkeyword in entries:
                    #entries[subkeyword][0].set(True)
#==========================
# deselect all chekedbox
    def deselect_all_checkboxes(self):
        for keyword , entries in self.k_list:
            for var, _ , check in entries.values():
                var.set(False)      
                self.set_checkbox_color(check, 'black')
#==========================
    def remove_sample(self):
        if self.samples:
            frame, entries = self.samples.pop()
            if frame.winfo_exists():  # Check if the widget still exists
                frame.destroy()
                self.k_list.pop()
                self.indx -=1
                #print(self.indx )
                if self.indx == 0:
                    self.add_sample(self.sample_tab)
                    
##==========================
       
    def load_input_values(self, file_path):
        for i in range(self.indx):
            self.remove_sample()
        suffix_list=[]
        for _, entries in self.k_list:
            for suffix_words, (var, entry, check) in entries.items():
                suffix_list.append(suffix_words.strip().strip("="))
        try:
            with open(file_path, "r") as file:
                self.deselect_all_checkboxes()    # deselect all checkboxes before import a new file
                lines = file.readlines()
                total_lines=0
                num_loaded_lines=0
                unknown_prefix=""
                unknown_suffix=""
                pattern="num-materials"
                for line in lines:
                    if line.strip().startswith("#"):
                        continue
                    match=re.search(fr"{pattern}\s*=\s*(\d+)", line)
                    if match:
                        #print(f'Found number after "{pattern}": {match.group(1)}')
                        num =int(match.group(1))
                        if num>1 and   num> int(self.indx):
                                for i in range(num-1):
                                    self.add_sample(self.sample_tab)
                                    
                        break
                        
                suffix_values={}
                for line in lines:
                    line = line.lstrip()
                    str_line = line.strip()
                    if ":" in line and not str_line.startswith('#'):
                        
                        total_lines +=1
                        material_suffix, value = re.split(r'\s|=', line, maxsplit=1)
                        material = material_suffix.strip().split(":")[0]
                        material =material.split("[")[0]
                        suffix = material_suffix.strip().split(":")[1]
                        suffix =suffix.strip().strip("=")
                        value = value.strip().strip("=").strip()
                        #print(material,suffix, value)
                        
                        
                        if material =="material":
                            if suffix in suffix_list:
                                num_loaded_lines +=1
                                if suffix =="alloy-host":
                                    suffix = "host-alloy"
                                value = value.strip().strip("=")
                                
                                if suffix in suffix_values:
                                    suffix_values[suffix].append(value)  # Append to existing list
                                else:
                                    suffix_values[suffix] = [value]      # Create a new list if word is new
                            else:
                                unknown_suffix =  f" {unknown_suffix} \n {material_suffix}"
                        else:
                            unknown_prefix =  f" {unknown_prefix} \n {material_suffix}"
    
                             
                if unknown_prefix != "" or unknown_suffix != "":            
                    with open("ERROR.log", 'w') as flog:
                        flog.write("the list keywords  not found in List of VAMGUI\n")
                        flog.write("---------------------------------------------\n")
                        flog.write(f"{unknown_prefix}")                
                self.inputfile = file_path
                
                suffix_values.pop("num-materials", None) 
                target_length = max(len(values) for values in suffix_values.values())
                # Append default values to each list until they reach the target length
                for key, values in suffix_values.items():
                    while len(values) < target_length:
                        values.append(suffix_values[key][0])  # Ap
                
                
                for suffix, value in suffix_values.items():
                    i=0
                    #print("suffix",suffix)
                    for _ , entries in self.k_list:
                        for suffix_words, (var, entry, check) in entries.items():
                            #print("suffix_words",suffix_words)
                            if suffix_words.strip("=").strip() == suffix:
                                var.set(True)
                                self.set_checkbox_color(check, 'blue')
                                if isinstance(entry, tk.Entry):
                                    entry.delete(0, tk.END)
                                    entry.insert(0, suffix_values[suffix][i])
                                    i +=1
                                if isinstance(entry, ttk.Combobox):                                       
                                    if suffix_values[suffix][i] in entry['values']:
                                        entry.set(suffix_values[suffix][i])
                                        entry.insert(0, suffix_values[suffix][i])
       
            
            if unknown_prefix != "" or unknown_suffix != "":
                messagebox.showinfo("Echec !!",f"Number of lines not loaded: {total_lines-num_loaded_lines} \n Unknown prefix:\n{unknown_prefix} \n Unknown suffix:\n  {unknown_suffix}"    )
            else:
                messagebox.showinfo("Success" ,f"File loaded successfully! \n Number of loaded keyword: {num_loaded_lines} \n Number of Total keyword: {total_lines}\n")
        except FileNotFoundError:
            messagebox.showinfo("Echec !!",f"File {file_path} not found." )
            #print(f"File {file_path} not found.")
        except Exception as e:
            messagebox.showinfo("Echec !!",f"An error occurred: {e}\n check .mat file ( num-materials ..)")
            #print(f"An error occurred: {e}")  
#============================================
    def load_file(self):
        file_path = filedialog.askopenfilename(title="Select file", filetypes=[("input files", "*"), ("All files", "*.*")])
        if file_path:
            self.load_input_values(file_path)      
#=============================================    
    # Add other methods as needed"""
    def close_window(self):
        # Save the file before closing
        self.save_to_file()
        # Close the window
        # Add your code to close the window here
#==========================
    def save_to_file(self):
        filename = "sample.mat"
        with open(filename, 'w') as file:
            file.write("#===================================================\n")
            file.write("# Sample vampire material file .mat\n")
            file.write("#===================================================\n\n")
            file.write(f"material:num-materials={len(self.samples)}\n\n")
            for index, (frame, entries) in enumerate(self.samples, start=1):
                file.write(f"#---------------------------------------------------\n")
                file.write(f"# sample {index}\n")
                file.write(f"#---------------------------------------------------\n")
                for subkeys, (var, entry, _) in entries.items():
                    if subkeys.strip().strip("=") != "num-materials":
                        if var.get():
                            file.write(f"material[{index}]:{subkeys} {entry.get().strip()}\n")
                file.write("\n")
        messagebox.showinfo("Success", f"File '{filename}' saved successfully!")
#==========================
    def material_attributes(self, tab):
            # Dictionary of default values
            self.default_values = {
            "num-materials=": "none",
            "unit-cell-category=": "0",
            "material-name=": "Cobalt", 
            "damping-constant=": "1.0", 
            "exchange-matrix[1]=": "0.0 J/link",
            #"exchange-matrix[2]=": "0.0 J/link", 
            #"exchange-matrix[3]=": "0.0 J/link", 
            #"exchange-matrix-1st-nn[1]=": "0.0 J/link", 
            #"exchange-matrix-1st-nn[2]=": "0.0 J/link",
            #"exchange-matrix-2nd-nn[1]=": "0.0 J/link",
            #"exchange-matrix-2nd-nn[2]=": "0.0 J/link", 
            #"exchange-matrix-3rd-nn[1]=": "0.0 J/link",
            #"exchange-matrix-3rd-nn[2]=": "0.0 J/link", 
            #"exchange-matrix-4th-nn[1]=": "0.0 J/link",
            #"exchange-matrix-4th-nn[2]=": "0.0 J/link", 
            "biquadratic-exchange[1]=": "0.0 J/link", 
            #"biquadratic-exchange[2]=": "0.0 J/link",
            "atomic-spin-moment=": "1.72 !muB", 
            "surface-anisotropy-constant=": "0.0 J/atom", 
            "neel-anisotropy-constant[1]=": "0.0 J", 
            #"neel-anisotropy-constant[2]=": "0.0 J", 
            "lattice-anisotropy-constant=": "0.0 J/atom", 
            "relative-gamma=": "1",
            "initial-spin-direction=": "0, 0, 1",
            "material-element=": "Fe", 
             
            "alloy-fraction[1]=": "0.0",
            #"alloy-fraction[2]=": "0.0",  
            "minimum-height=": "0.0", 
            "maximum-height=": "1.0", 
            "core-shell-size=": "1.0", 
            "interface-roughness=": "1.0",
            "intermixing[1]=": "1.0",
            #"intermixing[2]=": "1.0", 
            "density=": "1.0",
            "uniaxial-anisotropy-constant=": "0.0 J/atom",
            "uniaxial-anisotropy-direction=": "0,0,1",
            "cubic-anisotropy-constant=": "0.0 J/atom", 
            "second-order-uniaxial-anisotropy-constant=": "0.0  J/atom", 
            "fourth-order-uniaxial-anisotropy-constant=": "0.0  J/atom", 
            "sixth-order-uniaxial-anisotropy-constant" : "0.0 J/atom" ,
            "fourth-order-cubic-anisotropy-constant=" : "0.0 J/atom",
            "sixth-order-cubic-anisotropy-constant=" :  "0.0 J/atom",
            #"couple-to-phononic-temperature=": "off",
            "temperature-rescaling-exponent=": "1.0", 
            "temperature-rescaling-curie-temperature=": "0.0",
            "non-magnetic=": "remove",
            "host-alloy=": "none",
            "continuous ": "none",
            "fill-space=": "none",
            "geometry-file=": " ", 
            "lattice-anisotropy-file=": " ",
            "alloy-distribution" : " ",
            "alloy-variance" : "0.0",
            #"voltage-controlled-magnetic-anisotropy-coefficient=": "0.0 J/V"
        }

#def main():
    #root = tk.Tk()
    #app = MainInputTab (root)
    #root.mainloop()

#if __name__ == "__main__":
    #main()
    
  
