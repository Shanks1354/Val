import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="Will You Be My Valentine?", page_icon="❤️", layout="wide")

# Hide default Streamlit elements to make it look cleaner and immersive
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            /* Remove padding and max-width to use full screen */
            .block-container {padding: 0 !important; max-width: 100% !important;}
            /* Attempt to make iframe full height */
            iframe {height: 100vh !important;} 
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Will You Be My Valentine?</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Sacramento&family=Work+Sans:wght@300;400;600&display=swap" rel="stylesheet">
    <style>
        /* Combined CSS */
        body {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f9e3e3;
            font-family: 'Work Sans', sans-serif;
            flex-direction: column;
            overflow: hidden;
        }

        .container {
            text-align: center;
            padding: 20px;
            position: relative;
            z-index: 1;
        }

        h1 {
            font-family: 'Sacramento', cursive;
            font-size: 3.5em;
            color: #d32f2f;
            margin-bottom: 20px;
        }

        .buttons {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 20px;
            margin-top: 20px;
            flex-wrap: wrap;
        }

        .yes-button {
            font-size: 1.5em;
            padding: 10px 20px;
            background-color: #2e7d32;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-family: 'Work Sans', sans-serif;
            font-weight: 600;
            transition: background-color 0.3s, transform 0.1s;
            min-width: 100px;
        }

        .yes-button:hover {
            background-color: #1b5e20;
        }

        .no-button {
            font-size: 1.5em;
            padding: 10px 20px;
            background-color: #c62828;
            color: white;
            border: none;
            border-radius: 8px;
            cursor: pointer;
            font-family: 'Work Sans', sans-serif;
            font-weight: 600;
            transition: background-color 0.3s;
        }

        .no-button:hover {
            background-color: #b71c1c;
        }

        .gif_container img {
            max-width: 100%;
            height: auto;
            max-height: 300px;
            border-radius: 12px;
            margin-top: 30px;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        }

        /* Yes Page specific styles */
        .header_text {
            font-family: 'Sacramento', cursive;
            font-size: 4em;
            color: #d32f2f;
            margin-bottom: 30px;
        }
        
        #yes-screen .gif_container img {
             max-width: 400px;
        }

        /* Mobile adjustments */
        @media (max-width: 600px) {
            h1 { font-size: 2.5em; }
            .header_text { font-size: 2.5em; }
            .buttons { flex-direction: column; gap: 10px; }
            .yes-button, .no-button { width: 100%; max-width: 200px; }
        }
    </style>
</head>
<body>
    <div class="container" id="question-screen">
        <h1>Will you be my Valentine?</h1>
        <div class="buttons">
            <button class="yes-button" onclick="handleYesClick()">Yes</button>
            <button class="no-button" onclick="handleNoClick()">No</button>
        </div>
        <div class="gif_container">
            <img src="https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbW5lenZyZHI5OXM2eW95b3pmMG40cWVrMDhtNjVuM3A4dGNxa2g2dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/VM1fcpu2bKs1e2Kdbj/giphy.gif" alt="Cute GIF">
        </div>
    </div>

    <div class="container" id="yes-screen" style="display: none;">
        <h1 class="header_text">Knew you would say yes!</h1>
        <div class="gif_container">
            <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExMmo3c3l5ODh3ZGN6NHhhaDE2Mjg1ZjkwOXczdDFxbWM3dTBtaW9zaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/9XY4f3FgFTT4QlaYqa/giphy.gif" alt="Happy GIF">
        </div>
    </div>

    <script>
        const messages = [
            "Are you sure?",
            "Really sure??",
            "Are you positive?",
            "Pookie please...",
            "Just think about it!",
            "If you say no, I will be really sad...",
            "I will be very sad...",
            "I will be very very very sad...",
            "Ok fine, I will stop asking...",
            "Just kidding, say yes please! ❤️"
        ];

        let messageIndex = 0;

        function handleNoClick() {
            const noButton = document.querySelector('.no-button');
            const yesButton = document.querySelector('.yes-button');
            noButton.textContent = messages[messageIndex];
            messageIndex = (messageIndex + 1) % messages.length;
            const currentSize = parseFloat(window.getComputedStyle(yesButton).fontSize);
            yesButton.style.fontSize = `${currentSize * 1.5}px`;
        }

        function handleYesClick() {
            document.getElementById('question-screen').style.display = 'none';
            document.getElementById('yes-screen').style.display = 'block';
        }
    </script>
</body>
</html>
"""

# Render the HTML component
# height=1000 ensures enough vertical space on most devices without internal scrolling
components.html(html_content, height=1000, scrolling=False)
