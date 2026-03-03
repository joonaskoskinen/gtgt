import { readFileSync } from 'fs';
import { join, dirname } from 'path';
import { fileURLToPath } from 'url';
import { execSync } from 'child_process';

const __dirname = dirname(fileURLToPath(import.meta.url));
const projectDir = join(__dirname, '..');

console.log("Project dir:", projectDir);
console.log("Files in project dir:");
const files = execSync(`ls -la "${projectDir}"`).toString();
console.log(files);

// Try to find the zip
const zipFiles = execSync(`find "${projectDir}" -maxdepth 1 -name "*.zip" -type f 2>/dev/null || true`).toString().trim();
console.log("Zip files found:", zipFiles);

if (zipFiles) {
  const zipPath = zipFiles.split('\n')[0];
  console.log(`\nListing contents of: ${zipPath}`);
  try {
    const output = execSync(`unzip -l "${zipPath}"`).toString();
    console.log(output);
  } catch (e) {
    console.log("unzip not available, trying python:");
    const output = execSync(`python3 -c "import zipfile; z=zipfile.ZipFile('${zipPath}'); z.printdir()"`).toString();
    console.log(output);
  }
}
