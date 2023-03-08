# -*- coding: utf-8 -*-

from pathlib import Path
import sys

toolbox_dir = Path(__file__).parent
weights = (toolbox_dir/Path("bestUnet.pt")).absolute().__str__()

from UNet import UNet
from geoutils import GeoImage, CopyGeoTransform
import numpy as np
import arcpy
import torch


class Toolbox(object):
    def __init__(self):
        """Define the toolbox (the name of the toolbox is the name of the
        .pyt file)."""
        self.label = "AI segmentering"
        self.alias = "aiseg"

        # List of tool classes associated with this toolbox
        self.tools = [SemanticSegmentation]


class SemanticSegmentation(object):
    def __init__(self):
        """Define the tool (tool name is the name of the class)."""
        self.label = "Semantic Segmentation"
        self.description = ""
        self.canRunInBackground = False

    def getParameterInfo(self):
        """Define parameter definitions"""
        image = arcpy.Parameter(
            displayName="Bilde",
            name="bilde",
            datatype=["DEFolder","DERasterDataset"],
            parameterType="Required",
            direction="Input"
        )

        output = arcpy.Parameter(
            displayName="Segmenteringsmaske",
            name="segmenteringsmakse",
            datatype="DERasterDataset",
            parameterType='Derived',
            direction="Output"
        )

        params = [image,output]
        return params

    def isLicensed(self):
        """Set whether tool is licensed to execute."""
        return True

    def updateParameters(self, parameters):
        """Modify the values and properties of parameters before internal
        validation is performed.  This method is called whenever a parameter
        has been changed."""
        return

    def updateMessages(self, parameters):
        """Modify the messages created by internal validation for each tool
        parameter.  This method is called after internal validation."""
        return

    def execute(self, parameters, messages):
        """The source code of the tool."""
        net = UNet()
        if torch.cuda.is_available():
            net = net.to("cuda")
            net.load_state_dict(torch.load(weights,map_location="cuda"))
        else:
            net.load_state_dict(torch.load(weights,map_location="cpu"))
        net.eval()


        fil = parameters[0].valueAsText
        folder = Path(fil).parent
        out_file = folder / Path("segmentert_maske.tif")

        

        image = GeoImage(fil)

        #finn høyde og bredde
        c,H,W = image.data.shape

        # lag en maske som er like stor som bildet
        mask_data = np.zeros((1,H,W))

        for i in range(0,H-512,512):
            for j in range(0,W-512,512):
                local_image=image.data[:,i:i+512,j:j+512]/255
                local_image = torch.from_numpy(local_image).unsqueeze(0).float()
                if torch.cuda.is_available():
                    out = net(local_image.to("cuda")).to("cpu")
                else:
                    out = net(local_image)
                
                _, prediction = torch.max(torch.softmax(out,dim=1),dim=1)
                mask_data[0,i:i+512,j:j+512] = prediction

        mask_image = CopyGeoTransform(image,mask_data,str(out_file))
        parameters[1].value = str(out_file)
        return str(out_file)

    def postExecute(self, parameters):
        """This method takes place after outputs are processed and
        added to the display."""
        return
