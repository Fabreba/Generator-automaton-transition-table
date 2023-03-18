import pandas as pd
class Table:
    def __init__(self,*args):
        self.transi_names = []
        self.states_name = []
        self.dest_states_name = []
        self.historic_transitions = []
        for state in args:
            self.states_name.append(state.name)
            try:
                for hist in state.history_list:
                    self.historic_transitions.append(hist)
                for transition in state.transition_name_list:
                    self.transi_names.append(transition)
                    self.transi_names = sorted(set(self.transi_names))
                for dest in state.dest_name_list:
                    self.dest_states_name.append(dest)

                
            except:
                print("Array de transições vazio")
        print("Transições", self.transi_names)
        print("Estados", self.states_name)
        print("Estados destinos", self.dest_states_name)
    
    
    def create_table(self):
        self.df = pd.DataFrame(index=self.states_name, columns=self.transi_names)
        self.df = self.df.T
        print(self.df)
    def insert_table(self):
        
        for transition in self.historic_transitions:
            print(transition)
            name = transition[0]
            init = transition[1]
            dest = transition[2]
            
            if self.df.loc[name,init] == None:
                self.df.loc[name,init]=dest
            elif self.df.loc[name,init] != None:
               self.df.loc[name,init]=[self.df.loc[name,init],dest]
               

        for i in self.df.columns:
            for j in self.df.index:
                print((self.df.loc[j,i]))
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
    def print_state(self):
        print("Estado", self.name)
        print("Trans list name: ", self.transition_name_list)
        print("Desti list name: ", self.dest_name_list)
        print("Historic: ", self.history_list)

q1 = State('q1')
q2 = State('q2')
q3 = State('q3')

q1.transition('1',q1)
q1.transition('0',q2)
q1.transition('1',q3)
# q3.transition('0',q1)
a = Table(q1, q2,q3)
a.create_table()
a.insert_table()