<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Read me</title>
    <style>
        code {
            background-color: darkslategray;
            color: greenyellow;
            font-size: larger;
        }
    </style>
</head>
<body>
<h1>Fruits detection with yolov8</h1>

<p>Install</p>
<ol>
    <li>
        <h3>Virtual environtment</h3>
        <ol>
            <li><p>You can install virtual environtment with anaconda or venv package of python.</p>
                <p>In this project, I created a virtual environtment named 「venv」</p>
                <ul>
                    <li>
                        <p>venv package</p>
                        <code>py -m venv venv</code>
                    </li>
                    <li>
                        <p>anaconda</p>
                        <code>conda create --name venv python=3.11</code>
                    </li>
                </ul>
            </li>
            <li><p>Then activate the environtment.</p>
                <ul>
                    <li>
                        <p>venv package</p>
                        <code>.\venv\Scripts\activate</code>
                    </li>
                    <li>
                        <p>anaconda</p>
                        <code>conda activate venv</code>
                    </li>
                </ul>
            </li>
            <li>Change directory to this project.</li>
        </ol>
    </li>
    <li>
        <h3>YOLOv8 model</h3>
        <p>
            <code>pip install ultralytics</code>
        </p>
    </li>
</ol>
</body>
</html>
