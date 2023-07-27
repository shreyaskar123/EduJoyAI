from text2image import generate_image
from text2voice import generate_speech
from make_video import generate_video
from upload_youtube import upload_youtube
from genScript import generate_storyline

# story = generate_story(..., ..., )
story = [
    {
        "Image": "Description of Image 1: An animated illustration of a robot holding a magnifying glass, symbolizing the exploration of AI concepts.",
        "Script": "Welcome, curious minds, to the Explorify channel, your gateway to the incredible world of Artificial Intelligence! Today, we embark on a thrilling adventure where we demystify the inner workings of AI and reveal its secrets. So, strap in and prepare to have your mind blown!",
    },
    {
        "Image": "Description of Image 2: A visual representation of interconnected neurons forming a neural network, showcasing the complexity of AI algorithms.",
        "Script": "Imagine a vast network of interconnected neurons, mimicking the human brain's structure. That's the foundation of Artificial Intelligence. AI systems learn, adapt, and make decisions by processing vast amounts of data through neural networks. It's like teaching a computer to think!",
    },
    {
        "Image": "Description of Image 3: A collage of data points, algorithms, and mathematical equations, representing the data-driven nature of AI.",
        "Script": "Data is the lifeblood of AI. It's like fuel that powers the engines of intelligence. AI algorithms crunch through terabytes of information, extracting patterns and insights. They can recognize faces, translate languages, and even predict future events with remarkable accuracy. It's like having a crystal ball!",
    },
    {
        "Image": "Description of Image 4: An illustration of a robot interacting with humans, showcasing the practical applications of AI in everyday life.",
        "Script": "Artificial Intelligence isn't just a sci-fi concept; it's all around us! From voice assistants like Siri and Alexa to self-driving cars, AI is transforming the way we live. It helps us find the best routes, recommends movies we'll love, and even detects diseases early. It's like having a personal genius by your side!",
    },
    {
        "Image": "Description of Image 5: An artistic representation of AI algorithms making connections and generating insights, highlighting the power of machine learning.",
        "Script": "Machine Learning is the driving force behind AI's ability to learn and improve over time. Just like humans, AI systems learn from experience. They analyze patterns, adapt their behavior, and continuously optimize their performance. It's like having a digital prodigy that keeps getting better!",
    },
    {
        "Image": "Description of Image 6: A futuristic cityscape with autonomous vehicles and smart infrastructure, illustrating the transformative potential of AI in society.",
        "Script": "The potential of AI goes far beyond individual applications. It can revolutionize entire industries and shape the future of humanity. From healthcare to transportation, AI has the power to make our lives easier, safer, and more efficient. It's like a guiding star, leading us to a brighter tomorrow!",
    },
    {
        "Image": "Description of Image 7: A montage of various AI-powered robots and drones, representing the diverse applications of AI across different sectors.",
        "Script": "Robots and drones, once confined to the realm of science fiction, are now becoming a reality, thanks to AI. They can assist in dangerous tasks, explore unknown territories, and even help with household chores. It's like having a team of tireless assistants ready to lend a helping hand!",
    },
    {
        "Image": "Description of Image 8: A visual representation of AI and humans working together, symbolizing the collaboration between humans and machines.",
        "Script": "Despite all the incredible advancements, AI is not here to replace us; it's here to augment our capabilities. By collaborating with AI, we can unlock new frontiers of innovation, creativity, and problem-solving. It's like having a trusted partner in our quest for a better future!",
    },
    {
        "Image": "Description of Image 9: A collage showcasing the ethical considerations of AI, including privacy, bias, and transparency.",
        "Script": "As AI continues to evolve, we must address important ethical considerations. We need to ensure privacy, eliminate biases, and ensure transparency in AI systems. It's like nurturing a responsible and inclusive digital ecosystem, where everyone can benefit.",
    },
    {
        "Image": "Description of Image 10: An engaging image featuring colorful buttons with 'Subscribe' and 'Bell' icons, encouraging viewers to take action.",
        "Script": "Hey there, you curious souls! If you've enjoyed this mind-expanding journey into the world of AI, don't forget to subscribe to the Explorify channel! Hit that subscribe button and be part of our amazing community, where we explore the frontiers of technology together! And make sure to ring that bell icon to never miss any of our future videos. We promise to keep your brain engaged and entertained!",
    },
    {
        "Image": "Description of Image 11: An image expressing gratitude to the viewers and inviting them to join the conversation in the comments section.",
        "Script": "We're incredibly grateful for your support, and we can't wait to have you as part of our Explorify family. So, leave us a comment below and let's continue this thrilling AI adventure together. Remember, the future is ours to explore, and with AI by our side, the possibilities are limitless! Until next time, stay curious and keep exploring!",
    },
    {
        "Image": "Description of Image 12: A playful image showing a thumbs-up icon and the words 'Like and Share' to encourage viewers to engage further with the video.",
        "Script": "And hey, if you enjoyed this video and found it as exciting as we did, don't forget to give it a big thumbs-up and share it with your friends. Let's spread the knowledge and inspire more people to delve into the fascinating world of Artificial Intelligence. Together, we can create a future where AI empowers us all!",
    },
]
prompt = [
    {
        "title": "The History of the Internet - Explained in 3 Minutes",
        "description": "Discover the fascinating journey of the Internet from its humble beginnings to its global impact today. Join us as we explore the key milestones, inventions, and innovations that shaped the digital revolution. Get ready to dive into the exciting history of the Internet!",
        "tags": [
            "history of the internet",
            "internet evolution",
            "digital revolution",
            "technology",
            "online communication",
        ],
        "thumbnail_description": "Vibrant image showcasing a timeline of the Internet's evolution, starting with a computer monitor displaying early dial-up connections, progressing to a laptop with social media icons, and culminating in a futuristic holographic display with streaming video content.",
    },
    {
        "image": "A black and white photograph of a room filled with large mainframe computers, cables, and blinking lights. Technicians in lab coats are busy working on the machines.",
        "script": "Welcome to our educational video on the history of the Internet. In the early days, the Internet was a far cry from the interconnected world we know today. It all began in research laboratories and universities in the 1960s. Picture a room filled with large mainframe computers, cables, and blinking lights. Technicians in lab coats are busy working on the machines, laying the foundation for what would become a groundbreaking technology.",
    },
    {
        "image": "A close-up of a modem connected to a telephone line. The phone cord is plugged into the modem, and data is being transmitted through the line. The computer screen displays text-based content slowly loading.",
        "script": "One of the earliest breakthroughs was the development of the modem, which allowed computers to communicate over telephone lines. Here we have a close-up of a modem connected to a telephone line. The phone cord is plugged into the modem, and data is being transmitted through the line. On the computer screen, you can see text-based content slowly loading, symbolizing the birth of online communication.",
    },
    {
        "image": "A group of people in a meeting room discussing the concept of packet switching. Diagrams and charts are drawn on a whiteboard, illustrating the process of dividing data into packets for efficient transmission.",
        "script": "In the 1970s, the idea of packet switching emerged as a revolutionary way to transmit data across networks. Imagine a group of people in a meeting room, passionately discussing the concept. Diagrams and charts are drawn on a whiteboard, illustrating the process of dividing data into packets for efficient transmission. This breakthrough paved the way for the modern Internet, enabling data to travel across various networks and reach its destination intact.",
    },
    {
        "image": "A collage of colorful websites from the 1990s, featuring vibrant backgrounds, animated GIFs, and text in different fonts and sizes. The screen is crowded with images and text, showcasing the early days of web design.",
        "script": "As the Internet evolved, the World Wide Web was born, introducing a user-friendly way to access information. The 1990s were known for their unique web design aesthetics. Imagine a collage of colorful websites featuring vibrant backgrounds, animated GIFs, and text in different fonts and sizes. The screen is crowded with images and text, reflecting the early days of web design when creativity and experimentation were at their peak.",
    },
    {
        "image": "A smartphone held in someone's hand, displaying popular social media icons such as Facebook, Twitter, Instagram, and YouTube. Notifications are popping up, representing the rise of social networking and online communities.",
        "script": "In the 2000s, the Internet experienced a social revolution with the rise of social media platforms. Now, imagine a smartphone held in someone's hand, displaying popular social media icons such as Facebook, Twitter, Instagram, and YouTube. Notifications are popping up, representing the constant flow of information and the birth of online communities that connect people across the globe.",
    },
    {
        "image": "A futuristic holographic display showing a person immersed in virtual reality. Streaming video content is projected around them, showcasing the cutting-edge technologies that the Internet has enabled.",
        "script": "Fast forward to the present, and we find ourselves in a world where the Internet has transformed various aspects of our lives. Imagine a futuristic holographic display showing a person immersed in virtual reality. Streaming video content is projected around them, symbolizing the cutting-edge technologies that the Internet has made possible. From e-commerce to entertainment, education to communication, the Internet has become an integral part of our daily existence.",
    },
    {
        "image": "A diverse group of people using laptops, tablets, and smartphones, engaged in online activities like shopping, learning, and video conferencing. The screen is filled with a multitude of colorful windows, representing the vast opportunities the Internet offers.",
        "script": "The Internet has opened up a world of possibilities, empowering individuals and transforming industries. Picture a diverse group of people using laptops, tablets, and smartphones, engaged in online activities like shopping, learning, and video conferencing. The screen is filled with a multitude of colorful windows, representing the vast opportunities the Internet offers. It's a reminder of the incredible impact this technology has had on our lives.",
    },
    {
        "image": "An enthusiastic presenter with a big smile, surrounded by like, share, and subscribe buttons. Engaging text prompts appear on the screen, encouraging viewers to take action and leave comments.",
        "script": "We hope you enjoyed this whirlwind tour of the history of the Internet. If you found it informative, give us a thumbs up and share it with your friends. Don't forget to subscribe to our channel for more fascinating videos. We'd love to hear your thoughts in the comments section below. What's your favorite Internet milestone? Did we miss any important moments? Let's keep the conversation going!",
    },
]
# story = generate_storyline(prompt)
generate_image(prompt[1:])
generate_speech(prompt[1:])
video = generate_video()
video = (
    "/Users/shramankar/Downloads/learning_app/story_app/EduJoyAI/output/final_video.mp4"
)
print(video)

upload_youtube(
    video,
    prompt[0]["thumbnail_description"],
    prompt[0]["title"],
    prompt[0]["description"],
    prompt[0]["tags"],
)
