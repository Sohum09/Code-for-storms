# Code-for-storms
1. ACE Calculator - A simple script that produces TC duration & ACE for 6 hour intervals. I may revamp this in the future.
2. CKZ Script - Input parameters, it will output the pressure for the TC as defined by the landmark Courtney 2009 paper.
3. Dvorak DT - A C++ script that automatically calculates the DT according to Jack Beven's revision of the Dvorak Technique, circa 2010+.
4. Converter - A vital python script composed by my friend Sam, I adjusted it a bit. This script converts pre-2000 JTWC BT into HURDAT format.
Since the script uses a file as input, I have enclosed the For storms.txt file that it takes in as input in this repository.
5. RevCKZ - This script is the logical inverse of the CKZ script; This uses the direct method for now, but I have kept the Binary Search implementation at the bottom in multi-line comments for later investigation.
6. ATCF_to_HURDAT_Modern.py - A Python script composed by my friend Kathy Chan that is a logical extention of the other converter script. This converts modern ATCF BT to HURDAT format for the BT. As always, since this takes file as input, I've put in the For storms.txt text file as sample input for this.
7. MSLPConverter.py - A simple script that takes the altitude of the station, recorded pressure, and temperature to output the equivalent sea level pressure.
8. DistanceCalculator.py - Input the coordinates of any two points on earth, and the script will output the distance between them in both kilometres as well as nautical miles.
