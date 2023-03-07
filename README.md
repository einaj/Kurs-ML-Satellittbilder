# Maskinlæring og satellittbilder

Dette repoet inneholder kode og notebooks relatert til en ukes kurs i Maskinlæring på satellittbilder.
Notebookene skal kunne kjøre med conda environmentet GeoML, som lages og aktiveres ved `conda env create --file GeoML.yml` + `conda activate GeoML`. Dette miljøet er bygget opp fra en base av Arcgis Pro 3.1 sitt python miljø, og har dermed også *arcpy* installert og kan brukes i ArcGIS Pro gitt at man har matchende versjon.

## Kursmateriale
- [BackPropagation](notebooks/BackPropagation.ipynb) er en regne/kodeøvelse som går gjennom hva som skjer matematisk med utregning av gradienter under backpropagation for trening av neverale nettverk.
- [IntroTilPytorch](notebooks/IntroTilPytorch.ipynb) er en innføring av de grunnleggende funksjonene i pytorch, som brukes til å håndtere data og bygge nevrale nettverk.
- [GeoDataiPython](notebooks/GeoDataiPython.ipynb) introduserer en klasse og noen enkle funksjoner som er definert i [src/geoutils](src/geoutils.py) for å forenkle håndteringen av GeoTiffer i python.

## Timeplan

![](media/timeplan.jpg)

## Lenker

- Installere [Anaconda](https://www.anaconda.com/products/distribution)
- Alt om [conda-miljøer](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- Pytorch Dokumentasjon og [tutorials](https://pytorch.org/tutorials/)
- Introduksjon til [PyGeo](https://pytorch.org/blog/geospatial-deep-learning-with-torchgeo/)
- [Landcover AI](https://paperswithcode.com/dataset/landcover-ai) et labelet datasett for segmentering av landområder