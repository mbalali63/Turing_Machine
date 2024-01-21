import pandas as pd

class Turning:
    def __init__(self,number):
        self.numberOfRules = 6
        self.rulesSet = pd.DataFrame(columns=['Current State','Current Tape','Write to Tape','Move','Update State'])
        self.rulesSet = self.rulesSet.append({'Current State':'qs','Current Tape':'play','Write to Tape':'play','Move':'right','Update State':'q1'},ignore_index = True)
        self.rulesSet = self.rulesSet.append({'Current State':'q1','Current Tape':'0'     ,'Write to Tape':'0'     ,'Move':'right','Update State':'q1'},ignore_index = True)
        self.rulesSet = self.rulesSet.append({'Current State':'q1','Current Tape':'1'     ,'Write to Tape':'1'     ,'Move':'right','Update State':'q1'},ignore_index = True)
        self.rulesSet = self.rulesSet.append({'Current State':'q1','Current Tape':''    ,'Write to Tape':''    ,'Move':'left','Update State':'q2'},ignore_index = True)
        self.rulesSet = self.rulesSet.append({'Current State':'q2','Current Tape':'1'     ,'Write to Tape':'0'     ,'Move':'left','Update State':'q2'},ignore_index = True)
        self.rulesSet = self.rulesSet.append({'Current State':'q2','Current Tape':'0'     ,'Write to Tape':'1'     ,'Move':'stop','Update State':'qh'},ignore_index = True)        
        self.number = number
        self.numberBitsList = [i for i in str(number)]
        self.numberBitsList.insert(0,'play')
        self.numberBitsList.append('')
        self.currentState = 'qs'
        self.currentDir = 'right'
    def runInstruction(self,state,tapeVal,index):
        instruct = self.rulesSet[(self.rulesSet['Current State']==state) & (self.rulesSet['Current Tape']==tapeVal)]
        self.numberBitsList[index] = instruct['Write to Tape'].item()
        self.currentState = instruct['Update State'].item()
        self.currentDir = instruct['Move'].item()
    def runMachine(self):
        index = 0
        tapeVal = 'play'
        while self.currentState != 'qh':
            self.runInstruction(self.currentState, tapeVal, index)
            if (self.currentDir == 'left'):
                index = index - 1
            elif (self.currentDir == 'right'):
                index = index + 1
            elif (self.currentDir == 'stop'):
                index = index + 0
            tapeVal = self.numberBitsList[index]
        result = ''.join(self.numberBitsList[1:])
        return result
                
number = '0101'
turning = Turning(number)
result = turning.runMachine()
print('The result is {}'.format(result))
            
        
        
        
        
        