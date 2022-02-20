#!/usr/binenv python2.7
# -*- coding: utf-8 -*-
""" Note:
    Download IronPython 2.7.9 from https://github.com/IronLanguages/ironpython2/releases/tag/ipy-2.7.9
"""

# - - - - - - - - IN-BUILT IMPORTS

import os, shutil

# - - - - - - - - CLASS LIBRARY

class Compiler:

    @staticmethod
    def collect_files(folder_path):

        files = []
        ignore_list = (__file__, "__init__.py")

        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                abs_path = os.path.join(folder_path, file)
                # ignore current file, and from ignore_list.
                if not abs_path in ignore_list and file.endswith(".py"):
                    files.append(abs_path)
                # Recursiion for sub-folders
                elif os.path.isdir(abs_path) and abs_path.lower() not in ignore_list:
                    files += Compiler.collect_files(abs_path)
        
        return files
    
    @staticmethod
    def Build(filename, copy_target = "", export_folder = "bin"):
        
        folder_name = os.path.dirname(os.path.abspath(__file__))
        target_folder = os.path.join(folder_name, export_folder)
        target_file = os.path.join(target_folder, filename)

        # Create export folder
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)
        
        program_files = Compiler.collect_files(folder_name)

        try:
            from clr import CompileModules
            CompileModules(target_file, *program_files)
            print("\nBUILD SUCCESSFUL")
            print("Target: {}\n".format(target_file))
            
            if copy_target and os.path.exists(copy_target):
                shutil.copy2(target_file, copy_target)
                print("COPY SUCCESSFUL\n")
        except:
            print("BUILD FAILED\n")

# - - - - - - - - RUN SCRIPT

def Run():
    Compiler.Build("inhaus.dll")

if __name__ == "__main__":
    Run()
