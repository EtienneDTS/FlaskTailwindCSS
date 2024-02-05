import os
import subprocess
import textwrap


def start():
    # Get the current working directory and project name
    cur_dir = os.getcwd()
    file_name = cur_dir.split(sep=os.sep)[-1]
    
    # Define directory paths for templates and static files
    templates_dir = os.path.join(cur_dir, "templates")
    static_dir = os.path.join(cur_dir, "static")

    # Create the templates and static directories if they don't exist
    os.makedirs(templates_dir, exist_ok=True)
    css_dir = os.path.join(static_dir, "css")
    src_dir = os.path.join(static_dir, "src")
    os.makedirs(css_dir, exist_ok=True)
    os.makedirs(src_dir, exist_ok=True)

    # Define file paths for package.json and tailwind.config.js
    package_json = os.path.join(cur_dir, "package.json")
    tailwind_config_dir = os.path.join(cur_dir, "tailwind.config.js")
    
    # Generate the content for package.json with the script to run Tailwind CSS in watch mode
    json_init = textwrap.dedent(f"""\
    {{
        "name": "{file_name}",
        "scripts": {{
            "tailwind": "npx tailwindcss -i ./static/src/input.css -o ./static/css/main.css --watch"
        }}  
    }}
    """)
    
    # Generate the content for tailwind.config.js with JIT mode enabled
    tailwind_init = textwrap.dedent("""\
    /** @type {import('tailwindcss').config} */
    module.exports = {
        mode: "jit",
        content: [
            "./templates/*"
        ],
        theme: {
            extend: {},
        },
        plugins: [],
    }
    """)
    
    # Write the content to package.json
    with open(package_json, "w") as f:
        f.write(json_init)
        
    # Install Tailwind CSS using npm
    subprocess.run(["npm", "install", "tailwindcss"])

    # Write the content to tailwind.config.js
    with open(tailwind_config_dir, "w") as f:
        f.write(tailwind_init)
    
    # Create empty main.css file in the css directory
    with open(os.path.join(css_dir, "main.css"), "w") as f:
        pass
    
    # Write initial content to input.css in the src directory
    with open(os.path.join(src_dir, "input.css"), "w") as f:
        f.write(textwrap.dedent("""\
        @tailwind base;
        @tailwind components;
        @tailwind utilities;
        """))

    
if __name__ == "__main__":
    start()
