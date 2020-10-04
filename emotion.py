import pandas as pd  # Open source data analysis and manipulation tool

# Show path to your csv file
# Change 'happy' to your emotion
# change on your emotion
csv = pd.read_csv(r'C:\Users\User\Documents\Atom\openpose_tutorial\csv\surprise.csv')

# Below, let's take all our initial states and frames to zero

happy_state_time = 0
happy_state_number = 0

neutral_state_time = 0
neutral_state_number = 0

surprise_state_time = 0
surprise_state_number = 0

unknown_state_time = 0

# Using iterrows() method of the Pandas Dataframe in order to iterate
for index, pos in csv.iterrows():
    if (pos[11] < pos[5] and pos[14] < pos[5] and pos[20] < pos[5] and pos[23] < pos[5] and pos[14] < pos[47] and pos[50] > pos[23]):  # Happy
        happy_state_time += 1
        happy_state_number += 1
    elif (pos[5] < pos[14] and pos[11] < pos[14] and pos[14] < pos[32] and pos[5] < pos[11] and pos[5] < pos[23] and pos[20] < pos[23] and pos[23] < pos[41] and pos[5] < pos[20]):  # Neutral
        neutral_state_time += 1
        neutral_state_number += 1
    elif (pos[2] > pos[14] and pos[14] < pos[5] and pos[2] < pos[23] and pos[23] < pos[5] and pos[13] < pos[49] and pos[46] < pos[22] and pos[10] < pos[13] and pos[22] < pos[19]):  # Surprise
        surprise_state_time += 1
        surprise_state_number += 1
    else:
        unknown_state_time += 1  # Garbage

print("Time the person was in the happy state: " + str(happy_state_time / 29.97) + "\n")
print("Total number of happy moments: " + str(happy_state_number) + "\n")
print("Time the person was in the neutral state: " + str(neutral_state_time / 29.97) + "\n")
print("Total number of neutral moments: " + str(neutral_state_number) + "\n")
print("Time the user was in the surprise state: " + str(surprise_state_time / 29.97) + "\n")
print("Total number of surprise moments: " + str(surprise_state_number) + "\n")
print("Time the person was in the unknown state: " + str(unknown_state_time / 29.97) + "\n")
