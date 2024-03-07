import nbformat
from nbformat.v4.nbbase import new_code_cell, new_markdown_cell, new_notebook
import re
import os
import shutil

def process_notebook(folder_original, folder_new, filename, remove_output=False, verbose=1):

    ''' Remove nbgrader content from notebooks and save updated version
    
    '''

    ## Setup

    # read notebook file
    input_notebook = os.path.join(folder_original, file)
    with open(input_notebook, "r") as fp:
        if verbose >= 1:
            print("\nOpening ",input_notebook)
        nb = nbformat.read(fp, as_version=4)

    # display file metadata
    if verbose >= 2:
        print(f"nbformat = {nb.nbformat}.{nb.nbformat_minor}")
        display(nb.metadata)
        
    ## Remove code elements with specific tag
    def replace_code(pattern, replacement):
        ''' Replace content in code by applying regular expression
    
        '''
    
        if verbose >= 1:
            print("Removing following expression: ", pattern)
    
        count = 0
    
        regex = re.compile(pattern, re.DOTALL)
        for cell in nb.cells:
            if cell.cell_type == "code" and regex.findall(cell.source):
                cell.source = regex.sub(replacement, cell.source)
                count += 1
                if verbose >= 2:
                    print(f" - {pattern} removed")
                
        if verbose >= 1:
            print("\t",count," cells processed")
    
    SOLUTION_CODE = "### BEGIN SOLUTION(.*?)### END SOLUTION"
    SOLUTION_TEXT = "--- BEGIN SOLUTION(.*?)--- END SOLUTION"
    HIDDEN_NOTE = "--- BEGIN HIDDEN NOTE(.*?)--- END HIDDEN NOTE"
    HIDDEN_TESTS = "### BEGIN HIDDEN TESTS(.*?)### END HIDDEN TESTS"
    replace_code(SOLUTION_CODE, "# Add your solution here")
    replace_code(HIDDEN_TESTS, "# Removed autograder test. You may delete this cell.")
    
    OLD_DATA_PATH = "\.\./data/" # recall "\." escapes the "." character in regex
    NEW_DATA_PATH = "https://raw.githubusercontent.com/ndcbe/controls/main/notebooks/data/"    
    replace_code(OLD_DATA_PATH, NEW_DATA_PATH)
    
    ## Replace elements in markdown cells
    def replace_markdown(pattern, replacement):
        ''' Replace content in markdown by applying regular expression
    
        '''
    
        if verbose >= 1:
            print("Removing following expression: ", pattern)
    
        count = 0
    
        regex = re.compile(pattern, re.DOTALL)
        for cell in nb.cells:
            if cell.cell_type == "markdown" and regex.findall(cell.source):
                cell.source = regex.sub(replacement, cell.source)
                count += 1
                if verbose >= 2:
                    print(f" - {pattern} removed")
                
        if verbose >= 1:
            print("\t",count," cells processed")
    
    # Process Home Activity Boxes
    replace_markdown('style=\"background-color: rgba\(0,255,0,0.05\) ; padding: 10px; border: 1px solid darkgreen;\"',
                     'class=\"admonition seealso\"')
    replace_markdown('<b>Home Activity</b>:', '<p class=\"title\"><b>Home Activity</b></p>\n')
    replace_markdown('<b>Optional Home Activity</b>:', '<p class=\"title\"><b>Optional Home Activity</b></p>\n')
    
    # Process Tutorial Activity Boxes
    replace_markdown('style=\"background-color: rgba\(255,0,0,0.05\) ; padding: 10px; border: 1px solid darkred;\"',
                     'class=\"admonition danger\"')
    replace_markdown('<b>Tutorial Activity</b>:', '<p class=\"title\"><b>Tutorial Activity</b></p>\n')
    
    # Process Class Activity Boxes
    replace_markdown('style=\"background-color: rgba\(0,0,255,0.05\) ; padding: 10px; border: 1px solid darkblue;\"',
                     'class=\"admonition note\"')
    replace_markdown('<b>Class Activity</b>:', '<p class=\"title\"><b>Class Activity</b></p>\n')
    
    # Process Note Boxes
    replace_markdown('style=\"background-color: rgba\(255,255,0,0.05\) ; padding: 10px; border: 1px solid black;\"',
                     'class=\"admonition tip\"')
    replace_markdown('<b>Note</b>:', '<p class=\"title\"><b>Note</b></p>\n')
    
    # Remove text solutions
    replace_markdown(SOLUTION_TEXT, "*Answer*: ")

    # Remove hidden notes
    replace_markdown(HIDDEN_NOTE, "")

    # replace links to media with urls
    # 2022-09-21: removed "!" from the beginning both of these expressions to also work on handouts (pdf) in media folder
    # 2022-09-21: the use case is the error propagation handout
    MEDIA_LINK = '\[(.*)\]\(\.\./\.\./media/(.*\..*)\)'
    IMAGE_LINK = r'[\1](https://ndcbe.github.io/controls/_images/\2)'
    
    for cell in nb.cells:
        if cell.cell_type == "markdown":
        # if True: # Process media links in Python code too, this did not work for chapter6 notebook
            media_links = re.findall(MEDIA_LINK, cell.source)
            # copy media files to _images
            for txt, media_file in media_links:
                path_to_media_file = f"./media/{media_file}"
                print(f"    found link to media file: ![{txt}](../../media/{media_file})")
                if not os.path.exists(path_to_media_file):
                    print(f"    WARNING: media file {path_to_media_file} not found.")
                else:
                    print(f"    copy media file {media_file} to _images")
                    shutil.copy2(path_to_media_file, "./_build/html/_images")
            # replace media files with urls to _images
            cell.source = re.sub(MEDIA_LINK, IMAGE_LINK, cell.source)

    ## Remove code output
    # https://gist.github.com/decabyte/0ed87372774cf5d34d7e#file-nb_remove_output-py-L24
    if remove_output:
        for cells in nb.cells:
            if cells['cell_type'] == 'code':
                cells['outputs'] = []
                cells['execution_count'] = None
            

    ## Save new notebook
    output_notebook = os.path.join(folder_new, filename)
    
    with open(output_notebook, "w") as fp:
        if verbose >= 1:
            print("Saving ", output_notebook)
        nbformat.write(nb, fp)
    

# Testing
#process_notebook("./notebooks/01", "03-Flow-control.ipynb")

"""
IMPORTANT. We assume the source files are in XX-dev and the new files go into XX.
The list below is just values for XX.
"""
"""
folders = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16","contrib"]

for fld in folders:
    
    # Loop over filenames
    full_folder_name_original = "./notebooks/" + fld + "-dev"
    full_folder_name_new = "./notebooks/" + fld
    
    print("Processing files in ", full_folder_name_original)
    
    for file in sorted(os.listdir(full_folder_name_original)):
        
        # Check if file is a notebook using ending
        if re.match("(.*?)\.ipynb$", file):
            
            # process the notebook!
            process_notebook(full_folder_name_original, full_folder_name_new, file, verbose=1)
"""
            
"""
Process assignments which are in a private repo
"""
# Loop over filenames
full_folder_name_original = "../controls-private/assignments/"
full_folder_name_new = "./assignments/" # might need to move to /notebooks/assignments to get data references to work

for file in sorted(os.listdir(full_folder_name_original)):
    
    # Check if file is a notebook using ending
    if re.match("(.*?)\.ipynb$", file):
        
        # process the notebook!
        process_notebook(full_folder_name_original, full_folder_name_new, file, remove_output=True, verbose=1)