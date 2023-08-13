# Code generated using Google Bard
import sys

def concatenate_file(output_filename, filename):
  """Concatenates all the lines of a file as a comma separated string and writes it to another file, removing any lines if they start with //."""
  with open(filename, "r") as f:
    lines = f.readlines()
    lines = [line.strip() for line in lines]
    filtered_lines = [line for line in lines if not line.startswith("//") and line]
    concatenate_string = ",".join(filtered_lines)

  with open(output_filename, "w") as f:
    f.write(concatenate_string)

if __name__ == "__main__":
  output_filename = sys.argv[1]
  filename = sys.argv[2]
  concatenate_file(output_filename, filename)