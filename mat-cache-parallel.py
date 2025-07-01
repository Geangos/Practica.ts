# mat-cache-parallel.py
import os
import time
import glob
import multiprocessing
from functools import lru_cache

INPUT_DIR = "/mnt/input"
OUTPUT_DIR = "./output"
CACHE_SIZE = 10000  # Adjust based on memory

os.makedirs(OUTPUT_DIR, exist_ok=True)

@lru_cache(maxsize=CACHE_SIZE)
def process_matrix_line(line):
    # Dummy processing: return line reversed (replace with real logic)
    return line.strip()[::-1] + "\n"

def process_file(filepath):
    filename = os.path.basename(filepath)
    output_path = os.path.join(OUTPUT_DIR, filename.replace(".in", ".out"))

    with open(filepath, 'r') as fin, open(output_path, 'w') as fout:
        for line in fin:
            fout.write(process_matrix_line(line))

def main():
    start = time.time()
    files = glob.glob(os.path.join(INPUT_DIR, '*.in'))

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        pool.map(process_file, files)

    print(f"Processed {len(files)} files in {time.time() - start:.2f} seconds")

if __name__ == "__main__":
    main()
