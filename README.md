# Maskinlæring og satellittbilder

Dette repoet inneholder kode og notebooks relatert til en ukes kurs i Maskinlæring på satellittbilder.

## Lenker

Satellittbilder 

16.02: https://www.jottacloud.com/s/3009c8e7f96e6d54d169728cae64ad305c4

28.02: https://www.jottacloud.com/s/300e4b36cab8cf64f338a67c5eb41dde823

UMBRA eksempelbilder

Paris: http://umbra-open-data-catalog.s3.amazonaws.com/sar-data/tasks/ad%20hoc/Paris%2C%20France/dde73766-d7f1-40aa-babb-6c30300b6d37/2023-02-25-10-12-58_UMBRA-05.tif

Panama kanalen: http://umbra-open-data-catalog.s3.amazonaws.com/sar-data/tasks/Panama%20Canal%2C%20Panama/18a6f561-d058-4dda-bf82-cadebe6be230/2023-06-09-15-08-28_UMBRA-05/2023-06-09-15-08-28_UMBRA-05_GEC.tif

Mange flere: http://umbra-open-data-catalog.s3-website.us-west-2.amazonaws.com/?prefix=sar-data/tasks/


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
