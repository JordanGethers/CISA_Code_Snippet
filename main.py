import statistics
import os

def createParityBits(x, codeWordList):
    size = [0,0,0,0,0,0,0]

    c0 = x[0]
    c1 = x[1]
    c2 = x[2]
    c3 = x[3]

    c4 = c0 ^ c1 ^ c2
    c5 = c1 ^ c2 ^ c3
    c6 = c0 ^ c1 ^ c3

    size[0] = c0
    size[1] = c1
    size[2] = c2
    size[3] = c3
    size[4] = c4
    size[5] = c5
    size[6] = c6

    codeWordList.append(size)


def dataToCodewords(data, codes):
    relate = dict()
    ret = 0
    for word in codes:
        bitsMatch = 0
        for n in range(0, len(data)):
            if data[n] == word[n]:
                bitsMatch += 1
            if n == len(data) - 1:
                relate[str(word)] = bitsMatch

    nMax = 0
    for item in relate:
        if relate[item] > nMax:
            nMax = relate[item]
            ret = item
        if relate[item] == 6:
            #problem in code-word decision is likely in this if-statement
            ret = item
        if relate[item] == 7:
            ret = item
            return str(ret)

    return str(ret)

def createSignal():
    file_path = os.path.abspath("rawSignal")
    sec_file_path = os.path.abspath("channelNoise")

    file = open(file_path, "r")
    sec_file = open(sec_file_path, "r")

    signal = list()
    signalReads = file.readlines()
    noiseReads = sec_file.readlines()

    # print(signalReads)
    # print(noiseReads)
    f = open(r"signalReceived", "w")
    for i in range(0, len(signalReads)):
        sigSum = float(signalReads[i]) + float(noiseReads[i])
        if i == len(signalReads) - 1:
            f.write(str(sigSum))
        else:
            f.write(str(sigSum) + '\n')

    f.close()
    file.close()
    sec_file.close()

a = [0, 0, 0, 0]
b = [0, 0, 0, 1]
c = [0, 0, 1, 0]
d = [0, 0, 1, 1]
e = [0, 1, 0, 0]
f = [0, 1, 0, 1]
g = [0, 1, 1, 0]
h = [0, 1, 1, 1]
i = [1, 0, 0, 0]
j = [1, 0, 0, 1]
k = [1, 0, 1, 0]
l = [1, 0, 1, 1]
m = [1, 1, 0, 0]
n = [1, 1, 0, 1]
o = [1, 1, 1, 0]
p = [1, 1, 1, 1]

Collection = [
    a, b, c, d, e, f, g, h, i, j,
    k, l, m, n, o, p
]

CodeWords = list()
if __name__ == '__main__':
    if os.path.isfile("signalReceived") == False:
        createSignal()
        

    for letter in Collection:
        createParityBits(letter, CodeWords)

    # print(CodeWords)
    noise = list()  # list that holds noise for threshold calculation
    rawMessage = list()  # String that still has extra bits
    noiseCount = 0  # noise mean variable
    frame = 0  # marker for the proper line area of a symbol

    path = os.getcwd() + "/"
    print("Welcome to the signal processing program! ")
    changeFile = (input(f"Would you like to change the current default file ? (Y)es or (N)o? -> "))

    if changeFile != 'Y' and changeFile != 'y':
        file = open(os.path.abspath("signalReceived"))
        print("Opening -> ", file)
    elif changeFile == 'Y' or changeFile == 'y':
        fileUser = input(f"Provide name of file to use -> {path}")
        fileName = path + fileUser
        file = open(fileName)
        print(f"Opening -> {fileName}")

    for line in file:  # this loop for finding mean and std dev of the noise
        if noiseCount < 1000:
            noise.append(float(line))
            noiseCount += 1

    print("Mean of the noise is % s " % (statistics.mean(noise)))
    print("Standard Deviation of the noise is % s " % (statistics.stdev(noise)))
    pulseThreshold = statistics.mean(noise) * 8 + statistics.stdev(noise) * 16
    print(f"Pulse Threshold is -> {pulseThreshold}")
    lineCount = -1
    file.seek(0)  # reset file pointer
    for X in file:
        lineCount += 1
        if float(X) > pulseThreshold:
            print(f"Pulse Threshold hit at line {lineCount}, 'pulse' was -> {X}")
            # frame = lineCount
            frame = lineCount - 2
            break

    file.seek(0)  # reset file pointer
    currentLine = -1
    print(f"Starting Frame is -> {frame}\n")
    zero = False
    one = False
    for sample in file:
        currentLine += 1
        if frame <= currentLine <= frame + 100:
            if float(sample) > pulseThreshold and currentLine < frame + 30:
                zero = True
            else:
                if float(sample) > pulseThreshold and zero is False:
                    one = True
        if currentLine == frame + 100:
            if zero:
                #  print("Zero")
                rawMessage.append(0)
                zero = False
            if one:
                # print("One")
                rawMessage.append(1)
                one = False
            frame += 100

    noPadMessage = rawMessage
    tmpList = list()
    cleanList = list()
    for p in range(0, 8):
        noPadMessage.pop(0)
    for x in range(0, len(noPadMessage), 7):
        tmpList.extend(dataToCodewords(noPadMessage[x: x + 7:], CodeWords))
        # tmpList.extend(str(noPadMessage[x: x + 7:])) #signalReads purposes

    #print(f"Raw Message - without padding, with Hamming -> \t\t{noPadMessage}")

    for outer in tmpList:  
        for inner in outer:
            if inner == '0' or inner == '1':
                cleanList.append(int(inner))

    #print(f"data after cleanup, with Hamming -> \t\t\t\t{cleanList}")

    front4 = list()
    back4 = list()
    inOrder = list()
    display = str()
    printHelp = 0

    i = 0
    while i < len(cleanList):
        front4 = cleanList[i: i + 4:]
        i += 7
        back4 = cleanList[i: i + 4:]
        i += 7

        print_letter = front4 + back4  
        res = int("".join(map(str, print_letter)), 2)
        display += chr(res)
    print("Message displayed below: ")
    print(display)

    file.close()
