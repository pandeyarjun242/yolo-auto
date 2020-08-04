<!--
*** Thanks for checking out this README Template. If you have a suggestion that would
*** make this better, please fork the repo and create a pull request or simply open
*** an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo, twitter_handle, email
-->





<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/github_username/repo">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">YOLO-AUTO</h3>

  <p align="center">
    Train YOLOv3 custom object detectors in one lines
    <br />
    <a href="https://github.com/pandeyarjun242/yolo-auto"><strong>Explore the code »</strong></a>
    <br />
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

* [About the Project](#about-the-project)
  * [Built With](#built-with)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Usage](#usage)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [License](#license)
* [Contact](#contact)
* [Acknowledgements](#acknowledgements)



<!-- ABOUT THE PROJECT -->
## About The Project


We realised that training custom object detectors can be hard and really tiring. Creators haven't ever taken the step to making custom object detectors easy for all. YOLO-AUTO is an evolving libarary. We provide two liner code to create custom object detectors

Why?
* Your
* You shouldn't be doing the same tasks over and over like creating a README from scratch
* You should element DRY principles to the rest of your life :smile:


### Built With/On

* [Python](https://www.python.org/)
* [Darknet](https://pjreddie.com/darknet/)
* [GitPython](https://pypi.org/project/GitPython/)



<!-- GETTING STARTED -->
## Getting Started

To get started to create some awesome object detectors.

### Installation
 
1. Pip install the package
```sh
pip install yolo-auto
```
2. Gather Data and place in a repository
```sh
data/labels
data/images
```




<!-- USAGE EXAMPLES -->
## Usage

This is the only amount of code you need to write:

_For more examples, please refer to the [Documentation](https://example.com)_


```sh
from yolo_auto.yolov3auto import Yolov3Train

x = Yolov3Train("/Users/arjunpandey/Desktop/AI-Stuff/test/labels/","/Users/arjunpandey/Desktop/AI-Stuff/test/images/",1,['LicensePlate'],"/Users/arjunpandey/Desktop/AI-Stuff/test/")
x.train()
```




<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Your Name - [@instagram_handle](https://instagram.com/_.pandeymonium) - pandeyarjun.242@gmail.com

Project Link: [https://github.com/pandeyarjun242/yolo-auto](https://github.com/pandeyarjun242/yolo-auto)
