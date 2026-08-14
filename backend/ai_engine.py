def generate_response(message):

    text = message.lower()


    if "study plan" in text:

        return (
            "Here is a simple study plan: "
            "Start with 45 minutes of your main subject, "
            "take a 10-minute break, then practise "
            "programming for 30 minutes. Finish by "
            "reviewing what you learned."
        )


    if "programming" in text:

        return (
            "For programming, focus on fundamentals first: "
            "variables, conditions, loops, functions, "
            "classes, arrays and data structures. "
            "Then build small projects."
        )


    if "career" in text:

        return (
            "Choose a career based on the skills you enjoy. "
            "For software development learn programming, "
            "Git, databases and web development. "
            "For cybersecurity learn Linux, networking "
            "and security fundamentals."
        )


    if "resume" in text:

        return (
            "A strong student resume should contain "
            "education, technical skills, projects, "
            "achievements, certifications and links "
            "to GitHub and LinkedIn."
        )


    if "github" in text:

        return (
            "Keep your GitHub projects organised. "
            "Use a clear README, meaningful commits, "
            "screenshots, installation instructions "
            "and a clear technology stack."
        )


    if "python" in text:

        return (
            "Start Python with variables, data types, "
            "conditions, loops, functions, lists, "
            "dictionaries, files and object-oriented "
            "programming."
        )


    if "c#" in text:

        return (
            "For C#, begin with variables, data types, "
            "conditions, loops, methods, classes, "
            "objects, constructors and collections."
        )


    return (
        "I am Astra AI, your academic and career "
        "copilot. Ask me about studying, programming, "
        "projects, GitHub, resumes, careers or "
        "productivity."
    )