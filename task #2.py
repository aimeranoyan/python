time = int(input("Enter time in seconds: "))
hours = time // 3600
minutes = (time - hours * 3600) // 60
seconds = time % 60
print(f"{hours}:{minutes}:{seconds}")