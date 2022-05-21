from cmath import cos, pi, sin
import math
from operator import concat
from matplotlib import scale, style
import matplotlib.pyplot as plot
from numpy import block, real, sort
from prettytable import PrettyTable

def sort_dict(d):
    d = dict(sorted(d.items()))
    return d

def edit_data(table, angles):
    con = '1'
    while(con != '0'):
        choice = input("\nenter:\n1 to remove an angle\\s\n2 to add an angle\\s\n3 to edit an angel\'s\\angels\' value\n0 to return to main menu\nyour choice: ")
        if choice == '1':
            conRem = '1'
            #remove a point
            while conRem != '0':
                print(table)
                points = list(map(int, input('\nenter the angles you want to remove: ').split()))
                for point in points:
                    itr = 0
                    if point in angles:
                        for i in angles:    
                            if i != point:
                                itr+=1
                            if i == point:
                                break
                        angles.pop(point)
                        table.del_row(itr)
                        print('\nangle %d has been removed succesfully'%(point))
                    else:
                        print('\nangle %d does not exist\nchoose an existing angle from the table '%(point))
                print("")
                print(table)
                conRem = input('\ndo you wish to remove any other point?\n0 to exit edit\nanything else to continue\nyour choice: ') 


        elif choice == '2':
            conAdd = '1'
            #add angle
            while conAdd != '0':
                points = list()
                points = concat(points, (list(map(int, input('\nenter the angles you want to add: ').split()))))
                print("")
                for i in points:
                    if i not in angles:
                        v = int(input('enter the value of angle %d: '%(i)))
                        angles[i] = v
                    else:
                        print("the angle %d already exists"%(i))
                angles = sort_dict(angles)
                table.clear_rows()
                table.add_rows(angles.items())
                print('points have been added succesfully')
                print(table)
                conAdd = input("\ndo you wish to add any thing else?\n0 to exit add\nanything else to continue\nyour choice: ")
        elif choice == '3':
            #edit angle
            conEdit = '1'
            while conEdit != '0':    
                points = list(map(int, input('\nenter the  angles you want to edit: ').split()))
                for point in points:
                    if point in angles:
                        v = int(input("\nold value of angle %d = %d\nenter the new value of angle %d: "%(point, angles[point], point)))
                        angles[point] = v
                        cnt = 0
                        for i in angles:
                            if i != point:
                                cnt+=1
                            else:
                                break
                        table.clear_rows()
                        table.add_rows(angles.items())
                        print('point %d have been edited succesfully\n'%(point))
                    else:
                        print('angle %d not found\n'%(point))
                print(table)
                conEdit = input('\ndo you wish to edit any other point?\n0 to exit edit\nanything else to continue\nyour choice: ')
        elif choice == '0':
            return (table, angles)
        else:
            print('\nenter a valid choice\n')
            continue
        con = input('\n\ndo you wish for further editing?\nenter:\n0 to return to main menu\nanything else to continue\nyour choice: ')
    return (table, angles)


def draw_graph(angles):
    points = []
    values = []
    for point, value in angles.items():
        points.append(point)
        values.append(value)
        plot.scatter(point, value)
        plot.ion()
        plot.show()
    plot.plot(points, values)
    plot.plot([0, 400], [0, 0], color = 'black')
    for n in points:
        plot.plot([n,n], [1.1*min(values), angles[n]], linestyle = 'dashed')
    plot.ylim(1.1*min(values), 1.5*max(values))
    plot.xlim(0, points[-1]*1.1)
    plot.xlabel('angle')
    plot.ylabel('value')
    plot.xticks(points)
    F_eq(points, values)
    


def F_eq(angles, volts):
    p = len(angles)
    a0 = round((1/p)*sum(volts), 2)
    a = list()
    b = list()
    for n in range(1, 4):
        suma = 0
        sumb = 0
        for k in range(1, p+1):
            suma += volts[k-1]*real(cos(n*angles[k-1]*pi/180))
            sumb += volts[k-1]*real(sin(n*angles[k-1]*pi/180))
        a.append(round(2/p*suma, 2))
        b.append(round(2/p*sumb, 2))
    print('equation of curve = %f + %f cos(\u03F4) + %f cos(2\u03F4) + %f cos(3\u03F4)+.....\n+%f sin(\u03F4)+ %f sin(2\u03F4) + %f sin(3\u03F4)'%(a0, a[0], a[1], a[2], b[0], b[1], b[2]))
    #30 60 90 120 150 180 210 240 270 300 330 360
    #62 35 -38 -64 -63 -52 -28 24 80 96 90 70
    



def get_input():
    print("please, enter space seperated angles")
    angles = dict()
    keys = list(map(int, input().split()))
    
    inChoice = input('\n*enter 1 to enter values separately.\n*enter any other number to enter values in one line\nyour choice: ')
    if inChoice == '1':
        print("")
        for x in keys:
            angles[x] = int(input('enter the value of the %d degrees angle: '%(x)))
    else:
        print('\nenter space separated %d values in order'%(len(keys)))
        values = list(map(int, input().split()))
        if len(values) < len(keys):
            print("\nmore values are required\n")
            for n in range(len(values),len(keys)):
                 values.append(int(input('enter the value of the %d degrees angle: '%(keys[n]))))
        for k,v in zip(keys, values):
                angles[k] = v
    angles = sort_dict(angles)
    #put it in table
    table = PrettyTable(['angle', 'value'])
    table.add_rows(angles.items())
    print(table)
    
    return (table, angles)




if __name__ == "__main__":

    points = dict()
    #take input data
    table, points = get_input()

    while(1):
        choice = input("\nenter:\n1 to edit data \n2 to draw graph\n0 to exit\nyour choice: ")
        if choice == '1':
            table, points = edit_data(table, points)
            print('finished editing...')
        elif choice == '2':
            draw_graph(points)
        elif choice == '0':
            break
        else:
            print("\nenter valid number")
    print('\n\ngoodbye ;)\n\n')



