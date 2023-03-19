import pandas as pd
import numpy as np
class Table:
    def __init__(self,*args):
        self.transi_names = []
        self.states_name = []
        self.historic_transitions = []
        for state in args:
            self.states_name.append(state.name)
            try:
                for hist in state.history_list:
                    self.historic_transitions.append(hist)
                for transition in state.transition_name_list:
                    self.transi_names.append(transition)
                    self.transi_names = sorted(set(self.transi_names))
            except:
                print("Array de transições vazio")
        
    
    def create_table(self):
        self.df = pd.DataFrame(index=self.states_name, columns=self.transi_names)
        # self.df = self.df.T
    def insert_table(self):
        
        for transition in self.historic_transitions:
            name = transition[0]
            init = transition[1]
            dest = transition[2]
            if type(self.df.loc[init,name]) == float:
               self.df.loc[init,name]=dest
            else:
                self.df.loc[init,name]=[self.df.loc[init,name],dest]
                for i in self.df.loc[init,name]:
                    if isinstance(i, list):
                        self.df.loc[init,name].extend(i)  
                        self.df.loc[init,name].remove(i)
                

        for i in self.df.columns:
            for j in self.df.index:
                if type(self.df.loc[j,i]) == float:
                    self.df.loc[j,i]='[Ø]'
        print(self.df)  
            
class State:

    def __init__(self,name):
        self.name = name
        self.transition_name_list = []
        self.dest_name_list = []
        self.history_list = []
    
    def transition(self,transition_name,dest_state):    
        hist_tran = (transition_name,self.name,dest_state.name)
        self.history_list.append(hist_tran)
        self.transition_name_list.append(transition_name)   
        self.dest_name_list.append(dest_state.name)

qs = State('qs')
q1 = State('q1')
q2 = State('q2')
q3 = State('q3')
q4 = State('q4')
qf = State('qf')

qs.transition('1',qs)
qs.transition('1',q1)
qs.transition('2',qs)
qs.transition('2',q2)
qs.transition('3',qs)
qs.transition('3',q3)
qs.transition('4',qs)
qs.transition('4',q4)

q1.transition('1',qf)
q1.transition('2',q1)
q1.transition('3',q1)
q1.transition('4',q1)

q2.transition('1',q3)
q2.transition('2',qf)
q2.transition('3',q3)
q2.transition('4',q3)


q3.transition('1',q3)
q3.transition('2',q3)
q3.transition('3',qf)
q3.transition('4',q3)

q4.transition('1',q4)
q4.transition('2',q4)
q4.transition('3',q4)
q4.transition('4',qf)


a = Table(qs,q1,q2,q3,q4,qf)
a.create_table()
a.insert_table()