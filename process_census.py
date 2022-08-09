#For this assignment you are to process recent US Census Bureau data that was generated on December 21, 2021.

#Your program should have a function called process_file() and read the census data file specified above creating a python list
#where each element of the list is a line of the file.

def process_file(filename):
    file = open(filename)
    list = []
    for i in file:
        i = i.split(",")
        list.append(i)
    return list

#count_elements() that takes the list created above as an argument and returns the number of elements in the list
#(effectively returning the number of lines in the file)

def count_elements(num):
    total = 0
    for i in num:
        total += 1
    return total

#higher_birth_rate() that takes the list created and returns a list of states that have a higher birth rate than death rate

def higher_bith_rate(high):
    list = []
    for line in high:
        if line[3] == '0' or line[3] == 'STATE':
            continue
        if float(line[24]) > float(line[25]):
            list.append(line[4])
    return list


#neg_pop_change() that takes the list created and returns a list of states that
#have a negative population change for 2021, and the percentage of the state population (use population estimate for 2021)

def neg_pop_change(ne):
    list = []
    tuples = ()
    avg = 0
    for line in ne:
        if line[3] == '0' or line[3] == 'STATE':
            continue
        list.append([line[4], int(line[9]), int(line[7])])
    for i in list:
        if i[1] < 0:
            avg += i[1] / i[2]
            tuples = tuples + ((i[0], avg), )

    return tuples


# top_ten_states() that takes the list created and returns a list containing the top ten states in terms of population.  The
# list should be in descending order by population.

def top_ten_states(top):

    list = []
    for rec in top:
        if rec[3] == 0 or rec[3] == 'STATE': # if this is not a state
            continue
        list.append([rec[4], rec[7]])
        list.sort(key=lambda y: y[1])

    # now we have a list of state,population pairs
    result = list[0:10]
    result.reverse()

    return result










if __name__ == '__main__':
   census_list = process_file('NST-EST2021-alldata.csv')
   print(census_list)
   num_elems = count_elements(census_list)
   print(num_elems)
   higher_birth_list = higher_bith_rate(census_list)
   print(higher_birth_list)
   print(neg_pop_change(census_list))
   top_ten_list = top_ten_states(census_list)
   print(top_ten_list)