## What is MimCal
MimCal is advance calculate forex and crypto currency market can calculate stop loss and Entry lot of size. <br/>
MimCal working on windows, Linux, Macos<br/>
Mimcal become easy way to calculations of trading.

## Document
<p> if you're trader you need Mimcal </p>

![alt text](https://github.com/3mim/MimCal/blob/professional/PSD%20UI/MIMcal_intro.jpg?raw=true)

## Calculation
<p> this program include two side:</p>
### CRYPTO STOP LOSS
<p align="center">
   <p align="center">if you want to cal stop loss you needed 2 entry: </p>
   <p align="center">  1. Risk   </p>
   <p align="center"> 2. Leverage </p>
   <p align="center"> <img  width="40%" src="https://github.com/3mim/MimCal/blob/professional/PSD%20UI/calulate_crypto.gif?raw=true"/> </p>
   
</p>

### FOREX LOT
<p align="center">
   <p align="center">if you want to cal Entry lot size of Forex  needed 4 entry: </p>
   <p align="center">  1. Margin  </p>
   <p align="center">  2. Risk  </p>
   <p align="center">  3. Stop Loss (distance of stop loss to entry trade in pip)  </p>
   <p align="center">  4. 1Lot per $ (value of 1 pip per 1 lot) </p>
   <p align="center"> <img  width="40%" src="https://github.com/3mim/MimCal/blob/professional/PSD%20UI/calulate_forex.gif?raw=true"  /> </p>
</p>



## features
<h3 align="center" >
 Dark and Light Mode
</h3>

<br>

<p align="center">
  <img width="40%" src="https://github.com/3mim/MimCal/blob/professional/PSD%20UI/dark.gif?raw=true" />
</p>

<hr>

<h3 align="center"  >
 Two language (English and persian)  
</h3>

<br>

<p align="center" background="red">
  <img width="40%" src="https://github.com/3mim/MimCal/blob/professional/PSD%20UI/language.gif?raw=true" />
</p>
 
## MimCal for windows 
<p>  download <a href="https://github.com/3mim/MimCal/raw/professional/MimCal.zip">Mimcal</a></p>

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

<p> pyglet for custom fonts  <p>
<pre>
 <code> pip install pyglet </code>
</pre>

## pyinstaller
<pre>
 <code>  
   
pyinstaller --noconfirm --onefile --windowed --icon " icon location " --name " app name "  --debug "bootloader" --noupx --add-data " add address of customtkinter library " --add-data "add youre custom font" ;."  " youre script.py"

 </code>
</pre>



### example code
<pre>
 <code> pyinstaller --noconfirm --onefile --windowed --icon "C:/Users/MORTEZA/Documents/pythonCode/MimCal/test/mimcal.ico" --name "MimCal" --debug "bootloader" --noupx --add-data "C:/Users/MORTEZA/AppData/Local/Programs/Python/Python310/Lib/site-packages/customtkinter;customtkinter/" --add-data "C:/Users/MORTEZA/Documents/pythonCode/MimCal/test/fonts/IRANMarker.ttf;."  "C:/Users/MORTEZA/Documents/pythonCode/MimCal/test/mimcal.py" </code>
</pre> 
### NOTIC this code can prevent Windows Defender to detects an exe file as a virus.(to due debug is "bootloader")



## personal info
<p> email:
 <a href="morrtteeza@gmail.com">
  morrtteeza@gmail.com
 </a>
</p>
website: https://treem.ir <br>

more info aboute MimCal: https://treem.ir/mimcal <br>

https://treem.ir/calculate-lot-size-forex-with-mimcal/ <br>

https://treem.ir/calculate-stop-loss-crypto-with-mimcal/

