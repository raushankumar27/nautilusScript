#!/usr/bin/env python3
import os
from subprocess import call,Popen,PIPE
input_file=os.environ['NAUTILUS_SCRIPT_SELECTED_FILE_PATHS']
input_file=input_file.strip()
os.system("gnome-terminal -- ffmpeg -i \""+input_file+"\" -vn \""+input_file+".mp3\""+"") 


