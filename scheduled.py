
import os
import schedule
import nbformat
import time
from nbconvert import PythonExporter
import os

# Change the working directory to the directory containing the script
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def run_ipynb(ipynb_path):

    with open(ipynb_path, 'r', encoding='utf-8') as notebook_file:
        notebook_content = notebook_file.read()
    # Convert the notebook to a Python script
    print('2: Run the ipynb notebook')
        # Read the notebook content
    # Convert the notebook to a Python script
    notebook = nbformat.reads(notebook_content, as_version=4)
    python_exporter = PythonExporter()
    (python_script, resources) = python_exporter.from_notebook_node(notebook)

    # Execute the generated Python script
    exec(python_script)
def job():
    print('1: Start executing notebook')
    # Replace 'your_notebook.ipynb' with the actual notebook file name
    notebook_path = 'my_prjoect_main.ipynb'
   
    # Run the IPython notebook
    run_ipynb(notebook_path)
    print(notebook_path)

print('Scheduler is set!')
# Schedule the job to run every day at 3:00 AM
schedule.every().day.at("07:00").do(job)
#schedule.every(1).day.do(job)
#schedule.every(1).seconds.do(job)

# Keep the script running to allow schedule to work
while True:
    print('Scheduler loop is initiated!')
    schedule.run_pending()
    print('Run pending!')
    time.sleep(59)

#caffeinate -w 36388