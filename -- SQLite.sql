-- SQLite
SELECT Method, Dataset, ConfusionMatrix, Loss, Acc, AUC, AP, FrameConfusionMatrix, FrameAUC, FrameACC, Description
FROM Results
order by AUC desc;