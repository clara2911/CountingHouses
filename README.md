# Welcome to Counting Houses

## What is this?
Counting how many people live in an area in Malawi using Google Maps.
Why? TODO
![Satellite image of Blantyre,Malawi](images/satellite_image.png)




## How to run
`python entrypoint.py` (once you've completed setup below)



## Setup
### Python environment
```commandline
conda create --name counting-houses python==3.11 -y
conda activate counting-houses
pip install poetry
poetry install
```

### Google maps API connection
1. Go to the Google Cloud Console.
2. Click on "Select a project" and then "New Project".
3. Enter the project name and billing account, then click "Create".
4. Navigate to the "API & Services" > "Library" in the Google Cloud Console.
5. Search for and enable Maps Static API
6. Go to "API & Services" > "Credentials".
7. Click "Create Credentials" and select "API Key".
8. Copy the API key that is generated into a txt file and call it `credentials.txt`. 

# Contributors
Koen Greuell & [Clara Tump](https://github.com/clara2911)
