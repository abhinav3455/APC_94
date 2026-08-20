employee1 = {"Python", "Java", "SQL", "Git"}
employee2 = {"Python", "C++", "SQL", "Docker"}

print("Common skills:", employee1 & employee2)
print("Skills unique to Employee 1:", employee1 - employee2)
print("Skills unique to Employee 2:", employee2 - employee1)
print("All available skills:", employee1 | employee2)