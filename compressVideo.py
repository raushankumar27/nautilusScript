#!/usr/bin/env python3
import os
from subprocess import call,Popen,PIPE
input_file=os.environ['NAUTILUS_SCRIPT_SELECTED_FILE_PATHS']
input_file=input_file.strip()
file_name=input_file.rsplit('.',1)
os.system("gnome-terminal -- ffmpeg -i \""+input_file+"\" -vcodec libx264 -crf 24 \""+file_name[0]+"_compressed."+file_name[1]+"\""+"") 


