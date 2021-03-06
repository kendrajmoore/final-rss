
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/kendrajmoore/final-rss">
    <img src="https://i.ibb.co/R3YjLb1/microphone.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">RSS Converter</h3>

  <p align="center">
    This is a flask app that allows users to turn an RSS feed for a podcast into a website.
    <br />
    <a href="https://kendrajmoore.github.io/final-rss/"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://final-rss-kjm.herokuapp.com/">View Demo</a>
    ·
    <a href="https://github.com/kendrajmoore/final-rss/issues">Report Bug</a>
    ·
    <a href="https://github.com/kendrajmoore/final-rss/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://i.ibb.co/GxzrX4R/Screen-Shot-2021-12-10-at-8-48-48-AM.png)


### Built With

* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [Bootstrap](https://getbootstrap.com/)
* [Feedparser](https://pypi.org/project/feedparser/)
* [spaCy](https://spacy.io/)
* [Listen Notes API](https://www.listennotes.com/api)




<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* Python

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/kendrajmoore/final-rss.git
   ```
2. Install packages
   ```sh
   pip install -r requirements.txt
   ```
3. Get a Listennotes API key
4. Make .env and create a secret key and add API key
5. Start the app
  ```sh
   flask run
   ```


<!-- USAGE EXAMPLES -->
## Usage

The goal was to create an open source tool that provides small, independent or niche podcasters with a tool that allows them to be index by major search engines. This project is a prototype and is in development



1. Select search in the nav bar 
<img src="https://i.ibb.co/GxzrX4R/Screen-Shot-2021-12-10-at-8-48-48-AM.png" alt="Logo" width="400" height="400">
2. Enter a podcast
<img src="https://i.ibb.co/wpKxhR9/Screen-Shot-2021-12-12-at-10-20-13-PM.png" alt="Logo" width="400" height="400">
3. Copy the url
<img src="https://i.ibb.co/r0x4Ypr/Screen-Shot-2021-12-12-at-10-13-54-PM.png" alt="Logo" width="400" height="400">
4. Select RSS feed, paste the url and submit
<img src="https://i.ibb.co/LdcymSX/Screen-Shot-2021-12-12-at-10-25-38-PM.png" alt="Logo" width="400" height="400">

_For more examples, please refer to the [Documentation](https://kendrajmoore.github.io/final-rss/)_



<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/kendrajmoore/final-rss/issues) for a list of proposed features (and known issues).



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature`)
3. Commit your Changes (`git commit -m 'Add some feature'`)
4. Push to the Branch (`git push origin feature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Project Link: [https://github.com/kendrajmoore/final-rss](https://github.com/kendrajmoore/final-rss)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements
These are code snippets I reused 

* [README template | Github: othneildrew](https://github.com/othneildrew/Best-README-Template)
* [Flask tutorial | Miguel Grinberg](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms)
* [Background Linear Gradient | Codepen Manual Pinto](https://codepen.io/P1N2O/pen/pyBNzX)
* [Keyword Pipeline| Github: jaketae](https://github.com/jaketae/wordwise)
* [Regex| stackoverflow](https://stackoverflow.com/questions/3398852/using-python-remove-html-tags-formatting-from-a-string/3398894)
* [spaCy code | Towards Data Science Mammohan Singh](https://towardsdatascience.com/keyword-extraction-process-in-python-with-natural-language-processing-nlp-d769a9069d5c)






[license-shield]: https://img.shields.io/badge/License-MIT-yellow.svg
[license-url]: https://opensource.org/licenses/MIT
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/kendrajmoore/
[product-screenshot]: https://i.ibb.co/wKH4htP/Screen-Shot-2021-12-10-at-9-32-25-AM.png