import torch
from torchvision import datasets, transforms as transforms
from torch.utils.data import DataLoader, random_split, Subset
from sklearn.model_selection import train_test_split
import numpy as np

def load_mnist(batch_size=64, normalise=True, train_transforms=[], val_split=True, data_root='./data'): # TODO replace to multi epoch pre-loader
    """
    Loads the MNIST dataset with specified transformations and returns data loaders.
    
    Args:
        batch_size (int, optional): The number of samples per batch to load. Default is 64.
        normalise (bool, optional): Whether to normalize the dataset. Default is True.
        train_transforms (list, optional): List of additional transformations to apply to the training data. Default is an empty list.
        val_split (bool, optional): Whether to split the training data into training and validation sets. Default is True.
        data_root (str, optional): Root directory where the dataset will be stored. Default is './data'.
    
    Returns:
        tuple: If val_split is True, returns a tuple of DataLoader objects (train_loader, val_loader, test_loader). Otherwise, returns (train_loader, test_loader).

    
    The returned DataLoader objects have the following additional attributes:
        - mean (torch.Tensor): The mean value used for normalization.
        - std (torch.Tensor): The standard deviation value used for normalization.
        - min (torch.Tensor): The minimum value in the dataset.
        - max (torch.Tensor): The maximum value in the dataset.
        - normalised (bool): Whether the dataset was normalized.
    
    Example:
        train_loader, val_loader, test_loader = load_mnist(batch_size=32, normalise=True, train_transforms=[transforms.RandomRotation(10)], val_split=True, data_root='./data')
    """
    if normalise:
        mean = torch.tensor([0.1307])
        std = torch.tensor([0.3081])
    else:
        mean = torch.tensor([.5])
        std = torch.tensor([1])
    if normalise:
        train_transform = transforms.Compose([
            *train_transforms,
            transforms.ToTensor(),
            transforms.Normalize(mean, std)
        ])
        test_transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean, std)
        ])
    else:
        train_transform = transforms.Compose([
            *train_transforms,
            transforms.ToTensor()    
        ])
        test_transform = transforms.Compose([transforms.ToTensor()])
        
    train_dataset = datasets.MNIST(root=data_root, train=True, download=True, transform=train_transform)
    test_dataset = datasets.MNIST(root=data_root, train=False, transform=test_transform)
    if val_split:
        train_dataset, val_dataset = random_split(train_dataset, [0.8, 0.2])
        val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=True, num_workers=2)
    

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=2)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=2)
    
    # Initialize variables to track the min and max values
    min_val = float('inf')
    max_val = float('-inf')

    # Loop over the dataset
    for data, _ in train_loader:
        min_val = min(min_val, data.min().item())
        max_val = max(max_val, data.max().item())
    
    min_val, max_val = torch.tensor(min_val), torch.tensor(max_val)

    print(f'MNIST dataset - Min value: {min_val}, Max value: {max_val}')
    
    train_loader.mean, train_loader.std, train_loader.min, train_loader.max, train_loader.normalised = mean, std, min_val, max_val, normalise
    test_loader.mean, test_loader.std, test_loader.min, test_loader.max, test_loader.normalised = mean, std, min_val, max_val, normalise
    
    if val_split:
        val_loader.mean, val_loader.std, val_loader.min, val_loader.max, val_loader.normalised = mean, std, min_val, max_val, normalise
        return train_loader, val_loader, test_loader
    else:
        return train_loader, test_loader

