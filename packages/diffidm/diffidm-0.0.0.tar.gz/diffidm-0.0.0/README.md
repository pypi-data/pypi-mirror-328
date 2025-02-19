# DiffIDM [[Arxiv](https://arxiv.org/abs/2412.16750)]

This is the official code of our paper "Gradient-based Trajectory Optimization with Parallelized Traffic Simulation", which has been accepted to ICRA 2025. Here we provide the code for parallelized differentiable IDM computation layer, which could be easily adopted for larger scale traffic simulators. The computation layer can handle upto **2 million vehicles** in real time using either CPU or GPU. We also provide our experiment code for filtering vehicle trajectories in NGSim dataset using our simulator. Please see our paper for more details.

![Parallelization scheme](/static/parallel.png)

# Install

You need to install [pytorch](https://pytorch.org/) to use our computation layer. Then, you can install our computation layer using `pip`.
```bash
pip install diffidm
```

After installation, you can use the computation layer as follows.
```python
import torch
from diffidm.layer import IDMLayer

num_vehicles = int(1e6)   # 1M vehicles

### randomly generate IDM variables


```

# Usage: Trajectory filtering for NGSIM dataset

As demonstrated in our paper, we can use our computation layer to filter physically unrealistic vehicle motions from their trajectories captured in real-world. We tested our filtering algorithm on [NGSIM](https://data.transportation.gov/stories/s/Next-Generation-Simulation-NGSIM-Open-Data/i5zb-xe34#ngsim-vehicle-trajectories-and-supporting-data) dataset. To run the algorithm, first download the dataset (1.53GB) from this [page](https://data.transportation.gov/Automobiles/Next-Generation-Simulation-NGSIM-Vehicle-Trajector/8ect-6jqj/about_data) to `data` directory, under the name of `ngsim.csv`. Then, preprocess the data with the following command.

```bash
python ngsim_preprocess.py
```

This preprocessing step generates input data for our filtering algorithm, which would be saved in `input/`. Then, we can use the following command to filter the NGSIM trajectories in `us-101` category using our computation layer. Please see `ngsim_filter.py` for the details abour arguments.

```bash
CUDA_VISIBLE_DEVICES=0 OMP_NUM_THREADS=1 python ngsim_filter.py --token=us-101 --device=cuda 
```

The filtered trajectories and related optimization results (e.g. IDM parameters for each trip) are stored under `output/` directory. Finally, we can evaluate the filtered trajectories by comparing them with the ground truth data and generate the experimental results in the paper with following command. Also see `ngsim_eval.py` for the details about arguments.

```bash
python ngsim_eval.py --token=us-101 --render-traj-id=1000
```

The evaluation results are saved in `eval/`.

# Citation

If you found our work to be useful, please consider citing our work.
```bibtex
@article{son2024gradient,
  title={Gradient-based Trajectory Optimization with Parallelized Differentiable Traffic Simulation},
  author={Son, Sanghyun and Zheng, Laura and Clipp, Brian and Greenwell, Connor and Philip, Sujin and Lin, Ming C},
  journal={arXiv preprint arXiv:2412.16750},
  year={2024}
}
```

# Acknowledgement

We used [Wei Ma's NGSIM interface code](https://github.com/Lemma1/NGSIM-interface) for preprocessing NGSIM dataset. We appreciate this great work.