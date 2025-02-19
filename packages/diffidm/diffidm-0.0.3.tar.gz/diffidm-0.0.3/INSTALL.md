# DiffIDM [[Arxiv](https://arxiv.org/abs/2412.16750)]

This is the official code of our paper "Gradient-based Trajectory Optimization with Parallelized Traffic Simulation", which has been accepted to ICRA 2025. Here we provide the code for parallelized differentiable IDM computation layer, which could be easily adopted for larger scale traffic simulators. The computation layer can handle upto **2 million vehicles** in real time using either CPU or GPU. Please see our paper for more details.

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