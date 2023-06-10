with open('deforum_output_script.txt', 'w') as output_file:
  with open('deforum_input_script_3.txt', 'r') as input_file:
      # Read the file line by line
      for line in input_file:
          parts = line.split(": ")
          prefix = "A photography of"
          style = "ultrarealistic, photographic, and detailed"
          frame = int(parts[0]) + 60
          output_file.write(f"\"{frame}\":\"{prefix} {parts[1].strip()}, {style}\",\n")