def load_cifar10(batch_size=64, normalise=True, train_transforms=[transforms.RandomHorizontalFlip(), transforms.RandomCrop(32, 2, padding_mode='edge')], val_split=True, data_root='./data'):
    """
    Load the CIFAR-10 dataset with optional normalization and data augmentation.
    
    Args:
        batch_size (int, optional): The number of samples per batch to load. Default is 64.
        normalise (bool, optional): Whether to normalize the dataset. Default is True.
        train_transforms (list, optional): List of transformations to apply to the training data. Default is [transforms.RandomHorizontalFlip(), transforms.RandomCrop(32, 2, padding_mode='edge')].
        val_split (bool, optional): Whether to split the training data into training and validation sets. Default is True.
        data_root (str, optional): Root directory where the dataset will be stored. Default is './data'.
    
    Returns:
        tuple: If val_split is True, returns a tuple of DataLoader objects (train_loader, val_loader, test_loader). Otherwise, returns (train_loader, test_loader).
    
    The DataLoader objects have the following attributes:
        - mean (torch.Tensor): The mean used for normalization.
        - std (torch.Tensor): The standard deviation used for normalization.
        - min (torch.Tensor): The minimum value in the dataset.
        - max (torch.Tensor): The maximum value in the dataset.
        - normalised (bool): Whether the dataset was normalized.
    """
    if normalise:
        mean = torch.tensor([0.4914, 0.4822, 0.4465])
        std = torch.tensor([0.247, 0.243, 0.261])
    else:
        mean = torch.tensor([.5, .5, .5])
        std = torch.tensor([1, 1, 1])
    if normalise:
        train_transform = transforms.Compose([
            *train_transforms,
            transforms.ToTensor(),
            transforms.Normalize(mean, std),
        ])
        test_transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean, std),
        ])
    else:
        train_transform = transforms.Compose([
            *train_transforms,
            transforms.ToTensor(),
        ])
        test_transform = transforms.Compose([
            transforms.ToTensor(),
        ])

    train_dataset = datasets.CIFAR10(root=data_root, train=True, download=True, transform=train_transform)
    test_dataset = datasets.CIFAR10(root=data_root, train=False, transform=test_transform, download=True)
    if val_split:
        train_dataset, val_dataset = random_split(train_dataset, [0.8, 0.2])
        val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=True, num_workers=2)
        val_loader.mean, val_loader.std = mean, std
    

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=2)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=2)
    
    # Initialize variables to track the min and max values
    min_val = float('inf')
    max_val = float('-inf')

    # Loop over the dataset
    for data, _ in train_loader:
        min_val = torch.tensor(min(min_val, data.min().item()))
        max_val = torch.tensor(max(max_val, data.max().item()))

    print(f'CIFAR10 dataset - Min value: {min_val}, Max value: {max_val}')
    
    train_loader.mean, train_loader.std, train_loader.min, train_loader.max, train_loader.normalised = mean, std, min_val, max_val, normalise
    test_loader.mean, test_loader.std, test_loader.min, test_loader.max, test_loader.normalised = mean, std, min_val, max_val, normalise
    
    if val_split:
        val_loader.mean, val_loader.std, val_loader.min, val_loader.max, val_loader.normalised = mean, std, min_val, max_val, normalise
        return train_loader, val_loader, test_loader
    else:
        return train_loader, test_loader
    
def load_gtsrb(batch_size=64, normalise=True, train_transforms=[transforms.RandomRotation(10), transforms.RandomResizedCrop(size=(30, 30), scale=(0.85, 1.0)), transforms.RandomAffine(degrees=0, translate=(0.1, 0.1), shear=15),], val_split=True, data_root='./data'):
    """
    Load the German Traffic Sign Recognition Benchmark (GTSRB) dataset with optional normalization and data augmentation.
    
    Args:
        batch_size (int, optional): The number of samples per batch to load. Default is 64.
        normalise (bool, optional): Whether to normalize the dataset using predefined mean and std values. Default is True.
        train_transforms (list, optional): List of torchvision transforms to apply to the training data. Default includes random rotation, resized crop, and affine transformations.
        val_split (bool, optional): Whether to split the training data into training and validation sets. Default is True.
        data_root (str, optional): Root directory where the dataset is stored or will be downloaded. Default is './data'.
    
    Returns:
        tuple: If val_split is True, returns a tuple of DataLoader objects (train_loader, val_loader, test_loader). Otherwise, returns (train_loader, test_loader).
    
    The DataLoader objects returned have additional attributes:
        - mean (torch.Tensor): The mean used for normalization.
        - std (torch.Tensor): The standard deviation used for normalization.
        - min (torch.Tensor): The minimum value in the dataset.
        - max (torch.Tensor): The maximum value in the dataset.
        - normalised (bool): Whether the dataset was normalized.
    """
    if normalise:
        mean = torch.tensor([0.3403, 0.3121, 0.3214])
        std =  torch.tensor([0.2724, 0.2608, 0.2669])
    else:
        mean = torch.tensor([.5, .5, .5])
        std = torch.tensor([1, 1, 1])
    if normalise:
        train_transform = transforms.Compose([
            *train_transforms,
            transforms.Resize((30, 30)),
            transforms.ToTensor(),
            transforms.Normalize(mean, std),
        ])
        test_transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Resize((30, 30)),
            transforms.Normalize(mean, std),
        ])
    else:
        train_transform = transforms.Compose([
            *train_transforms,
            transforms.Resize((30, 30)),
            transforms.ToTensor(),
        ])
        test_transform = transforms.Compose([
            transforms.Resize((30, 30)),
            transforms.ToTensor(),
        ])

    train_dataset_ori = datasets.GTSRB(root=data_root, split='train', download=True, transform=train_transform)
    test_dataset = datasets.GTSRB(root=data_root, split='test', download=True, transform=test_transform)
    
    if val_split:
        file_names = train_dataset_ori._samples
        track_id_to_sample = [name[0].split("/")[-2] + "_" + name[0].split("/")[-1].split("_")[0] for name in file_names]
        track_ids = set(track_id_to_sample)
        train_track_ids, val_track_ids = train_test_split(np.array(list(track_ids)), test_size=0.2, train_size=0.8)
        train_ids = [i for i in range(len(track_id_to_sample)) if track_id_to_sample[i] in train_track_ids]
        val_ids = [i for i in range(len(track_id_to_sample)) if track_id_to_sample[i] in val_track_ids]

        
        train_dataset = Subset(train_dataset_ori, train_ids)
        val_dataset = Subset(train_dataset_ori, val_ids)

        val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=True)
        val_loader.mean, val_loader.std = mean, std

    else:
        train_dataset = train_dataset_ori


    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

    # Initialize variables to track the min and max values
    min_val = float('inf')
    max_val = float('-inf')

    max_target = float('-inf')
    # Loop over the dataset
    for data, target in train_loader:
        min_val = torch.tensor(min(min_val, data.min().item()))
        max_val = torch.tensor(max(max_val, data.max().item()))
        max_target = torch.tensor(max(max_target, target.max().item()))
        

    print(f'GTSRB dataset - Min value: {min_val}, Max value: {max_val}, no_classes: {max_target}')

    train_loader.mean, train_loader.std, train_loader.min, train_loader.max, train_loader.normalised = mean, std, min_val, max_val, normalise
    test_loader.mean, test_loader.std, test_loader.min, test_loader.max, test_loader.normalised = mean, std, min_val, max_val, normalise

    if val_split:
        val_loader.mean, val_loader.std, val_loader.min, val_loader.max, val_loader.normalised = mean, std, min_val, max_val, normalise
        return train_loader, val_loader, test_loader
    else:
        return train_loader, test_loader
    
