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
from diffidm import IDMLayer

device = 'cuda' if torch.cuda.is_available() else 'cpu'
num_vehicles = int(1e6)   # 1M vehicles

print("Device:", device)
print("Number of vehicles:", num_vehicles)

### randomly generate IDM variables
a_max = torch.rand(num_vehicles, device=device) * 5 + 5             # [5, 10], maximum acceleration
a_min = torch.rand(num_vehicles, device=device) * 5 - 10            # [-10, -5], minimum acceleration
a_pref = torch.rand(num_vehicles, device=device) * 4.9 + 0.1        # [0.1, 5], preferred acceleration
v_curr = torch.rand(num_vehicles, device=device) * 40 + 20          # [20, 60], current velocity
v_target = torch.rand(num_vehicles, device=device) * 40 + 20        # [20, 60], target velocity
pos_delta = torch.rand(num_vehicles, device=device) * 10 + 5        # [5, 15], headway distance to the leading vehicle
vel_delta = torch.rand(num_vehicles, device=device) * 20 + 10       # [10, 30], relative velocity to the leading vehicle
min_space = torch.rand(num_vehicles, device=device) * 9 + 1         # [1, 10], minimum space headway
time_pref = torch.rand(num_vehicles, device=device) * 4.9 + 0.1     # [0.1, 5], desired time headway
delta_time = torch.full((num_vehicles,), 0.01, device=device)       # 0.01, simulation time step

a_max = a_max.requires_grad_()
a_min = a_min.requires_grad_()
a_pref = a_pref.requires_grad_()
v_curr = v_curr.requires_grad_()
v_target = v_target.requires_grad_()
pos_delta = pos_delta.requires_grad_()
vel_delta = vel_delta.requires_grad_()
min_space = min_space.requires_grad_()
time_pref = time_pref.requires_grad_()
delta_time = delta_time.requires_grad_()
print("IDM variables generated.")

### forward pass: compute acceleration using IDM
start_event = torch.cuda.Event(enable_timing=True)
end_event = torch.cuda.Event(enable_timing=True)
start_event.record()

acc = IDMLayer.apply(
    a_max,
    a_min,
    a_pref,
    v_curr,
    v_target,
    pos_delta,
    vel_delta,
    min_space,
    time_pref,
    delta_time,
)

end_event.record()
torch.cuda.synchronize()
elapsed_time = start_event.elapsed_time(end_event)
print(f"Forward pass time: {elapsed_time} ms")

### backward pass: compute gradients of IDM variables
start_event.record()
acc.sum().backward()
end_event.record()
torch.cuda.synchronize()
elapsed_time = start_event.elapsed_time(end_event)
print(f"Backward pass time: {elapsed_time} ms")
```

If installed correctly, it would print as follows.
```bash
Device: cuda
Number of vehicles: 1000000
IDM variables generated.
Forward pass time: 1.222208023071289 ms
Backward pass time: 3.7359039783477783 ms
```

Now you can use it in your code!

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