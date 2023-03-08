import torch
import torch.nn as nn
import torch.nn.functional as F

class Block(nn.Module):
	def __init__(self, inChannels, outChannels):
		super().__init__()
		self.conv1 = nn.Conv2d(inChannels, outChannels, 3,padding=1)
		self.relu = nn.ReLU()
		self.conv2 = nn.Conv2d(outChannels, outChannels, 3, padding=1)
		
	def forward(self, x):
		return self.relu(self.conv2(self.relu(self.conv1(x))))
	
class Encoder(nn.Module):
    def __init__(self,channels=[3,32,64,128]):
        super().__init__()
        # Encoder funksjoner
        self.channels = channels
        self.blocks = nn.ModuleList([Block(channels[i],channels[i+1]) for i in range(len(channels)-1)])
        self.maxpool = nn.MaxPool2d(kernel_size=2,stride=2)


    def forward(self, x):
        # forward for encoder
        block_outputs = []
        for i in range(len(self.blocks)-1):
            x = self.blocks[i](x)
            block_outputs.append(x)
            x = self.maxpool(x)

        x = self.blocks[-1](x)
        block_outputs.append(x)
        return block_outputs
    
class Decoder(nn.Module):
    def __init__(self,channels=[128,64,32]):
        super().__init__()
        # Decoder funksjoner
        self.channels = channels
        self.blocks = nn.ModuleList([Block(channels[i], channels[i + 1]) for i in range(len(channels) - 1)])  
        self.upConvs = nn.ModuleList([nn.ConvTranspose2d(channels[i], channels[i + 1], 2, 2) for i in range(len(channels) - 1)]) 
    def forward(self,x,block_outputs):
        x = self.upConvs[0](x)
        # forward for decoder
        for i in range(1,len(self.channels)-1):
            x = self.upConvs[i](x)
            x = torch.cat([x,block_outputs[i]],dim=1)
            x = self.blocks[i](x)

        return x
    
class UNet(nn.Module):
	def __init__(self, encChannels=[3, 32, 64, 128],
		decChannels=[128,64, 32],
		nbClasses=5,
		outSize=(512,512)):
		super().__init__()
		# initialize encoder
		self.encoder = Encoder(encChannels)
		self.decoder = Decoder(decChannels)
		# initialize decoder
		self.head = nn.Conv2d(decChannels[-1], nbClasses, 1)
		self.outSize = outSize

	def forward(self, x):
		encFeatures = self.encoder(x)

		decFeatures = self.decoder(encFeatures[::-1][0], encFeatures[::-1][1:])

		map = self.head(decFeatures)

		map = F.interpolate(map,(512,512))
		return map