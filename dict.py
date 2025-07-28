translator={
    "Apple":"ஆப்பிள்",
    "Orange":"ஆரஞ்சு",
    "Banana":"வாழைப்பழம்",
    "Mango":"மாம்பழம்",
    "grapes":"தராட்சை"
}
words=input("Enter the English word:")
if words in translator:
    print("Tamil Meaning:",translator[words])
else:
    print("Sorry ,word not found!")
