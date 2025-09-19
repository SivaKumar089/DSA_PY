def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} → {destination}")
        return
    
    # Move n-1 disks from source to auxiliary
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    
    # Move nth disk from source to destination
    print(f"Move disk {n} from {source} → {destination}")
    
    # Move n-1 disks from auxiliary to destination
    tower_of_hanoi(n - 1, auxiliary, destination, source)


# Example
n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
