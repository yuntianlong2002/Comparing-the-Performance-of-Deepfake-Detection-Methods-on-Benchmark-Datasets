-- SQLite
SELECT Method, Dataset, ConfusionMatrix, Loss, Acc, AUC, AP, FrameConfusionMatrix, FrameAUC, FrameACC, Description
FROM Results
WHERE Method = 'xception_dftimit_lq'