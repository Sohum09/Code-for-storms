#Quick script to calculate 1-min winds from the raw SMAP reading:
#Reference link: https://cdn.discordapp.com/attachments/767902538950901760/956337409598062622/unknown.png

#Raw SMAP data as input:
raw_SMAP = float(input("Enter the raw 10-min SMAP reading (in kt): "))

#Linear regression equation to process the above:
processed_SMAP = (362.644732816453 * raw_SMAP + 2913.62505913216) / 380.88384339523

#Display output:
processed_SMAP = "{:.2f}".format(processed_SMAP)
print("Converted 1-min winds: ", processed_SMAP, "kt")
