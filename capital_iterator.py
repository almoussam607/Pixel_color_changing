
# Mohamad Almoussa

class Capitals(object):

    def __init__(self):
        # create dictionaries as in assignment 4
        file1 = open('country_capital_locations.csv')
        country_capital_locations = {}

        for i in file1:
            i = i.split(",")
            if i[0] == 'Country' or i[1] == 'Capital' or i[2] == 'Latitude' or i[3] == 'Longitude':
                continue
            country_capital_locations[i[0]] = i[1], float(i[2]), float(i[3])

        file2 = open('state_capital_locations.csv')
        state_capital_locations = {}
        for j in file2:
            j = j.split(",")
            if j[0] == 'name' or j[1] == 'description' or j[2] == 'latitude' or j[3] == 'longitude':
                continue
            state_capital_locations[j[0]] = j[1], float(j[2]), float(j[3])

        # create list of capitals from above
        d1 = {**state_capital_locations, **country_capital_locations}

        self.result = list(key[0] for key in d1.values())
        self.i = 0
        self.n = len(self.result)





    def __iter__(self):
        return self  # this is all you need here

    def __next__(self):
        # need to keep track of current position
        # return next element from list on each call
        # if end of list: raise StopIteration exception
        if self.i == self.n:

            raise StopIteration()
        else:
            val = self.result[self.i]
            self.i += 1
            return val




if __name__ == '__main__':
    caps = Capitals()  # your object
    for c in caps:
        print(f' Capital city is: {c}')



