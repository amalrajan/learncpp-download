# learncpp -> PDF

Just got significantly faster, thanks to parallel processing ⚡

## Support ❤️

Please support here: https://www.learncpp.com/about/


## Installation 

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
Watch out, this uses a lot more CPU and memory as shown:
..

If the script becomes unresponsive, try an older version which downloads tutorials in a sequential fashion.

## Facing trouble?

Feel free to open a new issue here: https://github.com/amalrajan/learncpp-download/issues. Please attach the console logs along.

## License

The MIT License