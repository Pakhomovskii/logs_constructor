
import os
import json
import datetime
import subprocess
from contextlib import contextmanager

from type_of_time import Time
from personal_structure import personalized


json_template_name = input(""" 
                  Type the name of your template file without '.json' suffix. \n
                  For example: 'your_template' \n
                  or press the 'enter' button if you want to use standard_structure template \n
                      """)

if json_template_name:
  with open(f"./templates/{json_template_name}.json", 'r') as f:
        template_dict = json.load(f)
        print(template_dict) # TODO DELETEME 

  
  for dict_key, dict_value in template_dict.items():
    if "command" in dict_key:
      with personalized(json_template_name,dict_value) as per_log:
        command_output = subprocess.check_output(dict_value)
        per_log.write(command_output)

    print('Personalized log Generated! \n')


else:
  with open("./templates/standard_structure.json", 'r') as f:
    template_dict = json.load(f)

  name_of_temp = template_dict["name_of_temp"]
  command = template_dict["command"]
  time = template_dict["time"]
  discInfo = template_dict["sourceInfo"]
  memoryInfo = template_dict["memoryInfo"]

  @contextmanager
  def generic(logs_name="no_spec", time_enum = time, memoryInfo=False, discInfo=False):

    # TODO:find out how to create new log_file without removing previous one
    gen_log = open(f"./logs/{logs_name}_generic.txt", 'w') 
    try:
      main_command_output = subprocess.check_output(command, shell=True)
      # now_time = Time.time_enum TODO:realize enum choice
      if memoryInfo:
        memoryInfo_command_output = subprocess.check_output("df -h", shell=True)
      else:
        memoryInfo_command_output= ""
        
      if discInfo: 
        discInfo_command_output = subprocess.check_output("grep MemTotal /proc/meminfo", shell=True)
      else:
        discInfo_command_output = ""

      gen_log.write(f"""{logs_name}, \n 
                      {memoryInfo_command_output}, \n, 
                      {discInfo_command_output}, \n, 
                      {main_command_output}""")
      yield gen_log

    finally:
      gen_log.close()

  #TODO improve output
  with generic(name_of_temp, discInfo, memoryInfo) as gen_log: 
    print('Standard log Generated! \n')
