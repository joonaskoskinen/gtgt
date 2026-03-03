import zipfile
import os
import subprocess

# Find zip files anywhere on the system
result = subprocess.run(["find", "/", "-name", "*.zip", "-type", "f"], capture_output=True, text=True, timeout=10)
print("Found zip files:")
print(result.stdout)
if result.stderr:
    print("Errors:", result.stderr[:500])

zip_files = [f.strip() for f in result.stdout.strip().split("\n") if f.strip()]

if not zip_files:
    raise FileNotFoundError("No zip files found")

zip_path = zip_files[0]
extract_to = "/home/user/extracted"
print(f"Using: {zip_path}")

with zipfile.ZipFile(zip_path, 'r') as z:
    print("ZIP-tiedoston sisalto:")
    print("-" * 60)
    for info in z.infolist():
        size = info.file_size
        name = info.filename
        print(f"  {size:>10} bytes  {name}")
    print("-" * 60)
    print(f"\nYhteensa {len(z.infolist())} tiedostoa/kansiota")
    
    # Extract all
    z.extractall(extract_to)
    print(f"\nPurettu kansioon: {extract_to}")
