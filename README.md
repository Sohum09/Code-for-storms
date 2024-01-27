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
9. SMAPConverter.py - Very quick script I whipped up that converts the raw 10-min SMAP reading to its equivalent 1-min version using a complicated linear regression equation.
10. JordanEqn.py - A quick script I whipped up on request from a friend, that uses the equation to derive pressure estimates from 700mb height as devised by Jordan et al. 1958.
11. ASCATUndersample.py - A quick script I whipped up. This applies the regression equation developed by Chou et al. 2013 to estimate the true representative windspeeds of a TC from the ASCAT Vmax of a particular pass.
12. ConeForecast.py - A python script where you input the coordinates and the wind forecasts of a storm, and a cone will be produced of your choice. Detailed instructions have been enclosed in the documentation so please do give it a read.
13. PlotWPACReconGraph.py - A python script where you input the data according to the format and the output is the recon data for all storms pre-1987 in the WPAC that got recon.
14. ATCFReader.py - A test python script that reads the ATCF Sector File and displays the latest updated values in the ATCF Format. I may expand on this later.
15. BestTrackReader.py - A python script where you input the ATCF id of the storm and it checks the NOAA SSD Archives for the official Best Track and returns the necessary information. Do note that these tracks may be hosted temporarily on the website.
16. BestTrackPlot.py - A python script that on inputting the ATCF id of the storm it plots the Best Track using cartopy and matplotlib.pyplot packages from the NOAA SSD Best Track Archives. Note that IDL crossover storms are not supported.
17. IBTRACS_BT_READER_NO_IDL.py - This script plots the Best Track using cartopy and matplotlib.pyplot packages from the IBTRACS dataset. This does not support IDL storms and can be used for cases where storms cross the prime meridian in the North Atlantic Ocean.
18. IBTRACS_BT_READER_IDL.py - The much awaited fix which does the same as the previous entry but now also supports IDL crossover storms.
