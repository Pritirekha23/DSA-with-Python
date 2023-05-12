'''TOWER OF HANOI::
       Rules::Only one disk can transforn in one step.
              Smaller disks are always kept on  larger disk.'''
              
              
def tower_of_hanoi(disk, source, helper, destination):
    if disk == 1:
        print(f'Move disk 1 from tower {source} to tower {destination}')
        return
    tower_of_hanoi(disk-1, source, destination, helper)
    print(f'Move disk  {disk} from tower  {source} to tower {destination}')
    tower_of_hanoi(disk-1, helper, source, destination)

disk=int(input('Enter the number of disks::'))
tower_of_hanoi(disk, 'A', 'B', 'C')


'''
output:
Enter the number of disks::3
Move disk 1 from tower A to tower C
Move disk  2 from tower  A to tower B
Move disk 1 from tower C to tower B
Move disk  3 from tower  A to tower C
Move disk 1 from tower B to tower A
Move disk  2 from tower  B to tower C
Move disk 1 from tower A to tower C  '''