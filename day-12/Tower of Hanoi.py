def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        print(f"Move disk 1 from {source} → {destination}")
        return
    
    
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    
   
    print(f"Move disk {n} from {source} → {destination}")
    
  
    tower_of_hanoi(n - 1, auxiliary, destination, source)



n = 3
tower_of_hanoi(n, 'A', 'C', 'B')
