import rasterio as rio
import geopandas as gpd
from shapely.geometry import mapping
from rasterio.mask import mask
from os import PathLike
from typing import Union
import numpy as np
import matplotlib.pyplot as plt


class GeoImage():
    """
    En klasse som holder på bildedataen og geotransformen til georefererte bilder
    """
    def __init__(self, source: Union[str,PathLike]):
        self.filepath = source
        self.ROI = None
        self.original = {}
        with rio.open(source) as src:
            self.original["data"] = src.read()
            self.original["transform"] = src.transform
            self.bounds = src.bounds
            self.metadata = src.tags()
            self.crs = src.crs

    def preview(self, useROI: bool=True):
        """
        Viser frem en thumbnail av bildet.
        Hvis useROI er True brukes ROI maske gitt at den er definert.

        Kwargs:
            useROI: bool, om ROI eller orignalt bilde skal vises 
        """
        # TODO: hva hvis ikke 1 eller 3 kanaler
        if useROI and self.ROI is not None:
           plt.imshow(self.ROI["data"].transpose(1,2,0)) 
        else:
            plt.imshow(self.original["data"].transpose(1,2,0))
        plt.axis("off")
        plt.show()

    def setROI(self, polygons: list[dict], nodata=0):
        """
        Oppdaterer ROI til bildet ved å lagre lese av originalbildet gjennom en maske defienert
        av et sett med polygoner. Lagrer infoen for ROI til bildet i dicten self.ROI.

        For å fjerne ROI, kan man bare sette object.ROI = None

        Args:
            polygons: list med polygoner i en dict på Python Geo Interface Protocol
        
        Kwargs:
            nodata: verdien som skal settes til piksler innenfor crop, men utefor maskert område
        """
        with rio.open(self.filepath) as source:
            roi_data, roi_transform = mask(source,polygons,crop=True,nodata=nodata)
        self.ROI = {"shapes":polygons, "data":roi_data, "transform":roi_transform}

    def save(self,filepath: Union[str,PathLike], useROI:bool = True):
        """
        Funksjon som lagrer det gjeldende dataen med tilhørende georefereing i fil oppgitt 
        i filename. Bruker ROI med crop dersom useROI er True.

        Args:
            filepath: str, filsti der bildet skal lagres (path/til/bilde/xxx.tif)
        
        Kwargs:
            useROI: bool, om ROI eller orignalt bilde skal brukes
        """
        if useROI and self.ROI is not None:
            data = self.ROI["data"]
            transform = self.ROI["transform"]
        else:
            data = self.original["data"]
            transform = self.original["transform"]

        if self.crs is None:
            crs = '+proj=latlong'
        else:
            crs = self.crs

        new_tiff = rio.open(
            str(filepath),
            'w',
            driver='GTiff',
            height=data.shape[1],
            width=data.shape[2],
            count=data.shape[0],
            dtype=data.dtype,
            crs=crs,
            transform=transform,
        )

        for k in self.metadata.keys():
            exec(f'new_tiff.update_tags({k}="{self.metadata[k]}")')

        new_tiff.write(data)
        new_tiff.close()

    @property
    def data(self) -> np.ndarray:
        if self.ROI is None:
            return self.original["data"]
        else:
            return self.ROI["data"]
        
    @data.setter
    def data(self,x):
        if self.ROI is None:
            self.original["data"] = x
        else:
            self.ROI["data"] = x
        
    @property
    def transform(self) -> rio.Affine:
        if self.ROI is None:
            return self.original["transform"]
        else:
            return self.ROI["transform"]

def CopyGeoTransform(source: GeoImage, data: np.ndarray, filepath: Union[str,PathLike], useROI=True) -> GeoImage:
    """
    Kopierer geotransformen og metadataen fra et GeoImage og setter den på ny data.

    Args:
        source: GeoImage transformen skal hentes fra
        data: den nye bildedataen
        filepath: filnavn det nye bildet skal lagres under
        
    Kwargs
        useROI: om ROI eller hele bildet skal brukes, gitt at ROI er definert
    """
    if useROI and source.ROI is not None:
        transform = source.ROI["transform"]
    else:
        transform = source.original["transform"]

    if source.crs is None:
        crs = '+proj=latlong'
    else:
        crs = source.crs

    new_tiff = rio.open(
        str(filepath),
        'w',
        driver='GTiff',
        height=data.shape[1],
        width=data.shape[2],
        count=data.shape[0],
        dtype=data.dtype,
        crs=crs,
        transform=transform,
    )

    for k in source.metadata.keys():
        exec(f'new_tiff.update_tags({k}="{source.metadata[k]}")')


    new_tiff.write(data)
    new_tiff.close()
    return GeoImage(filepath)

def readPolygon(filepath) -> list[dict]:
    """
    Funksjon som bruker geopandas og shapely til å lese inn en polygon fra en geojson 
    eller shapefile og konverterer det til Python Geo Interface Protocol.
    
    Args:
        filepath: filsti til shapefile eller geojson som definerer polygoner
    """

    geofile = gpd.read_file(filepath)
    return [mapping(g) for g in geofile.geometry.values]
