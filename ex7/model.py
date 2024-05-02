import torch
import torch.nn as nn
import torch.nn.functional as F

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(in_channels=1, out_channels=8, kernel_size=5, padding=2, stride=1)
        self.conv2 = nn.Conv2d(in_channels=8, out_channels=20, kernel_size=5)
        self.conv3 = nn.Conv2d(in_channels=20, out_channels=34, kernel_size=5)

        self.fc1 = nn.Linear(in_features=34*5*5*5, out_features=250)
        self.fc2 = nn.Linear(in_features=250, out_features=120)
        self.fc3 = nn.Linear(in_features=120, out_features=84)
        self.fc4 = nn.Linear(in_features=84, out_features=10)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.avg_pool2d(x, kernel_size=2, stride=2)
        x = F.relu(self.conv2(x))
        x = F.avg_pool2d(x, kernel_size=2, stride=2)
        x = F.relu(self.conv3(x))
        x = F.avg_pool2d(x, kernel_size=2, stride=2)
        # x = x.view(-1, 16*5*5)
        x = torch.flatten(x, 1)
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x


