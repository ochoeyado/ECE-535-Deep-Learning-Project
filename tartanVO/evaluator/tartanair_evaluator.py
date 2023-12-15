# Copyright (c) 2020 Carnegie Mellon University, Wenshan Wang <wenshanw@andrew.cmu.edu>
# For License information please see the LICENSE file in the root directory.

import numpy as np
from evaluator_base import ATEEvaluator, RPEEvaluator, KittiEvaluator, transform_trajs, quats2SEs
from os.path import isdir, isfile

# from trajectory_transform import timestamp_associate

class TartanAirEvaluator:
    def __init__(self, scale = False, round=1):
        self.ate_eval = ATEEvaluator()
        self.rpe_eval = RPEEvaluator()
        self.kitti_eval = KittiEvaluator()
        
    def evaluate_one_trajectory(self, gt_traj, est_traj, scale=False, kittitype=True):
        """
        scale = True: calculate a global scale
        """
        # load trajectories
        try:
            gt_traj = np.loadtxt(gt_traj)
            est_traj = np.loadtxt(est_traj)
        except:
            pass
        
        if gt_traj.shape[0] != est_traj.shape[0]:
            raise Exception("POSEFILE_LENGTH_ILLEGAL")
        if gt_traj.shape[1] != 7 or est_traj.shape[1] != 7:
            raise Exception("POSEFILE_FORMAT_ILLEGAL")

        # transform and scale
        gt_traj_trans, est_traj_trans, s = transform_trajs(gt_traj, est_traj, scale)
        gt_SEs, est_SEs = quats2SEs(gt_traj_trans, est_traj_trans)

        ate_score, gt_ate_aligned, est_ate_aligned = self.ate_eval.evaluate(gt_traj, est_traj, scale)
        rpe_score = self.rpe_eval.evaluate(gt_SEs, est_SEs)
        kitti_score = self.kitti_eval.evaluate(gt_SEs, est_SEs, kittitype=kittitype)

        return { 
                'kitti_score': kitti_score,
                'gt_aligned': gt_ate_aligned, 
                'est_aligned': est_ate_aligned,
                'ate_score': ate_score, 
                'rpe_score': rpe_score,} #Moved ate_score and rpe_score to bottom

if __name__ == "__main__":
    
    # scale = True for monocular track, scale = False for stereo track
    aicrowd_evaluator = TartanAirEvaluator() #         -pose_gt ***************************Vurrently: KiTTi 10.txt
    result = aicrowd_evaluator.evaluate_one_trajectory('tartanVO\evaluator\pose_gt.txt', 'tartanVO\evaluator\pose_est.txt', scale=True)
    print(result)

#04.txt did not have enough data for ground truth