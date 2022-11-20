# Personalized strutter of logs

class personalized:
  def __init__(self, json_template_name, command_output):

    self.file = open(f"./logs/{json_template_name}_personalized.txt", 'w')
    self.command = command_output

  def __enter__(self):
    
    self.file.write(f"{self.command}, \n")
    return self.file

  def __exit__(self, exc_type, exc_value, Traceback):
    self.file.close()
