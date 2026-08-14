const API_URL = "http://127.0.0.1:8000";


/* -------------------------
   THEME
------------------------- */

function toggleTheme() {

    document.body.classList.toggle("dark");

}


/* -------------------------
   NAVIGATION
------------------------- */

function openAssistant() {

    document
        .getElementById("assistant")
        .scrollIntoView({
            behavior: "smooth"
        });

}


/* -------------------------
   CHAT
------------------------- */

function enterMessage(event) {

    if (event.key === "Enter") {

        sendMessage();

    }

}


function askQuick(question) {

    document
        .getElementById("userMessage")
        .value = question;

    sendMessage();

}


function addUserMessage(text) {

    const messages =
        document.getElementById("messages");


    const div =
        document.createElement("div");

    div.className =
        "user-message";


    div.innerHTML =
        `<p>${escapeHTML(text)}</p>`;


    messages.appendChild(div);

    messages.scrollTop =
        messages.scrollHeight;

}


function addBotMessage(text) {

    const messages =
        document.getElementById("messages");


    const div =
        document.createElement("div");

    div.className =
        "bot-message";


    div.innerHTML = `

        <div class="avatar">
            ✦
        </div>

        <p>
            ${escapeHTML(text)}
        </p>

    `;


    messages.appendChild(div);

    messages.scrollTop =
        messages.scrollHeight;

}


async function sendMessage() {

    const input =
        document.getElementById(
            "userMessage"
        );


    const message =
        input.value.trim();


    if (!message) {

        return;

    }


    addUserMessage(message);

    input.value = "";


    try {

        const response =
            await fetch(
                `${API_URL}/api/chat`,
                {

                    method: "POST",

                    headers: {

                        "Content-Type":
                            "application/json"

                    },

                    body:
                        JSON.stringify({
                            message: message
                        })

                }
            );


        const data =
            await response.json();


        addBotMessage(
            data.response
        );


    } catch (error) {

        addBotMessage(
            "Astra backend is offline. Start the Python server and try again."
        );

    }

}


/* -------------------------
   TASKS
------------------------- */

function addTask() {

    const input =
        document.getElementById(
            "taskInput"
        );


    const text =
        input.value.trim();


    if (!text) {

        return;

    }


    const taskList =
        document.getElementById(
            "taskList"
        );


    const task =
        document.createElement("div");


    task.className =
        "task";


    task.innerHTML = `

        <input
            type="checkbox"
            onchange="completeTask(this)"
        >

        <span>
            ${escapeHTML(text)}
        </span>

    `;


    taskList.appendChild(task);

    input.value = "";

}


function completeTask(checkbox) {

    const task =
        checkbox.parentElement;


    task.classList.toggle(
        "completed",
        checkbox.checked
    );


    updateCompletedCount();

}


function updateCompletedCount() {

    const completed =
        document.querySelectorAll(
            ".task input:checked"
        ).length;


    document.getElementById(
        "completedTasks"
    ).innerText = completed;

}


/* -------------------------
   CAREER
------------------------- */

function careerAdvice(career) {

    const advice = {

        "Software Developer":
            "Focus on programming fundamentals, data structures, Git, databases, APIs and building real projects.",

        "Cybersecurity":
            "Start with Linux, networking, Python, web security, authentication and defensive security labs.",

        "AI Engineer":
            "Learn Python, statistics, machine learning, APIs, LLM concepts and build practical AI applications."

    };


    addBotMessage(
        advice[career]
    );


    openAssistant();

}


/* -------------------------
   SECURITY
------------------------- */

function escapeHTML(text) {

    return text

        .replaceAll("&", "&amp;")

        .replaceAll("<", "&lt;")

        .replaceAll(">", "&gt;")

        .replaceAll('"', "&quot;")

        .replaceAll("'", "&#039;");

}