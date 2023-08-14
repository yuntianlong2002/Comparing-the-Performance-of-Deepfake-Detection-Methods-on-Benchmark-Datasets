import os
import re
import sqlite3

# Connect to SQLite database (or create it)
conn = sqlite3.connect('benchmark_results.db')
cursor = conn.cursor()

# Create table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Results (
        Method TEXT,
        Dataset TEXT,
        ConfusionMatrix TEXT,
        Loss REAL,
        Acc REAL,
        AUC REAL,
        AP REAL,
        FrameConfusionMatrix TEXT,
        FrameAUC REAL,
        FrameACC REAL,
        Description TEXT
    )
''')
               
datasets = ['celebdf', 'dfdc', 'dftimit_hq', 'dftimit_lq', 'uadfv']


# Walk through directory and subdirectories
for root, dirs, files in os.walk('.'):
    for file in files:
        if file.endswith('.txt'):
            with open(os.path.join(root, file), 'r') as f:
                content = f.read()
                
                # Check if 'Benchmark results:' is in the file
                if 'Benchmark results:' in content:
                    # Extract text after 'Benchmark results:'
                    benchmark_text = content.split('Benchmark results:')[1]
                    
                    # Extract method and dataset
                    filename = os.path.splitext(file)[0]  # remove the .txt extension
                    for dataset in datasets:
                        if filename.startswith(dataset):
                            method = filename[len(dataset)+1:]
                            break
                    
                    
                    # Check if the file has both video-level and frame-level metrics
                    if "Confusion matrix (video-level):" in benchmark_text and "Confusion matrix (frame-level):" in benchmark_text:
                        # Extract video-level and frame-level metrics
                        confusion_matrix = re.search(r"Confusion matrix \(video-level\):\n(.*?\n.*?)\n", benchmark_text, re.DOTALL).group(1)
                        frame_confusion_matrix = re.search(r"Confusion matrix \(frame-level\):\n(.*?\n.*?)\n", benchmark_text, re.DOTALL).group(1)
                        frame_auc = float(re.search(r"Frame-level AUC: (.*?)\n", benchmark_text).group(1))
                        frame_acc = float(re.search(r"Frame-level ACC: (.*?)\n", benchmark_text).group(1))
                    elif "Confusion matrix (video-level):" in benchmark_text:
                        # Extract video-level metrics only
                        confusion_matrix = re.search(r"Confusion matrix \(video-level\):\n(.*?\n.*?)\n", benchmark_text, re.DOTALL).group(1)
                        frame_confusion_matrix = None
                        frame_auc = None
                        frame_acc = None
                    else:
                        # Extract general confusion matrix
                        confusion_matrix = re.search(r"Confusion matrix:\n(.*?\n.*?)\n", benchmark_text, re.DOTALL).group(1)
                        frame_confusion_matrix = None
                        frame_auc = None
                        frame_acc = None

                    # Extract loss, acc, auc, ap
                    loss = float(re.search(r"Loss: (.*?)\n", benchmark_text).group(1))
                    acc = float(re.search(r"Acc: (.*?)\n", benchmark_text).group(1))
                    auc = float(re.search(r"AUC: (.*?)\n", benchmark_text).group(1))
                    ap = float(re.search(r"AP: (.*?)\n", benchmark_text).group(1))

                    # Get the last two lines for the description
                    description = "\n".join(benchmark_text.split("\n")[-3:-1])
                    
                    # Insert the data into the SQLite database
                    cursor.execute('''
                        INSERT INTO Results (
                            Method, Dataset, ConfusionMatrix, Loss, Acc, AUC, AP, 
                            FrameConfusionMatrix, FrameAUC, FrameACC, Description
                        )
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    ''', (method, dataset, confusion_matrix, loss, acc, auc, ap, frame_confusion_matrix, frame_auc, frame_acc, description))

# Commit changes and close connection
conn.commit()
conn.close()