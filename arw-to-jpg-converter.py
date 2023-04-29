import tkinter as tk
from tkinter import filedialog
import subprocess
import os

# Define the PowerShell script path
ps_script = os.path.abspath("Convert-ARWtoJPG.ps1")

def browse_input_dir():
    """Open a file dialog to select the input directory."""
    input_dir = filedialog.askdirectory()
    input_entry.delete(0, tk.END)
    input_entry.insert(0, input_dir)

def browse_output_dir():
    """Open a file dialog to select the output directory."""
    output_dir = filedialog.askdirectory()
    output_entry.delete(0, tk.END)
    output_entry.insert(0, output_dir)

def convert_arw_to_jpg():
    """Run the PowerShell script to convert ARW files to JPG format."""
    # Get the input and output directory paths from the GUI
    input_dir = input_entry.get()
    output_dir = output_entry.get()

    # Construct the PowerShell command
    ps_command = f"powershell.exe -ExecutionPolicy ByPass -File {ps_script} -inputDir '{input_dir}' -outputDir '{output_dir}'"

    # Run the PowerShell command
    subprocess.run(ps_command, shell=True)

# Create the GUI window
root = tk.Tk()
root.title("ARW to JPG Converter")
root.geometry("500x300")

# Create the input directory label and entry
input_label = tk.Label(root, text="Input directory:", font=("Arial", 14))
input_label.pack(side=tk.TOP)
input_entry = tk.Entry(root, font=("Arial", 14))
input_entry.pack(side=tk.TOP)
input_button = tk.Button(root, text="Browse...", font=("Arial", 14), command=browse_input_dir)
input_button.pack(side=tk.TOP)

# Create the output directory label and entry
output_label = tk.Label(root, text="Output directory:", font=("Arial", 14))
output_label.pack(side=tk.TOP)
output_entry = tk.Entry(root, font=("Arial", 14))
output_entry.pack(side=tk.TOP)
output_button = tk.Button(root, text="Browse...", font=("Arial", 14), command=browse_output_dir)
output_button.pack(side=tk.TOP)

# Create the convert button
convert_button = tk.Button(root, text="Convert", font=("Arial", 14), command=convert_arw_to_jpg)
convert_button.pack(side=tk.TOP)

# Create the signature/credits label
signature_label = tk.Label(root, text="Created by: @joosefupas", font=("Courier", 16))
signature_label.pack(side=tk.BOTTOM, pady=20)

# Run the GUI
root.mainloop()
