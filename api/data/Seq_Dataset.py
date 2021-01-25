import pandas as pd
from PIL import Image

class Seq_dataset(object):
    def __init__(self, 
        image_dir, 
        seq_len = 32, 
        transform = None,
        image_ext = ['.jpg', '.bmp', '.png']):
        self._opt = opt
        assert transform is not None
        self._transform = transform
        self.image_ext = image_ext
        self.seq_len = seq_len
        # read dataset
        self._read_dataset()

    def __getitem__(self, index):
        assert (index < self._dataset_size)
        images = []
        labels = []
        img_paths = []
        frames_ids = []
        df = self.sample_seqs[index]
        for i, row in df.iterrows():
            img_path = row['path']
            image = Image.open(img_path).convert('RGB')
            image = self._transform(image)
            frame_id = row['frames_ids']
            images.append(image)
            img_paths.append(img_path)
            frames_ids.append(frame_id)
        # pack data
        sample = {'image': torch.stack(images,dim=0),
                  'path': img_paths,
                  'index': index,
                  'frames_ids':frames_ids
                  }
        return sample
    def _read_dataset(self):
        #sample them 
        seq_len = self.seq_len
        frames_paths = glob.glob(os.path.join(self.image_dir, '*'))
        frames_paths = [x for x in frames_paths if any([ext in x for ext in self.image_ext])]
        frames_paths = sorted(frames_paths)
        self._data = {'path': frames_paths, 'frames_ids': np.arange(len(frames_paths))} # dataframe are easier for indexing

        self._data = pd.DataFrame.from_dict(self._data)
        self.sample_seqs = []
        N = seq_len
        for i in range(len(self._data['path'])//N + 1):
            start, end = i*N, i*N + seq_len
            if end >= len(self._data):
                start, end = len(self._data) - seq_len, len(self._data)
            new_df = self._data.iloc[start:end]
            if not len(new_df) == seq_len:
                assert len(new_df) < seq_len
                count = seq_len - len(new_df)
                for _ in range(count):
                    new_df = new_df.append(new_df.iloc[-1])
            assert len(new_df) == seq_len
            self.sample_seqs.append(new_df)
        self._ids = np.arange(len(self.sample_seqs)) 
        self._dataset_size = len(self._ids)

    def __len__(self):
        return self._dataset_size
