# CISA_Code_Snippet
One of my favorite projects to talk about!

The zip file contains three different files:

* main.py - the program to run (using python3 main.py)
* rawSignal
* channelNoise

To unzip the files, head to a linux/Unix based command line and run the command:
unzip CISA_Code_Snippet.zip 
* Ensure that all three files mentioned above are within the same directory

What main.py does is combine the rawSignal and channelNoise into a new file, 'receivedSignal'.
This "receivedSignal" is representative of what it is like to receive bits of information over wifi. Wifi is a very noisy medium for information distribution.
So, in this program I take a sample wifi signal and utilize a basic hamming code to sort through any corrupted bits and obtain the orignally intended message.

This code was developed using python 3.9.13.
To run the program simply run the command below:
python3 main.py

You will be prompted to use another file instead of the default file. You may ignore this option for our purposes.
Below is what the "receivedSignal" file would look like without my correction/processing.

ZhAn%hco ÒèaNw regeived h)r B.E~g. ant InR/ de/rees in dmåstbic`l Enfi.åEVioï b2o} xgbiaog Universh4ùn Langz`/u, Ghioy,()n 1y96 ajt 099¸,`2ecrecvi6ely. XE secg)rd$ Hiq P(.d*$vEwzuu in elEctbkcaL$engineerhnc gro} th'0Stcvg$n)veVwity çn Ne÷ Yo2c át(Ctwoy [1]rooiban 2017. Fso-!5y1¹(tn 380!, he wïrkeä ij indw{uRQ es(an E}bed$ed¨sysõum QoFPwcru lgkow%r.hFrkm 20p6 vk "007. He`ges(a`Poredíwu+Ral(R%SeArkieb Kn$th% Ao}putms$cmenãí g`áRtemnt qt Casnewig

åNlïn UNyvarsi|y.!He joifdd$t@å bic}lty$i~ 5hE2cnmrupeSãiEncå(@epqrtMent At0floriDa Sdad-0Uîiv%rwépy In Na$n(200w int"i3 sqrrently a VulXr~nmccor® hiw reñå`2a``inteb%sT iS máinì9 7ireí%rs1.e|wïrib>
