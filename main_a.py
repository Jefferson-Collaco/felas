import random
import matplotlib.pyplot as plt

# desafio giant steps

class Person:
    def __init__(self, n, N):
        self.p_right = (n)/(N+1)
        self.drank = False
        self.position_in_table = n
        
    def drink(self):
        self.drank = True
    
class Table:
    def __init__(self, N):
        self.number_of_people = N
        self.queue = [Person(i+1, N) for i in range(N)]
        self.N_drank = 0
        self.time_spent = 0
        self.passing_direction = 'none'
        
    def add_time(self):
        self.time_spent = self.time_spent + 1
        
    def print_queue(self):
        for item in range(self.number_of_people):
            print('position in table: ', self.queue[item].position_in_table)
            print('Individual prob for passing the cup the right hand side: ', self.queue[item].p_right)
            print('Individual drank: ', self.queue[item].drank)
            
        
    def check_if_everybody_drank(self):
        if self.N_drank != self.number_of_people:
            return False
        else:
            return True
        
    def drinking_game(self):
        
        print('starting drinking game')
        curr_pos = 1
        self, curr_pos = pass_cup(self, curr_pos)
        
        print('after first person had drank')
        while self.check_if_everybody_drank() != True:
            # print('inside the while')
            print('inside of while curr_pos = ', curr_pos)
            self, curr_pos = pass_cup(self, curr_pos)
            
            print('time spent: ', self.time_spent)
            # print('printing queue')
            # self.print_queue()
            
            print()
        
def get_direction(Person):
    x = random.random()
    
    if x > Person.p_right:
        return "left"
    else:
        return "right"

def pass_cup(Table, curr_pos):
    
    passing_direction = Table.passing_direction

    # check if person drank
    if Table.queue[curr_pos - 1].drank == True:
        pass
    else:
        # drink and pass the cup in either direction
        Table.queue[curr_pos - 1].drink()
        Table.N_drank += 1
        passing_direction = get_direction(Table.queue[curr_pos - 1])
        
    Table.passing_direction = passing_direction
    
    if Table.passing_direction == 'left':
        curr_pos += 1
        curr_pos = fix_index(Table, curr_pos)
    elif Table.passing_direction == 'right':
        curr_pos -= 1
        curr_pos = fix_index(Table, curr_pos)
    else:
        print('table passing direction = ', Table.passing_direction)
        raise Exception
    
    # yes -> just pass the cup in the same direction
    # no -> drink and pass the cup
    
    Table.add_time()
    print(Table.passing_direction)
    
    return Table, curr_pos
    
def fix_index(Table, curr_pos):
    if curr_pos == 0:
        curr_pos = Table.number_of_people
    if curr_pos == Table.number_of_people + 1:
        curr_pos = 1
        
    return curr_pos

def check_if_nth_drink(Table, curr_pos):

    nth_person = Table.queue[curr_pos - 1]
    
    if nth_person.drank == False:
        return True
    if nth_person.drank == True:
        return False
    
def start(Table, N):
    Table.drinking_game()
    return Table

def get_mean(N_iter, N_people):
    
    average = []
    cost_per_queue = []
    
    for i in range(N_iter):
        table = Table(N_people)
        tab_final = start(table, N_people)
        
        tab_final.time_spent -= 1
        
        if i == 0:
            average.append(tab_final.time_spent)
        else:
            aux_average = (average[i-1]*(i) + tab_final.time_spent)/(i+1)
            average.append(aux_average)
        
        # sample_average += tab_final.time_spent
        cost_per_queue.append(tab_final.time_spent)

        # sample_average = float(sample_average/(i+1))
        # average.append(sample_average)
    
    
    return average, cost_per_queue

# exercicio
# a

N_iter = 100
N_people = 3
average, custos = get_mean(N_iter, N_people)

# print(media_10)

plt.plot(average)
plt.plot(custos, '*')
# plt.hist(custos, density=True, bins=30)


# exercicio
# b










