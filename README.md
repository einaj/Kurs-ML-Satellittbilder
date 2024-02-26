# Maskinlæring og satellittbilder

Dette repoet inneholder kode og notebooks relatert til en ukes kurs i Maskinlæring på satellittbilder.

## Lenker

Satellittbilder 

16.02: https://www.jottacloud.com/s/3009c8e7f96e6d54d169728cae64ad305c4

28.02: https://www.jottacloud.com/s/300e4b36cab8cf64f338a67c5eb41dde823

<!--
- Installere [Anaconda](https://www.anaconda.com/products/distribution)
- Alt om [conda-miljøer](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html)
- Pytorch Dokumentasjon og [tutorials](https://pytorch.org/tutorials/)
- Introduksjon til [TorchGeo](https://pytorch.org/blog/geospatial-deep-learning-with-torchgeo/)
- [Landcover AI](https://paperswithcode.com/dataset/landcover-ai) et labelet datasett for segmentering av landområder
- [DOTA](https://paperswithcode.com/dataset/dota) Dataset for Object deTection in Aerial Images (RGB)
- [Yolov5](https://github.com/ultralytics/yolov5) Yolov5
- [EuroSAT](https://github.com/phelber/EuroSAT#) Klassifisering av landareale i Sentinel 2 (RGB og Multispektral)
- [CLIP](https://github.com/openai/CLIP) Tekst og bilde modell. Zero-Shot klassifisering.

## Kursmateriale
- [BackPropagation](notebooks/BackPropagation.ipynb) er en regne/kodeøvelse som går gjennom hva som skjer matematisk med utregning av gradienter under backpropagation for trening av neverale nettverk.
- [IntroTilPytorch](notebooks/IntroTilPytorch.ipynb) er en innføring av de grunnleggende funksjonene i pytorch, som brukes til å håndtere data og bygge nevrale nettverk.
- [CIFAR-10 ConvNet](notebooks/CIFAR-10%20ConvNet.ipynb) er en introduksjon til oppsett og trening av konvolusjonsnett for klassifisering.
- [GeoDataiPython](notebooks/GeoDataiPython.ipynb) introduserer en klasse og noen enkle funksjoner som er definert i [src/geoutils](src/geoutils.py) for å forenkle håndteringen av GeoTiffer i python.
- [Segmentering](notebooks/Segmentering.ipynb) setter opp et UNet for semantisk segmentering av landtyper fra satellittbilder.
- [toolbox](toolbox/) er en implemtering av et trent UNet fra Segmenteringsnotebooken, i en Python toolbox for Arcgis Pro. Den kjører i Arcgis 3.1 med conda miljøet som ligger vedlagt, men det kan hende man må lage et eget miljø ved å clone det lokale arcgispro-py3, og installere nødvendige pakker.

-->