# TODO: add code to download tiny imagenet

def load_tinyimagenet(batch_size=64, normalise=True, train_transforms=[transforms.RandomHorizontalFlip(), transforms.RandomCrop(64, 4, padding_mode='edge'),], val_split=True, data_root='./data'):
    """
    Loads the TinyImageNet dataset with specified transformations and normalization.
    
    Args:
        batch_size (int, optional): The number of samples per batch. Default is 64.
        normalise (bool, optional): Whether to normalize the dataset. Default is True.
        train_transforms (list, optional): List of transformations to apply to the training data. Default is [transforms.RandomHorizontalFlip(), transforms.RandomCrop(64, 4, padding_mode='edge')].
        val_split (bool, optional): Whether to split the training data into training and validation sets. Default is True.
        data_root (str, optional): Root directory of the dataset. Default is './data'.
    
    Returns:
        tuple: If val_split is True, returns a tuple of DataLoader objects (train_loader, val_loader, test_loader). Otherwise, returns (train_loader, test_loader).
    
    The returned DataLoader objects have the following attributes:
        - mean: The mean used for normalization.
        - std: The standard deviation used for normalization.
        - min: The minimum value in the dataset.
        - max: The maximum value in the dataset.
        - normalised: Whether the dataset was normalized.
    """
    if normalise:
        mean = torch.tensor([0.4802, 0.4481, 0.3975])
        std = torch.tensor([0.2302, 0.2265, 0.2262])
    else:
        mean = torch.tensor([.5, .5, .5])
        std = torch.tensor([1, 1, 1])

    if normalise:
        train_transform = transforms.Compose([
            *train_transforms,
            transforms.ToTensor(),
            transforms.Normalize(mean, std),
        ])
        test_transform = transforms.Compose([
            transforms.ToTensor(),
            transforms.Normalize(mean, std),
        ])
    else:
        train_transform = transforms.Compose([
            *train_transforms,
            transforms.ToTensor(),
        ])
        test_transform = transforms.Compose([
            transforms.ToTensor(),
        ])

    train_dataset = datasets.ImageFolder(root=data_root + '/train', transform=train_transform)
    test_dataset = datasets.ImageFolder(root=data_root + '/val', transform=test_transform)
    if val_split:
        train_dataset, val_dataset = random_split(train_dataset, [0.8, 0.2])
        val_loader = DataLoader(val_dataset, batch_size=batch_size, shuffle=True, num_workers=2)
        val_loader.mean, val_loader.std = mean, std
    

    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True, num_workers=4)
    test_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False, num_workers=4)
    
    # Initialize variables to track the min and max values
    min_val = float('inf')
    max_val = float('-inf')

    # Loop over the dataset
    for data, _ in train_loader:
        min_val = torch.tensor(min(min_val, data.min().item()))
        max_val = torch.tensor(max(max_val, data.max().item()))

    print(f'TinyImageNet dataset - Min value: {min_val}, Max value: {max_val}')
    
    train_loader.mean, train_loader.std, train_loader.min, train_loader.max, train_loader.normalised = mean, std, min_val, max_val, normalise
    test_loader.mean, test_loader.std, test_loader.min, test_loader.max, test_loader.normalised = mean, std, min_val, max_val, normalise
    
    if val_split:
        val_loader.mean, val_loader.std, val_loader.min, val_loader.max, val_loader.normalised = mean, std, min_val, max_val, normalise
        return train_loader, val_loader, test_loader
    else:
        return train_loader, test_loader