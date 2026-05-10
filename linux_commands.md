# Linux Commands for Bioinformatics

## Navigation Commands

```bash
pwd
```
Show current directory path.

```bash
ls
```
List files and folders.

```bash
ls -l
```
Detailed file list.

```bash
ls -a
```
Show hidden files.

```bash
cd folder_name
```
Move into a directory.

```bash
cd ..
```
Go back one directory.

---

# File & Directory Management

```bash
mkdir project_name
```
Create a new directory.

```bash
rm file.txt
```
Remove a file.

```bash
rm -r folder_name
```
Remove a directory recursively.

```bash
cp file1.txt file2.txt
```
Copy files.

```bash
mv old.txt new.txt
```
Move or rename files.

```bash
touch file.txt
```
Create an empty file.

---

# Viewing File Content

```bash
cat file.txt
```
Display full file content.

```bash
less file.txt
```
Open large text files interactively.

```bash
head file.fastq
```
Show first lines of a file.

```bash
tail file.fastq
```
Show last lines of a file.

---

# Searching & Filtering

```bash
grep "ATCG" file.txt
```
Search for patterns inside files.

```bash
find . -name "*.fastq"
```
Find FASTQ files.

---

# Permissions

```bash
chmod +x script.sh
```
Make script executable.

```bash
chmod 755 script.sh
```
Change file permissions.

---

# Compression

```bash
gzip file.fastq
```
Compress file.

```bash
gunzip file.fastq.gz
```
Extract compressed file.

---

# System Information

```bash
top
```
Monitor system processes.

```bash
df -h
```
Check disk space.

```bash
free -h
```
Check memory usage.

---

# Bioinformatics Related Commands

```bash
fastqc sample.fastq
```
Run FastQC quality analysis.

```bash
python script.py
```
Run Python script.

```bash
bash pipeline.sh
```
Run shell script.

---

# Git Commands

```bash
git status
```
Check repository status.

```bash
git add .
```
Stage all changes.

```bash
git commit -m "message"
```
Create commit.

```bash
git push
```
Upload changes to GitHub.

---

# Notes

Linux is essential for:
- NGS analysis
- Bioinformatics pipelines
- HPC environments
- Automation workflows
