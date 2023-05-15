# MilesPlus Automation
## Task Overview
 - To reduce the manual work of converting the miles plus work recording report from "txt" format to "csv", this task has been formulated. The "txt" file had a format consisting of multiple delimeters and had to be arranged into a csv file as per the required format.

## Prerequisites
- On your local machine, you need Python installed and a shell terinal to run the python script for the convertion.

## Preparing your virtual machine
- [python download link](https://www.python.org/downloads/)
- [git bash download link](https://git-scm.com/download/win)

## The script
As you go inside the milesplus folder, you will see a file "app.py". That's the script conataining the code for the conversion.

## Code Overview
- Initially the required modules are imported.
- After that, source folder's and detination folder's path is set through the arguments passed by the user trough stdin in the command which will start the script.
- Conversion function, which includes the conversion of txt to csv along with splitting the values into extra columns. The function ends by applying the border around the data inside the newly constructed csv file.
- After the conversion is done, user gets informed about the files converted and where the converted files are stored (destination folder).

## How to run the script
This script is kept on a public github repo. Passing the source folder and destination folder path of local file system is neccessary in order to tell the script that where the "txt" files are kept and where to store them after the conversion. Add an extra "\" to both paths. 
```
Example:
curl -sS https://raw.githubusercontent.com/bhatanimesh02/miles_plus_automation/main/milesplus/app.py | python - --source "C:\users\source\\" --destination "C:\users\destination\\"
```
```sh
curl -sS https://raw.githubusercontent.com/bhatanimesh02/miles_plus_automation/main/milesplus/app.py | python - --source "<source-folder-path>" --destination "<destination-folder-path>"
```
