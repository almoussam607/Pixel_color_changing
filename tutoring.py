import math
def main():
    points=[(1,5),(13.5,9),(10,5),(8,2),(16,3)]
    a=distance(points)
    print(a)

    #for i in range(len(points) -1):
       # m = (((points[i + 1][0] - points[i][0])**2) + ((points[i+1][1]-points[i][1])**2)) ** .5
       # print(m)

def distance(points):
                 #13.5       1                    9            5
    mindis=(((points[3][0]-points[2][0])**2)+((points[3][1]-points[2][1])**2) ** 0.5)
    print(mindis)
    index0=0
    index1=1
    for i in range(len(points) - 1):
        d = (((points[i + 1][0] - points[i][0]) ** 2) + ((points[i + 1][1] - points[i][1]) ** 2)) ** .5
        print(d)



regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
match = re.fullmatch(regex, email)

elif match is None:
flash('Email is invalid, the pattern should be real email address.', category='error')

main()


