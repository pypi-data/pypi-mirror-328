import torch as th
from typing import Union

IDM_DELTA = 4.0

class IDMLayer:
    '''
    Compute acceleration of a vehicle based on IDM model.
    Parameters are all PyTorch Tensors of shape [N,], where N is the number of vehicles, or batch.

     1. a_max: Maximum acceleration (> 0)
     2. a_min: Maximum deceleration (< 0)
     3. a_pref: Preferred acceleration (or deceleration)
     4. v_curr: Current velocity of ego vehicle
     5. v_target: Target velocity of ego vehicle
     6. pos_delta: Position delta from leading vehicle
     7. vel_delta: Velocity delta from leading vehicle
     8. min_space: Minimum desired distance to leading vehicle
     9. time_pref: Desired time to move forward with current speed
     10. delta_time: Length of time step
    '''
    @staticmethod
    def apply(a_max: th.Tensor, 
                a_min: th.Tensor,
                a_pref: th.Tensor, 
                v_curr: th.Tensor, 
                v_target: th.Tensor, 
                pos_delta: th.Tensor, 
                vel_delta: th.Tensor, 
                min_space: th.Tensor, 
                time_pref: th.Tensor,
                delta_time: th.Tensor,
                prevent_negative_speed: bool = True):

        optimal_spacing = IDMLayer.compute_optimal_spacing(
                            a_max, 
                            a_pref, 
                            v_curr, 
                            vel_delta, 
                            min_space, 
                            time_pref)
        
        '''
        Do not allow negative optimal spacing.

        If it is allowed to be negative, acceleration could become negative value even when the leading
        vehicle is much faster than ego vehicle, so it can accelerate more.
        '''
        optimal_spacing = IDMLayer.soft_min_clamp(optimal_spacing, 0.0)
        
        acc = IDMLayer.compute_acceleration(a_max,  
                                            v_curr, 
                                            v_target, 
                                            pos_delta,
                                            optimal_spacing)
        
        '''
        Do not allow acc to go below a_min or below the deceleration required to stop in delta_time.
        '''
        if prevent_negative_speed:
            acc_lb = -v_curr / delta_time
            acc_lb = th.max(acc_lb, a_min)
        else:
            acc_lb = a_min
        acc = IDMLayer.soft_min_clamp(acc, acc_lb)
        
        return acc
    
    @staticmethod
    def soft_min_clamp(x: th.Tensor, min_val: Union[th.Tensor, float]):
        return min_val + th.nn.functional.softplus(x - min_val)

    @staticmethod
    def compute_optimal_spacing(a_max: th.Tensor, 
                                a_pref: th.Tensor, 
                                v_curr: th.Tensor, 
                                vel_delta: th.Tensor, 
                                min_space: th.Tensor, 
                                time_pref: th.Tensor):

        optimal_spacing = (min_space + v_curr * time_pref + \
            ((v_curr * vel_delta) / (2 * th.sqrt(a_max * a_pref))))

        return optimal_spacing

    @staticmethod
    def compute_acceleration(a_max, 
                            v_curr, 
                            v_target, 
                            pos_delta,
                            optimal_spacing):
        acc = a_max * (1.0 - th.pow(v_curr / v_target, IDM_DELTA) - \
            th.pow((optimal_spacing / pos_delta), 2.0))

        return acc