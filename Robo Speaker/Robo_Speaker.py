import os

print("=================================================")
print("========== Welcome to Robo Speaker 2.0 ==========")
print("=================================================")

while True:
    text = input("\nEnter what you want to say: ")
    if text.lower() in ["quit", "exit"]:
        break

    command = f"spd-say '{text}'"
    os.system(command)
