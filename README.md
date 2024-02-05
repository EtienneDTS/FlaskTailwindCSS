# FlaskTailwindCSS

Flask Tailwind CSS is a convenient library designed to automate the integration of Tailwind CSS into your Flask projects with just a simple command. This library simplifies the process of configuring and managing Tailwind CSS, allowing you to focus more on building your Flask application and less on setup hassles.


## Installation

Install PageRouter using `pip`:

```bash
pip install flask-tailwindcss

```

## Usage

Before you proceed, make sure you are in the correct directory.

```bash
pwd
```

path/to/your/project

- project/

    - env/

    - app.py


If this is the case, you can use the following command:

```bash
flask-tailwindcss
```

After executing the command, your project structure should resemble the following:

- project/

    - env/

    - static/

        - css/

            - main.css

        - src/

            - input.css

    - templates/

    - app.py  

    - package.json

    - tailwind.config.js



You can now add in your templates the <link> tag to reference an external stylesheet. Here's an example:

```html
<link rel="stylesheet" type="text/css" href="{{url_for('static', filename='css/main.css')}}">
```

And finally, run the npm server using:

```bash
npm run tailwind
```


## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue.



## License

This project is licensed under the MIT License:

MIT License

Copyright (c) 2024 Etienne DTS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.