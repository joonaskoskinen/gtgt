import zipfile
import os

zip_path = "/vercel/share/v0-project/Uusi WinRAR ZIP archive (2).zip"
extract_to = "/vercel/share/v0-project/extracted"

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
