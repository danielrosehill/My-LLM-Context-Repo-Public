import os
import shutil
import json

def copy_json_files(source_dir, target_dir):
  """
  Recursively copies all JSON files within a directory to a target directory, naming the copied files after the source directory.

  Args:
    source_dir: The directory to search for JSON files.
    target_dir: The directory to copy the files to.
  """

  for root, _, files in os.walk(source_dir):
    for file in files:
      if file.endswith(".json"):
        source_path = os.path.join(root, file)
        relative_path = os.path.relpath(root, source_dir)
        target_file = os.path.join(target_dir, f"{relative_path}.json")

        # Create the target directory if it doesn't exist
        os.makedirs(os.path.dirname(target_file), exist_ok=True)

        # Copy the file
        shutil.copy2(source_path, target_file)
        print(f"Copied '{source_path}' to '{target_file}'")

if __name__ == "__main__":
  # Get the current directory
  current_dir = os.getcwd()

  # Create the target directory one level up
  target_dir = os.path.join(current_dir, "..", "JSON")

  # Call the function to copy the JSON files
  copy_json_files(current_dir, target_dir)