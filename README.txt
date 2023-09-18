Explanation: This tool automatically translates any [NAB: Not translated] placeholders in a xml file into german by sending the english version to the google translation API and writing the changes into a output.txt file. The input file will not be modified.

replace "input.xlf" in the batch file with the name of your input file or rename your input file to this.

the batch file, the python file, as well as your input file (xlf / xml) need to be in the same folder for this to work (the output file will be created or overwritten on each attempt so make backups if needed)

make sure python is installed before running the script

make sure to run the command in the line below to install the googletranslator dependency 

pip install googletrans==4.0.0-rc1

please pay attention to the rate limit of max. 5 request per seconds and up to 500.000 free characters per month that the google translation api can handle for free each month anything beyond that costs money (~20$ / 1 million Characters)

There is no functionallity implemented as of now in this tool to make translations after reaching the free monthly limit. The google API will just return errors after hitting the limit.

All devices in the same network will probably be blocked from using the program if the api limit is reached. So a workaround might be if several people use it from home office.
