import streamlit as st
st.title("Buzzfeed Quiz: What color of the rainbow are you?")

col1, col2, col3 = st.columns([1,2,1])

points = 0

st.image("WebDevLab01/WebDevLab01/Images/basic-emotions.jpg", use_container_width=True)
     #NEW below                               
answer = st.selectbox("**Which attribute describes your personality the best?**", ["Sad", "Angry", "Happy", "Lucky", "Energetic", "Fancy", "Well-Rounded"])
if answer == "Sad":
    points += 4
elif answer == "Angry":
    points += 30
elif answer == "Happy":
    points += 35
elif answer == "Well-Rounded":
    points += 12
elif answer == "Lucky":
    points += 20
elif answer == "Energetic":
    points += 23
elif answer == "Fancy":
    points += 16
st.write('---')
with col2:
    st.image("WebDevLab01/WebDevLab01/Images/thinkEmoji.jpg", use_container_width= True)
    #NEW below
    answer2 = st.number_input("**Pick a number 0-200:**", min_value=0, max_value=200,step=1)
    if 0 <= answer2 <=25:
        points += 4
    elif 26 <= answer2 <=54:
        points += 12
    elif 55 <= answer2 <=83:
        points += 24
    elif 84 <= answer2 <=112:
        points += 28
    elif 113 <= answer2 <=141:
        points += 36
    elif 142 <= answer2 <=171:
        points += 40
    elif 172 <= answer2 <=200:
        points += 48
    st.write('---')
st.image("WebDevLab01/WebDevLab01/Images/nav_weather.jpg", use_container_width=True)
    #NEW below
weather = st.radio(
    "**What is your favorite kind of weather?**",
    ["Clear and Sunny", "Overcast", "Stormy/Rainy", "Snowy",]
    )
if weather == "Clear and Sunny":
    points += 45
elif weather == "Overcast":
    points += 5
elif weather == "Stormy/Rainy":
    points += 20
elif weather == "Snowy":
    points += 35
st.write('---')
st.image("WebDevLab01/WebDevLab01/Images/music.jpg", use_container_width=True)
music = st.radio(
    "What music do you like the most?",
    ["Blues","Rock and Roll","Hip-Hop","Rap","Country","R&B"]
    )
if music == "Blues":
    points += 3
elif music == "Rock and Roll":
    points += 30
elif music == "Hip-Hop":
    points += 45
elif music == "Rap":
    points += 26
elif music == "Country":
    points += 37
elif music == "R&B":
    points += 16
st.write('---')
st.image("WebDevLab01/WebDevLab01/Images/kitties.jpg", use_container_width=True)
    #NEW
kitties = st.text_input("Which word describes Cats the best?(Cute, Boring, Tedious, or Precious)")
if kitties == "Precious":
    st.write("Good answer...")
    st.audio("WebDevLab01/WebDevLab01/youBetter.mp3", format="audio/mp3",autoplay=True)
    points += 45
elif kitties == "Cute":
    st.write("Good answer...")
    st.audio("WebDevLab01/WebDevLab01/youBetter.mp3", format="audio/mp3",autoplay=True)
    points += 50
elif kitties == "Boring":
    points += 25
    st.write("How evil...")
    st.audio("WebDevLab01/WebDevLab01/boo-6377.mp3", format="audio/mp3",autoplay=True)
elif kitties == "Tedious":
    st.write("How evil...")
    st.audio("WebDevLab01/WebDevLab01/boo-6377.mp3", format="audio/mp3",autoplay=True)

    points += 5
st.write('---')
    #NEW
    

if st.button("Complete Quiz"):
    st.audio("WebDevLab01/WebDevLab01/funny-yay-6273.mp3",format="audio/mp3",autoplay=True)

    if 1<=points<=25:
        st.image("WebDevLab01/WebDevLab01/Images/blue.jpg", use_container_width=True)
        st.subheader("**You're blue!**")
    elif 26<=points<=54:
        st.image("WebDevLab01/WebDevLab01/Images/indigo.jpg", use_container_width=True)
        st.subheader("**You're indigo!**")
    elif 55<=points<=83:
        st.image("WebDevLab01/WebDevLab01/Images/purple.jpg", use_container_width=True)
        st.subheader("**You're purple!**")
    elif 84<=points<=112:
        st.image("WebDevLab01/WebDevLab01/Images/green.jpg", use_container_width=True)
        st.subheader("**You're green!**")
    elif 113<=points<=141:
        st.image("WebDevLab01/WebDevLab01/Images/orange.jpg", use_container_width=True)
        st.subheader("**You're orange!**")
    elif 142<=points<=171:
        st.image("WebDevLab01/WebDevLab01/Images/red.jpg", use_container_width=True)
        st.subheader("**You're red!**")
    elif 172<=points:
        st.image("WebDevLab01/WebDevLab01/Images/yellow.jpg", use_container_width=True)
        st.subheader("**You're yellow!**")
        

