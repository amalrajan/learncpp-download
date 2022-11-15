<hr/>

## COLAB FORK
<br/>
Just run: 
<div align="center"><a href="https://colab.research.google.com/github/egemenertugrul/learncpp-download/blob/master/LearnCPP_PDF.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a></div>
<br/><hr/>

# learncpp -> PDF 

Just got significantly faster, thanks to parallel processing ⚡

## Support ❤️

Please support here: https://www.learncpp.com/about/


## Installation

### Docker

```
docker pull amalrajan/learncpp-download:latest
docker run -d --name=learncpp-download -v <host-downloads-path>:/app/downloads --shm-size=1.14gb amalrajan/learncpp-download
```

Replace `host-downloads-path` with a local path on your system where you'd want the files to get downloaded

### Local 

```
git clone https://github.com/amalrajan/learncpp-download.git
cd learncpp-download
pip install -r requirements.txt
```

If you are a Windows user, head over to https://wkhtmltopdf.org/downloads.html and configure the package.
On Linux/MacOS system, you should install this package using your package manager: `wkhtmltopdf`


## Usage

```
python main.py
```

## Parallel processing

Thanks to https://github.com/ray-project/ray, the processing time is now reduced to ~5 seconds from the previous 300 seconds, on a decent system.
Watch out, this uses a lot more CPU and memory.

<!-- ![image](https://raw.githubusercontent.com/amalrajan/learncpp-download/master/screenshots/Screenshot%202022-02-25%20145949.png) -->

In case the script becomes unresponsive on your system, try an older version which downloads tutorials in a sequential fashion. Example, this tree: https://github.com/amalrajan/learncpp-download/tree/517e8c0818de79d3c0420c2e02f4e11c01c0b878.

## Facing trouble?

Feel free to open a new issue here: https://github.com/amalrajan/learncpp-download/issues. Please attach the console logs along.

## License

The MIT License
