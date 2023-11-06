from tkinter import *
import tkinter.font as tkFont
from tkinter import filedialog
import ngram_score
from PIL import Image
from PIL import ImageTk

class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        #setting up
        self.geometry("1060x600+10+10")
        self.resizable(False, False)
        self.titlefont = tkFont.Font(family="Arial", size=30)
        self.buttonfont = tkFont.Font(family="Consolas", size=20)
        self.paragraphfont = tkFont.Font(family="Arial",size=15)
        self.buttoncolour = "#a3ceff"
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)

        self.introFrame = Frame(self)
        self.introFrame.config(bg="#ffffff")
        #adding labels to the page
        lab1 = Label(self.introFrame, text="Cryptography", bg= "#248aff" , font=self.titlefont)
        lab1.grid(row=0, column=0, columnspan=2, sticky="NSEW")
        lab2 = Label(self.introFrame, anchor="w", justify="left", text="Welcome\nRead the introduction which explains what cryptography is about and why it is important. Then click on one of the types\nof encryption down the side.\nWhen you have finished reading and learning about each type of encryption have a go at the challenge using the\nbottom right button.\n ", bg="#ffffff", font=self.paragraphfont)
        lab2.grid(row=1, column=0, columnspan=2, sticky="EW")
        #adding buttons to the page
        b1 = Button(self.introFrame, text=" Caesar Shift ", bg=self.buttoncolour, font=self.buttonfont, command=self.caesarshiftSwitch) #add command to the end (command=)
        b1.grid(row=2, column=1, sticky=W)
        b2 = Button(self.introFrame, text="  Rail Fence  ", bg=self.buttoncolour, font=self.buttonfont, command=self.railfenceSwitch) #add command to the end (command=)
        b2.grid(row=3, column=1, sticky=W)
        b3 = Button(self.introFrame, text=" Substitution ", bg=self.buttoncolour, font=self.buttonfont, command=self.substitutionSwitch) #add command to the end (command=)
        b3.grid(row=4, column=1, sticky=W)
        b4 = Button(self.introFrame, text="Steganography ", bg=self.buttoncolour, font=self.buttonfont, command=self.steganographySwitch) #add command to the end (command=)
        b4.grid(row=5, column=1, sticky=W)
        #adding textbox to the page
        Intro = "\nCryptography is a method of protecting information and communication by using codes that\ncan only be understood by the people that are intended to read and process the information.\nThis method is used to ensure the confidentiality of a message. There are many types of\ncryptography including Caesar Shift, Vigenere Cipher, Enigma, etc.\n\nThere are key objectives that all ciphers have to follow which ensure that the information is\nconfidential, has integrity (has not been altered between the sender and receiver) and is\nauthentic (the sender and receiver can confirm each other's identities). Cryptography is vital\nto be able to prevent people from reading information that was not meant for them. The\ninformation is likely confidential.\n\nThe use of ciphers played a huge role during World War II during which the Germans' use the enigma to send messages between themselves. The ciphertext was intercepted by the British and decoded by the codebreakers at Bletchley Park. The codebreakers at Bletchley were\nvital to the war and helped to shorten the war by about 3 years."
        textbox = Text(self.introFrame, height=17, width=75, font=self.paragraphfont, bg="#ffffff", borderwidth=0)
        textbox.grid(row=2, column=0, rowspan=4)
        textbox.insert("end", Intro)
        textbox.config(state="disabled")
        self.introFrame.grid(row=0, column=0, sticky="NSEW") 


        self.caesarshiftFrame = Frame(self)
        lab1 = Label(self.caesarshiftFrame, text="Cryptography: Caesar Shift", bg= "#248aff" , font=self.titlefont)
        lab1.grid(row=0, column=0, columnspan=3, sticky="NSEW")
        #adding a textbox
        CaesarShift = "The Caesar Shift is named after Julius Caesar, the Roman Emperor, who used it when he was communicating with his\nmilitary forces.\n\nCaesar shift works by moving the alphabet by however many characters are selected. It moves all the letters by this\nmany, creating a ciphertext of what seems like random characters. This could turn the phrase 'HELLO WORLD' into\n'LIPPS ASVPH' by shifting each character 4 characters so the letter 'a' would become an 'e'.\n\nWhy not have a go below. Add some text to the box on the left and click to the arrow buttons to change the shift. Then\nclick encode to encrypt the text. To decode it add your encrypted text to the right box and click the decode button to\ndecrypt it, you do not need to add a shift for this to work."
        textbox = Text(self.caesarshiftFrame, height=11,font=self.paragraphfont, bg="#ffffff", borderwidth=1)
        textbox.grid(row=1, column=0, columnspan=3, sticky="NSWE")
        textbox.insert("end", CaesarShift)
        textbox.config(state="disabled")
        #adding a back arrow to homepage
        self.backArrowCeasar = Canvas(self.caesarshiftFrame,width=40,height=40, bg="red")
        self.backArrowCeasar.grid(row=0, column=0, sticky="W")
        self.Arrow = PhotoImage(file = "BackButton.png")
        self.backArrowCeasar.create_image(0,0,image=self.Arrow, anchor=NW)
        self.backArrowCeasar.bind("<Button-1>",self.backClicked)
        #adding interactive section
        self.caesarshiftInteractive = Canvas(self.caesarshiftFrame, height=120)
        self.caesarshiftInteractive.grid(row=2, column=0, columnspan=3, sticky = "EW")
        self.caesarinputtextbox = Text(self.caesarshiftFrame, width=40,height=5, font=self.paragraphfont, bg="#ffffff", borderwidth=1)
        self.caesarinputtextbox.grid(row=3, column=0)
        buttonCommit=Button(self.caesarshiftFrame, text="Commit", command=self.CaesarEncode)
        buttonCommit.grid(row=3, column=1)
        buttonDecode=Button(self.caesarshiftFrame, text="Decode", command=self.caesarDecode)
        buttonDecode.grid(row=4, column=1)
        self.caesaroutputtextbox = Text(self.caesarshiftFrame, width=40, height=5,font=self.paragraphfont, bg="#ffffff", borderwidth=1)
        self.caesaroutputtextbox.grid(row=3, column=2)
        self.caesarshiftFrame.columnconfigure(1,weight=1)


        self.railfenceFrame = Frame(self)
        self.railfenceFrame.config(bg="#ffffff")
        #adding a textbox
        lab1 = Label(self.railfenceFrame, text="Cryptography: Rail Fence", bg= "#248aff" , font=self.titlefont)
        lab1.grid(row=0, column=0, columnspan=3, sticky="NSEW")
        RailFence="Rail fence cipher is an easy cipher that works by transposing the letters of the into an order that can be encrypted\nquickly, and can be difficult to decrypt without the key.\nIt works by writing the message in a rail fence grid such as the one in the interactive activity. You select the number of\nrails you want, (this one contains 3), then you input your phrase which it will then put into the rail fence. It will then output\nthe phrase in cipher text. The phrase 'HELLOWORLD' would be outputted like this 'HLERDLOLWO' when the rail fence\nhas 5 rails.\n\nEnter the text you would like to encrypt to the large box on the left, then put the number of rails you would like to use in\nthe smaller box below. Once you have done this press the encode button and your rails will appear below and then\nencrypted text will appear in the box to the right."
        textbox = Text(self.railfenceFrame, height=11,width=96, font=self.paragraphfont, bg="#ffffff", borderwidth=0)
        textbox.grid(row=2, column=0, columnspan=3)
        textbox.insert("end", RailFence)
        textbox.config(state="disabled")
        #adding a back arrow to homepage
        self.backArrowRailfence = Canvas(self.railfenceFrame,width=40,height=40, bg="red")
        self.backArrowRailfence.grid(row=0, column=0, sticky="W")
        self.backArrowRailfence.create_image(0,0,image=self.Arrow, anchor=NW)
        self.backArrowRailfence.bind("<Button-1>",self.backClicked)
        #adding interactive section
        self.railfenceinputtextbox = Text(self.railfenceFrame, width=40,height=5, font=self.paragraphfont, bg="#ffffff", borderwidth=1)
        self.railfenceinputtextbox.grid(row=3, column=0)
        buttonCommit=Button(self.railfenceFrame, text="Commit", command=self.solveRailFence)
        buttonCommit.grid(row=3, column=1)
        self.railfenceoutputtextbox = Text(self.railfenceFrame, width=40, height=5,font=self.paragraphfont, bg="#ffffff", borderwidth=1)
        self.railfenceoutputtextbox.grid(row=3, column=2)
        self.railfenceFrame.columnconfigure(1,weight=1)
        self.railfenceNoRailsBox = Text(self.railfenceFrame, width=10, height=1, font=self.paragraphfont, bg="#ffffff", borderwidth=1)
        self.railfenceNoRailsBox.grid(row=4, column=0)
        self.railfenceInteractive = Canvas(self.railfenceFrame, height=200)
        self.railfenceInteractive.grid(row=6, column=0, columnspan=3, sticky = "EW")


        self.substitutionFrame = Frame(self)
        self.substitutionFrame.config(bg="#ffffff")
        #adding a textbox
        lab1 = Label(self.substitutionFrame, text="Cryptography: Substitution", bg= "#248aff" , font=self.titlefont)
        lab1.grid(row=0, column=0, columnspan=3, sticky="NSEW")
        Substitution = "This works by replacing the letters in a piece of text with other characters. A well known example of this is the Caesar\nshift. Another example of this shift would be a homophonic cipher which works by replacing each letter with a substitute. In this case we are using a random jumble of letters.\n\nThis cipher works by replacing all of the letters in the plaintext with letters that are associated in a table(Like the one in\nthe interactive task below) Making a code made of random letters that have no order to them.\n\nHave a go at entering some text below and have a look at the encoded text next to it to see if you can work out how it is\ndoing it."
        textbox = Text(self.substitutionFrame,height=10, width=96, font=self.paragraphfont, bg="#ffffff", borderwidth=0)
        textbox.grid(row=1, column=0, columnspan=3)
        textbox.insert("end", Substitution)
        textbox.config(state="disabled")
        #adding a back arrow to homepage
        self.backArrowSubstitution = Canvas(self.substitutionFrame,width=40,height=40, bg="red")
        self.backArrowSubstitution.grid(row=0, column=0, sticky="W")
        self.backArrowSubstitution.create_image(0,0,image=self.Arrow, anchor=NW)
        self.backArrowSubstitution.bind("<Button-1>",self.backClicked)
        #adding interactive section
        self.substitutionInteractive = Canvas(self.substitutionFrame, height=150)
        self.substitutionInteractive.grid(row=2, column=0, columnspan=3, sticky = "EW")
        self.substitutioninputtextbox = Text(self.substitutionFrame, width=40,height=5, font=self.paragraphfont, bg="#ffffff", borderwidth=1)
        self.substitutioninputtextbox.grid(row=3, column=0)
        buttonCommit=Button(self.substitutionFrame, text="Commit", command=self.retrieve_inputsubstitution)
        buttonCommit.grid(row=3, column=1)
        self.substitutionoutputtextbox = Text(self.substitutionFrame, width=40, height=5,font=self.paragraphfont, bg="#ffffff", borderwidth=1)
        self.substitutionoutputtextbox.grid(row=3, column=2)
        self.substitutionFrame.columnconfigure(1,weight=1)


        self.steganographyFrame = Frame(self)
        self.steganographyFrame.config(bg="#ffffff")
        #adding a textbox
        lab1 = Label(self.steganographyFrame, text="Cryptography: Steganography", bg= "#248aff" , font=self.titlefont)
        lab1.grid(row=0, column=0, columnspan=3, sticky="NSEW")
        Steganography = "Steganography is hiding messages in something not so secret. This can be anything from a piece of text to a picture.\nThe use of this is to be deceiving in order to deter unwanted parties from reading the information. Steganography is not\na type of cryptography as it does not involve scrambling data or using a key. It instead hides data within something else.\nTo do a basic grid steganography you would, using the number of characters in your chosen phrase, make a grille which\nis a sheet with holes in it. This has the same number of holes as it does characters. A grid of letters is then created,\nlining up the spaces in the grille with the characters in the text. The rest of the characters would be made up of random\ncharacters to fill the spaces, making it difficult for someone without the grille to decode it.\n\nTo have a go write some text into the input box then upload an image using the button, choose the photo you would like\nand press encrypt. Similarly if you want to find the text hidden in an image upload the image and press decode.\nNOTE: this only works if the image was encoded using this software."
        textbox = Text(self.steganographyFrame, height=12, width=96, font=self.paragraphfont, bg="#ffffff", borderwidth=0)
        textbox.grid(row=2, column=0, columnspan=3)
        textbox.insert("end", Steganography)
        textbox.config(state="disabled")
        #adding a back arrow to homepage
        self.backArrowSteganography = Canvas(self.steganographyFrame,width=40,height=40, bg="red")
        self.backArrowSteganography.grid(row=0, column=0, sticky="W")
        self.backArrowSteganography.create_image(0,0,image=self.Arrow, anchor=NW)
        self.backArrowSteganography.bind("<Button-1>",self.backClicked)
        #adding interactive section
        self.steganographyinputtextbox = Text(self.steganographyFrame, width=50,height=5, font=self.paragraphfont, bg="#ffffff", borderwidth=1)
        self.steganographyinputtextbox.grid(row=3, column=0, sticky="W")
        buttonEncode=Button(self.steganographyFrame, text="Encode", command = self.EncryptSteganography)
        buttonEncode.grid(row=4, column=0)
        buttonDecode=Button(self.steganographyFrame, text="Decode", command = self.DecryptSteganography)
        buttonDecode.grid(row=5, column=0)
        self.steganographyFrame.columnconfigure(1,weight=1)
        self.mainloop()


    def CaesarShiftGrid(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.shiftedletters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.caesarshiftInteractive.delete(ALL)
        self.leftpos = 100
        self.boxWidth = 30
        #draw top row of letters
        for i in range(0,26):
            self.caesarshiftInteractive.create_text(self.leftpos+i*self.boxWidth+self.boxWidth//2,35,text=self.letters[i], font=self.buttonfont)
        #draw box gridlines
        for xpos in range(0,self.boxWidth*27,self.boxWidth):
            self.caesarshiftInteractive.create_line(self.leftpos+xpos,50,self.leftpos+xpos,100)
        self.caesarshiftInteractive.create_line(self.leftpos,50, self.leftpos+self.boxWidth*26, 50)
        self.caesarshiftInteractive.create_line(self.leftpos,100, self.leftpos+self.boxWidth*26, 100)       
        #draw arrows
        self.larrow = PhotoImage(file = "alphabetButtonBack.png")
        lefty = self.caesarshiftInteractive.create_image(self.leftpos,75,image=self.larrow, anchor="e")
        self.rarrow = PhotoImage(file = "alphabetButtonForward.png")
        righty = self.caesarshiftInteractive.create_image(self.leftpos+self.boxWidth*26+1,75,image=self.rarrow,anchor="w")
        self.caesarshiftInteractive.tag_bind(lefty,"<Button-1>",self.Caesarleftshiftclicked)
        self.caesarshiftInteractive.tag_bind(righty,"<Button-1>",self.Caesarrightshiftclicked)
        self.lettersDrawn = []
        self.drawCaesarLetters()
        self.shifted = 0


    def CaesarEncode(self):
        #read input
        inputValue = self.caesarinputtextbox.get(1.0, END)
        inputValue = inputValue.lower()
        #encode
        plaintext = list(inputValue.strip())
        caesarshifttext = ""
        for x in plaintext:
            if x != " " and x != "0" and x != "1"and x != "2"and x != "3"and x != "4"and x != "5"and x != "6"and x != "7"and x != "8"and x != "9":
                x = (ord(x))-97
                x = (x + self.shifted) % 26
                newx = chr(x+97)
                caesarshifttext += newx
        #stick in right box
        self.caesaroutputtextbox.delete(1.0, END)
        self.caesaroutputtextbox.insert(1.0,caesarshifttext)

    
    def caesarDecode(self):
        CodetoDecode = self.caesaroutputtextbox.get(1.0, END).strip()
        CodedtoDecode = CodetoDecode.lower()
        calculator = ngram_score.ngram_score("english_quadgrams.txt")
        compareNum = -10000000
        for y in range(0,26):
            decoded = ""
            for char in CodetoDecode:
                if char != " " and char != "0" and char != "1"and char != "2"and char != "3"and char != "4"and char != "5"and char != "6"and char != "7"and char != "8"and char != "9":
                    cval = (ord(char))-97
                    cval = (cval-y) % 26
                    newletter = chr(cval+97)
                    decoded += newletter
            score = calculator.score(decoded.upper())
            if score > compareNum:
                compareNum = score
                NoShifts = y
        plainText = ""
        for letter in CodetoDecode.lower():
            if letter != " " and letter != "0" and letter != "1"and letter != "2"and letter != "3"and letter != "4"and letter != "5"and letter != "6"and letter != "7"and letter!= "8"and letter != "9":
                value = (ord(letter))-97
                value = (value-NoShifts)%26
                finalLetter = chr(value+97)
                plainText += finalLetter 
        #stick in left box
        self.caesarinputtextbox.delete(1.0, END)
        self.caesarinputtextbox.insert(1.0,plainText)


    def Caesarleftshiftclicked(self, e):
        self.shiftedletters = self.shiftedletters[1:] + self.shiftedletters[0]
        self.drawCaesarLetters()
        self.shifted += 1 % 26

        
    def Caesarrightshiftclicked(self, e):
        self.shiftedletters =  self.shiftedletters[-1] + self.shiftedletters[:-1]
        self.drawCaesarLetters()
        self.shifted -= 1 % 26


    def drawCaesarLetters(self):
        for letter in self.lettersDrawn:
            self.caesarshiftInteractive.delete(letter)
        self.lettersDrawn = []
        for i in range(0,26):
            self.lettersDrawn.append(self.caesarshiftInteractive.create_text(self.leftpos+i*self.boxWidth+self.boxWidth//2,75,text=self.shiftedletters[i], font=self.buttonfont))
    

    def encryptRailfence(self):
        self.leftpos = 100
        self.boxWidth = 25
        self.boxHeight = 25
        row = 0
        direction = 1
        encoded = ""
        self.Correct = True
        AddValue = "\nPlease insert a number between 2 and 4"
        AddText = "Please add text into the input box"
        self.railfenceoutputtextbox.delete(1.0,END)
        NumRails = self.railfenceNoRailsBox.get(1.0, END).strip()
        message = self.railfenceinputtextbox.get(1.0, END).strip().lower()
        if (NumRails != "2" and NumRails != "3" and NumRails != "4"):
            self.railfenceoutputtextbox.insert(1.0,AddValue)
            self.Correct = False
        if message == "":
            self.railfenceoutputtextbox.insert(1.0,AddText)
            self.Correct = False
        if self.Correct:
            self.railfenceoutputtextbox.delete(1.0,END)
            NoRails = int(NumRails)
            railstrings = ["" for x in range(NoRails)]
            for i  in range(len(message)):
                for railnum in range(NoRails):
                    if railnum == row:
                        railstrings[railnum] += message[i]
                    else:
                        railstrings[railnum] += " "
                if row == NoRails-1:
                    direction = -1
                if row == 0:
                    direction = 1
                row = row + direction
            for rail in railstrings:
                print(rail)
            print(railstrings)
            for column in range(0,len(message)):
                for railnum in range(0,len(railstrings)):
                    self.railfenceInteractive.create_text(self.leftpos+column*self.boxWidth+self.boxWidth//2,35+railnum*25,text=railstrings[railnum][column], font=self.buttonfont)
            for a in range (0, NoRails):
                for b in range (len(message)):
                    if railstrings[a][b] != " ":
                        encoded += railstrings[a][b]
            self.railfenceoutputtextbox.delete(1.0, END)
            self.railfenceoutputtextbox.insert(1.0,encoded)


    def solveRailFence(self):
        self.railfenceInteractive.delete('all')
        self.encryptRailfence()
        if self.Correct:
            self.railfenceGrid()

    
    def railfenceGrid(self):
        self.leftpos = 100
        self.boxWidth = 25
        self.boxHeight = 25
        Xwidth = len(self.railfenceinputtextbox.get(1.0, END).strip())
        NoRails = int(self.railfenceNoRailsBox.get(1.0, END).strip())
        #draw box gridlines
        for xpos in range(0,self.boxWidth*(Xwidth+1),self.boxWidth):
            self.railfenceInteractive.create_line(self.leftpos+xpos,25,self.leftpos+xpos,25+25*(NoRails))
        for ypos in range(0,self.boxHeight*(NoRails+1),self.boxHeight):
            self.railfenceInteractive.create_line(self.leftpos,self.boxHeight+ypos, self.leftpos+self.boxWidth*(Xwidth), self.boxHeight+ypos)


    def substitutionGrid(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.encryptionletters = "ZGWQARYEVHMSCXKTBPIULDNFJO"
        self.leftpos = 100
        self.boxWidth = 30
        #draw top row of letters
        for i in range(0,26):
            self.substitutionInteractive.create_text(self.leftpos+i*self.boxWidth+self.boxWidth//2,35,text=self.letters[i], font=self.buttonfont)
        #drow bottom row of letters
        for i in range (0,26):
            self.substitutionInteractive.create_text(self.leftpos+i*self.boxWidth+self.boxWidth//2,75,text=self.encryptionletters[i], font=self.buttonfont)
        #draw box gridlines
        for xpos in range(0,self.boxWidth*27,self.boxWidth):
            self.substitutionInteractive.create_line(self.leftpos+xpos,50,self.leftpos+xpos,100) 
        self.substitutionInteractive.create_line(self.leftpos,50, self.leftpos+self.boxWidth*26, 50)
        self.substitutionInteractive.create_line(self.leftpos,100, self.leftpos+self.boxWidth*26, 100)    


    def retrieve_inputsubstitution(self):
        #read input
        inputValue = self.substitutioninputtextbox.get(1.0, END)
        inputValue = inputValue.lower()
        #encode
        plaintext = list(inputValue.strip())
        substitutiontext = ""
        for y in plaintext:
            if y != " " and y != "0" and y != "1"and y != "2"and y != "3"and y != "4"and y != "5"and y != "6"and y != "7"and y != "8"and y != "9":
                y = (ord(y))-97
                newy = self.encryptionletters[y]
                substitutiontext += newy
        #stick in right box
        self.substitutionoutputtextbox.delete(1.0, END)
        self.substitutionoutputtextbox.insert(1.0,substitutiontext)


    def SteganographySettings(self):
        canvaswidth = 250
        canvasheight = 250
        self.steganographyInteractive = Canvas(self.steganographyFrame, height=canvasheight, width = canvaswidth)
        self.steganographyInteractive.grid(row=3, column=1, rowspan=6)
        UploadImage = Button(self.steganographyFrame, text="Upload Image",command = self.loadpic)
        UploadImage.grid(row=6, column=0)
        return self.steganographyInteractive, UploadImage

    
    def loadpic(self):
        filename = filedialog.askopenfilename(initialdir = "/",
                                        title = "Select a File",
                                        filetypes = (("PNGs",
                                                        "*.png*"),
                                                    ("all files",
                                                        "*.*")))
        self.bigImg = Image.open(filename)
        originalwidth, originalheight = self.bigImg.size
        if originalwidth >= originalheight:
            newWidth=250
            newHeight = int((originalheight/originalwidth) * newWidth)
        else:
            newHeight=250
            newWidth = int((originalwidth/originalheight) * newHeight)
        self.smallVersion = self.bigImg.resize((newWidth,newHeight), Image.ANTIALIAS)
        self.smallVersion = ImageTk.PhotoImage(self.smallVersion)
        self.steganographyInteractive.create_image(0, 0, anchor="nw", image=self.smallVersion)
        return filename
        
        
    def EncryptSteganography(self):
        #read input
        Input = self.steganographyinputtextbox.get(1.0, END)
        Input = Input.lower().strip()
        plaintext = list(Input)
        textlength = len(Input)
        pixelmap = self.bigImg.load()
        #self.steganographyinputtextbox.insert(1.0,Input)
        self.keypoints = ((92,97),(125,165),(145,194),(192,135),(50,111),(83,114),(161,85),(152,133),
                (34,33),(22,163),(148,84),(177,130),(137,158),(127,166),(144,46),(27,172),(191,162),
                (122,35),(75,36),(77,107),(74,138))
        if Input == "":
            AddText = "Please add some text into this box"
            self.steganographyinputtextbox.delete(1.0,END)
            self.steganographyinputtextbox.insert(1.0,AddText)
        else:
            for letternum in range (0, textlength):
                if plaintext[letternum] != " " and plaintext[letternum] != "0" and plaintext[letternum] != "1"and plaintext[letternum] != "2"and plaintext[letternum] != "3"and plaintext[letternum] != "4"and plaintext[letternum] != "5"and plaintext[letternum] != "6"and plaintext[letternum] != "7"and plaintext[letternum] != "8"and plaintext[letternum] != "9":
                    thispixelx = self.keypoints[letternum][0]
                    thispixely = self.keypoints[letternum][1]
                    rgbcolours = pixelmap[thispixelx,thispixely] # get colours of this pixel
                    cval = ((ord(plaintext[letternum]))-97)
                    rgbcoloursnextpixel = pixelmap[thispixelx+1,thispixely] # get colours of the pixel to the right
                    #check red value of this pixel
                    #if its greater than 128, set next pixel red to this pixel red - cval
                    if int(rgbcolours[0])>=128:
                        pixelmap[thispixelx+1,thispixely] = (int(rgbcolours[0]) - cval, rgbcoloursnextpixel[1], rgbcoloursnextpixel[2])
                    #if its less than 128 set next pixel red to this pixel red +cval
                    if int(rgbcolours[0])<128:
                        pixelmap[thispixelx+1,thispixely] = (int(rgbcolours[0]) + cval, rgbcoloursnextpixel[1], rgbcoloursnextpixel[2])
            self.bigImg.save("SteganographyEncodedImage.png")
            encrypted = "Done, it has been saved to the folder where this program is"
            self.steganographyinputtextbox.delete(1.0,END)
            self.steganographyinputtextbox.insert(1.0,encrypted)


    def DecryptSteganography (self):
        pixelmap = self.bigImg.load()
        self.keypoints = ((92,97),(125,165),(145,194),(192,135),(50,111),(83,114),(161,85),(152,133),
                (34,33),(22,163),(148,84),(177,130),(137,158),(127,166),(144,46),(27,172),(191,162),
                (122,35),(75,36),(77,107),(74,138))
        lettersFound = ""
        for kp in self.keypoints:
            #look at pixel and get r val
            #look at pixel next to and get r val
            #find diff
            #convert to letter
            #add to lettersFound
            thisPixel  = pixelmap[kp[0], kp[1]]
            nextPixel  = pixelmap[kp[0]+1, kp[1]]
            difference = abs(thisPixel[0] - nextPixel[0])
            finalLetter = chr(difference+97)
            lettersFound += finalLetter 
        self.steganographyinputtextbox.delete(1.0,END)
        self.steganographyinputtextbox.insert(1.0,lettersFound)



    def backClicked(self,e):
        # removes other frames from the grid, but adds homepage
        print("Clicked Back")
        self.caesarshiftFrame.grid_forget()
        self.railfenceFrame.grid_forget()
        self.steganographyFrame.grid_forget()
        self.substitutionFrame.grid_forget()
        self.introFrame.grid(row=0, column=0, sticky="NSEW") 


    def intropageSwitch(self):
        # removes other frames from the grid, but adds homepage
        #default when opening software
        self.caesarshiftFrame.grid_forget()
        self.railfenceFrame.grid_forget()
        self.steganographyFrame.grid_forget()
        self.substitutionFrame.grid_forget()
        self.introFrame.grid(row=0, column=0, sticky="NSEW") 


    def caesarshiftSwitch(self):
        # removes other frames from the grid, but adds Caesar Shift Page
        print("Clicked CaesarShift")
        self.introFrame.grid_forget()
        self.railfenceFrame.grid_forget()
        self.steganographyFrame.grid_forget()
        self.substitutionFrame.grid_forget()
        self.caesarshiftFrame.grid(row=0, column=0, sticky="NSEW")
        self.CaesarShiftGrid()


    def railfenceSwitch(self):
        # removes other frames from the grid, but adds Rail Fence Page
        print("Clicked RailFence")
        self.introFrame.grid_forget()
        self.caesarshiftFrame.grid_forget()
        self.steganographyFrame.grid_forget()
        self.substitutionFrame.grid_forget()
        self.railfenceFrame.grid(row=0, column=0, sticky="NSEW")


    def steganographySwitch(self):
        # removes other frames from the grid, but adds Steganography Page
        print("Clicked Steganography")
        self.introFrame.grid_forget()
        self.caesarshiftFrame.grid_forget()
        self.railfenceFrame.grid_forget()
        self.substitutionFrame.grid_forget()
        self.steganographyFrame.grid(row=0, column=0, sticky="NSEW")
        self.SteganographySettings()


    def substitutionSwitch(self):
        # removes other frames from the grid, but adds Substitution Page
        print("Clicked Substitution")
        self.introFrame.grid_forget()
        self.caesarshiftFrame.grid_forget()
        self.railfenceFrame.grid_forget()
        self.substitutionFrame.grid(row=0, column=0, sticky="NSEW")
        self.substitutionGrid()

if __name__ == "__main__":
    app = App()
