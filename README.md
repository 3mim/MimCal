## What is MimCal
MimCal is advance calculate forex and crypto currency market can calculate stop loss and Entry lot of size
MimCal working on windows, Linux, Macos
Mimcal become easy way to calcution of trading.

## Document
<p> if you're trader dont be doubt that you need Mimcal </p>

![alt text](https://github.com/3mim/MimCal/blob/professional/PSD%20UI/MIMcal_intro.jpg?raw=true)

## Calculation
### CRYPTO STOP LOSS
<p align="center">
   <p align="center">if you want to cal stop loss you needed 2 entry: </p>
   <p align="center">  1. Risk   </p>
   <p align="center"> 2. Leverage </p>
   <p align="center"> <img  width="30%" src="https://github.com/3mim/MimCal/blob/professional/PSD%20UI/calulate_crypto.gif?raw=true"/> </p>
   
</p>

### FOREX LOT
<p align="center">
   <p align="center">if you want to cal Entry lot size of Forex  needed 4 entry: </p>
   <p align="center">  1. Margin  </p>
   <p align="center">  1. Risk  </p>
   <p align="center">  1. Stop Loss (distance of stop loss to entry trade in pip)  </p>
   <p align="center">  1. 1Lot per $ (value of 1 pip per 1 lot) </p>
   <p align="center"> <img  width="30%" src="https://github.com/3mim/MimCal/blob/professional/PSD%20UI/calulate_forex.gif?raw=true"  /> </p>
</p>



## features
<h3 align="center" >
 Dark and Light Mode
</h3>

<br>

<p align="center">
  <img width="30%" src="https://github.com/3mim/MimCal/blob/professional/PSD%20UI/dark.gif?raw=true" />
</p>

<hr>

<h3 align="center"  >
 Two language (English and persian)  
</h3>

<br>

<p align="center" background="red">
  <img width="30%" src="https://github.com/3mim/MimCal/blob/professional/PSD%20UI/language.gif?raw=true" />
</p>
 
## MimCal for windows 
<p>  download <a href="https://github.com/3mim/MimCal/raw/professional/mimcal.exe">Mimcal.exe</a></p>

## MimCal for Linux and macOS

### Prerequisites

<p> Tkinter for GUI <p>
<pre>
 <code> pip install tkinter </code>
</pre>

<p> customtkinter for  modernize GUI <p>
<pre>
 <code> pip install customtkinter </code>
</pre>

<p> webbrowser  <p>
<pre>
 <code> pip install webbrowser </code>
</pre>

## pyinstaller

### if upx install
<pre>
 <code> pyinstaller --upx-dir "upx address on youre device" -y --clean -F  --noconfirm   --onefile  --windowed --add-data "customtkinter library address" --add-data "custom font address" -i " youre icon location"   youre_script.py </code>
</pre>



### example code
<pre>
 <code> pyinstaller --upx-dir C:\Users\MORTEZA\upx-3.96-win64 -y --clean -F  --noconfirm   --onefile  --windowed --add-data "c:/users/morteza/appdata/local/programs/python/python310/lib/site-packages/customtkinter;customtkinter/" --add-data "C:/Users/MORTEZA/Documents/pythonCode/mori/IRANMarker.ttf;." -i "./mimcal.ico"   .\mimcal.py </code>
</pre> 




## personal info
<p> email:
 <a href="morrtteeza@gmail.com">
  morrtteeza@gmail.com
 </a>
</p>
website: https://treem.ir


