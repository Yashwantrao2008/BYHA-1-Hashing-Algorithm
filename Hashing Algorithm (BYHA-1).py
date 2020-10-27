import tkinter as tk
from tkinter import *

NumToAdd_1 = 9430262891917782453505428615423908959337133318060136057500156255678762671372860573332772880083351396057524931504385716027623347943200141094344753624825307762215594192604578753787978269601932849879909633393767026810172385679928208587638289863380675770580062928032570829725218880682992310460844019438899010975869797432820746602074348730633672870320922200801181198411807458432694355888212771559874430166458267627029052321106778499115081354499233635127637031095090184772635718378923169089226819374531079979019330808402708562581798182381605077758937856052611045589835048162220234108040945376599063443175705016772288759841910026312524650551419299
NumToAdd_2 = 1961881819591349203371757222104433517602558237394176632218917240990973893098241027402706479290834450916749171841834699224713374907540812244209696535963861735173893304215441350408897774988940039078213792439621630253036401295505806906721907309328326025292409709835441317591535637799839835483009809776716606845967248217752268520392257263201714532351153721064390492331306963647284459913657777360858513557232494810375242527338806928732472570184534844401646890303604718709698089986365943340416165772557142592746414268402377599171410700973461459199778232582412553223114832940294087965527875984006272537295061657531244073976369822789473463261532509
KeepNum_A = 5
KeepNum_B = 9
BlocSiz = 1
DivNextBlock = 3
AddNextBlock = 1
PWRW = 5
IFPWR = 3
LPWR = 4

MainWindow = tk.Tk()
MainWindow.geometry("700x225")
MainWindow.title("BYHA-1 (0.0.1) Hashing Algorithm")
InputBox = Entry(MainWindow, width=80)
Label(MainWindow, text='Input', bd=60).grid(row=1)
InputBox.grid(row=1, column=2)

def Hash(InputBox, NumToAdd_1, NumToAdd_2, KeepNum_A, KeepNum_B, BlocSiz, DivNextBlock, AddNextBlock, PWRW, IFPWR, LPWR, DigestLen):
	InpPass = InputBox.get()
	InpPass = [(InpPass[i:i+BlocSiz]) for i in range(0, len(InpPass), BlocSiz)] #Splits the input into blocks
	TotalBlocks = len(InpPass)
	TotalBlocks = TotalBlocks - 1
	srn = 0 #serial number
	CurrentBlock = InpPass[0] #The block that is currently begin hashed
	Block = ''.join(format(ord(i), 'b') for i in CurrentBlock) #Converts CurrentBlock to binary.

	while srn <= TotalBlocks:
		CurrentBlock = InpPass[srn]
		Block = str(Block)
		CurrentBlock = ''.join(format(ord(i), 'b') for i in CurrentBlock) #Turn the next block to binary (Used when combining the hashed and new blocks).
		CurrentBlock = int(CurrentBlock)/DivNextBlock  
		CurrentBlock = int(CurrentBlock)+AddNextBlock
		CurrentBlock = str(CurrentBlock)
		Block = CurrentBlock + Block  #Combines the hashed block and the next block to make a new block to be hashed
		Block = int(Block)**PWRW
		Blocklen = len(str(Block)) 
		SubBlocklen = 0

		if Blocklen % DigestLen==0:
			SubBlocklen = Blocklen/DigestLen #The block is divided into sub-blocks. SubBlocklen is the length of these sub-blocks
			Block = str(Block)
			Block = Block[0]
			Block = [(Block[i:i+int(SubBlocklen)]) for i in range(0, len(Block), int(SubBlocklen))]  #Splits the block into sub-blocks
			Block = Block[1] #Picks only the second sub-block. This adds in some more uncertanity
			Block = int(Block)+NumToAdd_1 #Helps add even more randomnes and helps lengthen the hash
			srn = srn + 1 
			Block = Block**IFPWR   
			SubBlocklen1 = SubBlocklen
			SubBlocklen = DigestLen
			Block = str(Block)
			Block = [(Block[i:i+SubBlocklen]) for i in range(0, len(Block), SubBlocklen)] #Splits the block
			Block = Block[int(SubBlocklen1)-KeepNum_A] #Turns one of the sub-blocks into the block
		else:
			SubBlocklen = Blocklen/DigestLen
			SubBlocklen = int(SubBlocklen)+1
			SubBlocklen = SubBlocklen*DigestLen
			Block = str(Block)
			Block = [(Block[i:i+SubBlocklen]) for i in range(0, len(Block), SubBlocklen)]
			Block = Block[0]
			srn = srn + 1
			Block = int(Block)+NumToAdd_2 #The number added is different from that of the seed if Blocklen % Divison as it helps reduce collisions.
			Block = Block**LPWR
			SubBlocklen = SubBlocklen/DigestLen
			SubBlocklen1 = SubBlocklen
			SubBlocklen = DigestLen
			SubBlocklen = int(SubBlocklen)
			Block = str(Block)
			Block = [(Block[i:i+SubBlocklen]) for i in range(0, len(Block), SubBlocklen)]
			Block = Block[int(SubBlocklen1)-KeepNum_B]
		if srn > TotalBlocks:
			global Digest
			Digest = "Digest:- "+str(Block)
			Display = Label(MainWindow, text=Digest)
			Display.place(x=40, y=100)

HashButton = Button(MainWindow, text='Hash Now', command= lambda : Hash(InputBox, NumToAdd_1, NumToAdd_2, KeepNum_A, KeepNum_B, BlocSiz, DivNextBlock, AddNextBlock, PWRW, IFPWR, LPWR, 64))
HashButton.grid(row=3)   
MainWindow.mainloop()

#Hashing algorithm by B.Yashwant Rao, Class VIII, JNV Nizamsagar.