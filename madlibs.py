
def main():
    print("Welcome to Mad Libs! Pick a story (chose 1 or 2)\n")
    user = input()

    #user picks which story to fill out
    while(not (user == '1' or user == '2')):
        print("Invalid. Please try again")
        user = input()

    #reads .txt file
    with open("madlibs.txt") as file:
        stories = file.read()
    
    #finds the correct story
    story_number = stories.find("#")+1
    while(not(stories[story_number] ==  user)):
        story_number = stories.find("#", story_number)+1

    #saves the correct story in a new string
    story = stories[story_number + 1:stories.find("#", story_number+1)]
  
    blank = []

    start = story.find("$")
    end = 0

    #goes through the story string to pick out the "blanks" surrounded by "$"
    while(not(start == -1)):
        
        end = story.find("$", start + 1 )

        blank.append(story[start:end+1])

        start = story.find("$", end + 1)

    print("\nFill in the blank!")

    #takes in user input and replaces the "blanks"
    for i in blank:
        print("\n" + i[1:-1] + ":\n")
        answer = input()
        story = story.replace(i, answer, 1)

    print("\nHere's the final story:\n")
    
    print(story)

if __name__ == "__main__":
    main()

