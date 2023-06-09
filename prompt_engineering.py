with open('deforum_output_script.txt', 'w') as output_file:
  with open('deforum_input_script_detailed.txt', 'r') as input_file:
      # Read the file line by line
      for line in input_file:
          parts = line.split(": ")
          style = "trending on artstation, happy ambience, happy colors"
          output_file.write(f"\"{parts[0]}\":\"{parts[1].strip()}, {style}\",\n")
