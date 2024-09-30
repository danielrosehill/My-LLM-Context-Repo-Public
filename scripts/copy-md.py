import os
import shutil

def copy_markdown_files(source_dir, target_dir):
  """
  Recursively copies all Markdown files within a directory to a target directory, 
  naming the copied files after the source directory.
  """
  for root, _, files in os.walk(source_dir):
    for file in files:
      if file.endswith(".md"):
        source_path = os.path.join(root, file)
        # Get the folder name relative to the source directory
        folder_name = os.path.basename(root)
        # Create the target path using the folder name
        target_file = os.path.join(target_dir, f"{folder_name}.md")
        os.makedirs(os.path.dirname(target_file), exist_ok=True)
        shutil.copy2(source_path, target_file)
        print(f"Copied '{source_path}' to '{target_file}'")

if __name__ == "__main__":
  # Get the current directory
  current_dir = os.getcwd()

  # Create the target directory one level shallower
  target_dir = os.path.join(current_dir, "..", "MD")

  # Call the function to copy the Markdown files
  copy_markdown_files(current_dir, target_dir)