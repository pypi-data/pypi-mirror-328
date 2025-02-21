from typing import Dict, List

import networkx as nx
import numpy as np
import torch
from facenet_pytorch import InceptionResnetV1, fixed_image_standardization
from torch.utils.data.dataloader import DataLoader
from torchvision.transforms import Resize, ToTensor, Compose, Normalize

from identity_clustering.dataset import VideoDataset
from identity_clustering.facedetector import FacenetDetector
from identity_clustering.utils import extract_crops


class FaceCluster:

    def __init__(
            self, crops=None, similarity_threshold: int = 0.85, device: str = "cpu", allow_single_face_cluster: bool = False, is_profiling : bool = False, is_inference : bool = False, shape:tuple = (128,128)
    ):
        self.similarity_threshold = similarity_threshold
        self.device = torch.device(device)
        self.crops = crops   
        self.shape = shape
        self.is_inference = is_inference
    def _set_crops(self, crops) -> None:
        '''
        A setter function to set the threshold attribute
        Args :
         - crops : List[tuple] -> contains tuples with (frame_no(int), PIL Image of the cropped face, bbox(list(int)))

        Returns :
            None
        '''
        self.crops = crops

    def _set_threshold(self, threshold : float) -> None:
        '''
        A setter function to set the threshold attribute
        Args :
         - threshold : float -> threshold value.

        Returns :
            None
        '''
        self.similarity_threshold = threshold

    def _generate_connected_components(self, similarities):
        '''
        Helper function for the clustering function, takes in dot product similarities and clusters them based on a predefined threshold,
        the threshold can be set by the user when intializing the class or can be set while calling the `cluster_faces` function
        
        Args :
         - similarities : np.ndarray -> similarity matrix (attention without scaling)

        Returns :
         - components : list -> list of clustered faces
        '''
        graph = nx.Graph()
        n = similarities.shape[0]
        threshold = self.similarity_threshold
        mask = (similarities > threshold) & (~np.eye(n, dtype = bool))
        edges = np.argwhere(mask)
        graph.add_edges_from(map(tuple,edges))
        components_list = [list(component) for component in nx.connected_components(graph)]
        return components_list
    @torch.no_grad
    def get_similarities(self, crops_images):
        transform = Compose([Resize(self.shape), ToTensor()])
        faces = torch.stack([transform(face) for face in crops_images])
        faces = faces.to(self.device, non_blocking=True)
        embeddings_extractor = InceptionResnetV1(pretrained="vggface2").eval().to(self.device)
        embeddings = embeddings_extractor(faces)
        similarities = torch.mm(embeddings, embeddings.T).cpu().numpy()
        return similarities

    def cluster_faces(self, crops, threshold=None):
        '''
        Function that clusters the faces using the dot product similarity metric.
        
        Args:
         - crops : List[tuple] -> contains tuples with (frame_no(int), PIL Image of the cropped face, bbox(list(int)))
         - threshold : Optional[float] -> set to change the threshold attribute.
        
        Returns :
         - clustered_faces : Dict[int,list] -> returns a dictionary containing the identity as keys and all the faces associated with a single
                                               identity as a list.
        '''

        if threshold:
            self._set_threshold(threshold)

        if crops and self.is_inference:
            self._set_crops(crops)

        # Convert crops to PIL images
        crops_images = [row[3] for row in crops]

        similarities = self.get_similarities(crops_images)

        components = self._generate_connected_components(similarities)
        components = [sorted(component) for component in components]

        # Assigning each cluster to a unique identity
        clustered_faces = {}
        for identity_index, component in enumerate(components):
            for index, face_index in enumerate(component):
                component[index] = crops[face_index]

            clustered_faces[identity_index] = component



        return clustered_faces


def cluster(
    clust: FaceCluster,
    video_path: str,
    faces: List[tuple],
    pad_constant: int | tuple | None = 3,
) -> Dict[int, list]:
    crops = extract_crops(video_path, faces, pad_constant)
    clustered_faces = clust.cluster_faces(crops)
    return clustered_faces


def detect_faces(video_path, device):
    """  
    We'll be using the facenet detector that is required to detect the faces
    present in each frame. This function is only responsible to return
    a dictionary that contains the bounding boxes of each frame.
    Args:
        video_path: str - Path to the video
        device: str - indicates whether to leverage CPU or GPU for processing 
    returns: 
        dict: dict template:
            {
                frame_no: [[
                    [number, number, number, number],
                    [number, number, number, number],
                    ...
                    ...
                    [number, number, number, number]
                ]]
            }
        int: fps of the video
    """
    detector = FacenetDetector(device=device)

    # Read the video and its information
    dataset = VideoDataset([video_path])
    loader = DataLoader(
        dataset, shuffle=False, num_workers=0, batch_size=1, collate_fn=lambda x: x
    )

    # Detect the faces
    for item in loader:
        bboxes = {}
        video, indices, fps, frames = item[0]
        """
            Update bboxes dict with the bounding boxes present in each frame with the 
            frame number as the index and 
            a two dimensional list containing the bounding boxes as the value. 
        """
        bboxes.update({i: b for i, b in zip(indices, detector._detect_faces(frames))})
        found_faces = False
        for key in list(bboxes.keys()):
            if isinstance(bboxes[key], list):
                found_faces = True
                break

        if not found_faces:
            return None, indices[-1]
    return bboxes, fps