import xml.etree.ElementTree as ET
import subprocess

# Load metadata
tree = ET.parse("metadata.xml")
root = tree.getroot()

package_name = root.find("name").text
version = root.find("version").text
description = root.find("description").text
dependencies = [dep.text for dep in root.find("dependencies")]

print(f"Installing {package_name} v{version}...")
print(description)

# Install dependencies
for dep in dependencies:
    subprocess.run(["pip", "install", dep])

print("Installation complete!")
