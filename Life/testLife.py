from life import *
import sys
import random

inn = sys.stdin
err = sys.stderr
out = sys.stdout

def runTest(testCase):
    return{
        "1": regression,
        "2": testGaia,
        "3": testPartical,
        "4": testTick,
        "5": testTexas,
        "6": testByFile
    }.get(testCase,regression)()

def regression():
    print("---------REGRESSION--------")
    testLib = {
        "1": gaia,
        "2": partical,
        "3": testRule,
    }
    for testCase in testLib:
        testLib[testCase]()


def testGaia():
    print("--------Test Gaia ----------")
    earth = Gaia(5,5)
    earth.show()
    for i in earth.curr:
        for j in i:
            print(j.neighbors())
    earth.show()
    earth.nextTick()
    earth.giveLife(2,3)
    earth.show()
    pass

def testPartical():
    print("--------Test Partical ------------")
    earth = Gaia(5,5)
    earth.curr[1][2].live()
    earth.curr[2][2].live()
    earth.curr[3][2].live()
    earth.curr[2][3].live()
    earth.show()
    earth.curr[2][3].kill()
    earth.show()
    pass

def testTick():
    print("--------Test Tick ------------")
    earth = Gaia(5,5)
    earth.curr[1][2].live()
    earth.curr[2][2].live()
    earth.curr[3][2].live()
    print("State One")
    earth.show()

    print("Start next Tick")
    earth.nextTick()
    earth.show()

    print("Start next Tick")
    earth.nextTick()
    earth.show()
def testTexas():
    print(" -------- Texas is big, let's make a big Board ---------")
    earth = Gaia(100,50)
    earth.curr[1][2].live()
    earth.curr[2][2].live()
    earth.curr[3][2].live()
    print("State One")
    earth.show()

    print("Start next Tick")
    earth.nextTick()
    earth.show()
def testByFile():
    print("---------- Test by a premade file in maps ------------")
    fileName = input("Please choose a map that you want to test: ")
    lines = open('maps/'+fileName,'r')
    firstLine = lines.readline().split(' ')
    H,W = int(firstLine[0]),int(firstLine[1])
    earth = Gaia(H,W)
    for line in lines:
        line = line.split(' ')
        x,y = int(line[0]),int(line[1])
        earth.curr[x][y].live()
    earth.show()
    exit = input('Press anything for next Tick, e for exit ')
    while (exit != 'e'):
        earth.nextTick()
        earth.show()
        exit = input('Press anything for next Tick, e for exit')
    print("Done !!!")
def gaia():
    H , W = random.randint (1,100) ,random.randint (1,100)
    earth = Gaia(H,W)
    assert len(earth.curr) == len (earth.next) == H
    assert len(earth.curr[random.randint(1,H)]) == len(earth.next[random.randint(1,H)]) == W
    print ("Pass gaia test")
def partical():
    p1 = Particle(random.randint(0,100),random.randint(0,100))
    assert (p1.x,p1.y) in p1.neighbors()
    assert (p1.x+1,p1.y-1) in p1.neighbors()
    print("Pass Partical test")
    pass
    
def testRule():
    H , W = random.randint (1,100) ,random.randint (1,100)
    earth = Gaia(H,W)
    for i in range(random.randint(0,H*W)):
        x , y = random.randint (1,H-1) ,random.randint (1,W-1)
        earth.giveLife(x,y)
    pass


if __name__ == "__main__":
    testCase = inn.readline().strip('\n')
    # testCase = str(testCase)
    # print (testCase)
    # testCase = int(testCase)
    runTest(testCase)