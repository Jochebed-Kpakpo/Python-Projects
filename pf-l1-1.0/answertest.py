name = input("what is your name")
job = input("what is your job")
adjective1 = input("first adjective")
adjective2 = input("second adjective")
food1 = input("first food")
food2 = input("second food")
feeling = input("a feeling")

text = f''' {name} started their first Generation course today. They are training as a {job}.
They found their cohort to be very {adjective1} but their teacher was, at least, {adjective2}. 
For lunch they have {food1} and {food2} while reviewing their notes. 
They feel {feeling} but are determined to complete the course.'''

print(text)